

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# FUNCION PARA REALIZAR LOS CALCULOS
def calcular_balance(masa_inicial, humedad_inicial, humedad_final):

    Hi = humedad_inicial / 100
    Hf = humedad_final / 100

    agua_inicial = masa_inicial * Hi
    materia_seca = masa_inicial - agua_inicial

    masa_final = materia_seca / (1 - Hf)
    agua_retirada = masa_inicial - masa_final
    agua_final = masa_final * Hf

    rendimiento = (masa_final / masa_inicial) * 100

    porcentaje_agua_retirada = (
        agua_retirada / agua_inicial
    ) * 100

    return {
        "agua_inicial": agua_inicial,
        "materia_seca": materia_seca,
        "masa_final": masa_final,
        "agua_retirada": agua_retirada,
        "agua_final": agua_final,
        "rendimiento": rendimiento,
        "porcentaje_agua_retirada": porcentaje_agua_retirada
    }


# FUNCION PRINCIPAL DE LA APLICACION
def main():

    st.set_page_config(
        page_title="SecaAgro",
        page_icon="🌱",
        layout="centered"
    )

    st.title("🌱 SecaAgro")
    st.subheader("Calculadora de balance de masa en el secado agrícola")

    st.write(
        "Esta aplicación permite calcular el balance de masa "
        "durante el proceso de secado de productos agrícolas."
    )

    st.caption("Todos los porcentajes de humedad se expresan en base húmeda.")

    st.divider()

    # ENTRADA DE DATOS
    st.header("1. Datos del proceso")

    producto = st.text_input(
        "Nombre del producto agrícola",
        placeholder="Ejemplo: Mango, banano, yuca..."
    )

    col1, col2 = st.columns(2)

    with col1:
        masa_inicial = st.number_input(
            "Masa inicial (kg)",
            min_value=0.0,
            value=100.0,
            step=1.0
        )

        humedad_inicial = st.number_input(
            "Humedad inicial (%)",
            value=80.0,
            step=1.0
        )

    with col2:
        humedad_final = st.number_input(
            "Humedad final deseada (%)",
            value=20.0,
            step=1.0
        )

    st.divider()

    # VALIDACIONES Y CALCULOS
    if not producto.strip():

        st.info("Ingrese el nombre del producto para comenzar.")

    elif masa_inicial <= 0:

        st.error("La masa inicial debe ser mayor que cero.")

    elif humedad_inicial <= 0 or humedad_inicial >= 100:

        st.error(
            "La humedad inicial debe ser mayor que 0 % "
            "y menor que 100 %."
        )

    elif humedad_final < 0:

        st.error("La humedad final no puede ser negativa.")

    elif humedad_final >= humedad_inicial:

        st.error(
            "La humedad final debe ser menor que la humedad inicial."
        )

    else:

        resultados = calcular_balance(
            masa_inicial,
            humedad_inicial,
            humedad_final
        )

        # RESULTADOS PRINCIPALES
        st.header("2. Resultados del balance de masa")

        col3, col4 = st.columns(2)

        with col3:
            st.metric(
                "Masa final",
                f"{resultados['masa_final']:.2f} kg"
            )

        with col4:
            st.metric(
                "Agua retirada",
                f"{resultados['agua_retirada']:.2f} kg"
            )

        st.divider()

        # TABLA DE DATOS Y RESULTADOS
        st.header("3. Tabla de resultados")

        datos = {
            "Concepto": [
                "Producto",
                "Masa inicial",
                "Humedad inicial",
                "Humedad final deseada",
                "Agua inicial",
                "Materia seca",
                "Masa final",
                "Agua final",
                "Agua retirada",
                "Rendimiento del proceso",
                "Porcentaje de agua retirada"
            ],

            "Valor": [
                producto,
                f"{masa_inicial:.2f} kg",
                f"{humedad_inicial:.2f} %",
                f"{humedad_final:.2f} %",
                f"{resultados['agua_inicial']:.2f} kg",
                f"{resultados['materia_seca']:.2f} kg",
                f"{resultados['masa_final']:.2f} kg",
                f"{resultados['agua_final']:.2f} kg",
                f"{resultados['agua_retirada']:.2f} kg",
                f"{resultados['rendimiento']:.2f} %",
                f"{resultados['porcentaje_agua_retirada']:.2f} %"
            ]
        }

        tabla = pd.DataFrame(datos)

        st.dataframe(
            tabla,
            use_container_width=True,
            hide_index=True
        )

        # DESCARGAR RESULTADOS
        archivo_csv = tabla.to_csv(index=False).encode("utf-8-sig")

        st.download_button(
            label="Descargar resultados en CSV",
            data=archivo_csv,
            file_name="resultados_secaagro.csv",
            mime="text/csv"
        )

        st.divider()

        # GRAFICA DEL PROCESO
        st.header("4. Gráfica del balance de masa")

        fig, ax = plt.subplots(figsize=(8, 5))

        posiciones = [0, 1]

        materia_seca = resultados["materia_seca"]
        agua_inicial = resultados["agua_inicial"]
        agua_final = resultados["agua_final"]

        ax.bar(
            posiciones,
            [agua_inicial, agua_final],
            label="Agua",
            color="#4A90E2"
        )

        ax.bar(
            posiciones,
            [materia_seca, materia_seca],
            bottom=[agua_inicial, agua_final],
            label="Materia seca",
            color="#E8B04A"
        )

        ax.set_xticks(posiciones)
        ax.set_xticklabels(["Antes del secado", "Después del secado"])
        ax.set_ylabel("Masa (kg)")
        ax.set_title(f"Balance de masa del {producto}")
        ax.legend()
        ax.grid(axis="y", alpha=0.3)

        plt.tight_layout()

        st.pyplot(fig)
        plt.close(fig)

        st.divider()

        # INTERPRETACION
        st.header("5. Interpretación de resultados")

        st.write(
            f"El producto agrícola seleccionado es **{producto}**. "
            f"Su masa inicial es de **{masa_inicial:.2f} kg**, "
            f"con una humedad inicial de **{humedad_inicial:.2f} %**."
        )

        st.write(
            f"Para alcanzar una humedad final de "
            f"**{humedad_final:.2f} %**, se deben retirar "
            f"**{resultados['agua_retirada']:.2f} kg de agua**."
        )

        st.write(
            f"Después del secado, se obtiene una masa final de "
            f"**{resultados['masa_final']:.2f} kg**."
        )

        st.success(
            "El balance de masa se calculó correctamente."
        )


# EJECUTAR LA APLICACION
if __name__ == "__main__":
    main()
