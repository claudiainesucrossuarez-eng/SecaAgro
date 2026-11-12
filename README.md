
# SecaAgro 🌱

## Descripción
SecaAgro es una aplicación web desarrollada en Python mediante Streamlit. Su objetivo es calcular y analizar el balance de masa durante el proceso de secado de productos agrícolas como mango, banano, yuca y plátano.

## Objetivo
Determinar la cantidad de agua que debe retirarse de un producto agrícola para alcanzar una humedad final deseada, conservando la materia seca.

## Datos de entrada
- Nombre del producto agrícola.
- Masa inicial (kg).
- Humedad inicial (%).
- Humedad final deseada (%).

## Resultados
- Agua inicial.
- Materia seca.
- Masa final esperada.
- Agua que se debe retirar.
- Rendimiento másico del proceso.
- Porcentaje de agua retirada.

## Herramientas utilizadas
- Python.
- Streamlit.
- Pandas.
- Matplotlib.

## Instalación

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

## Ejecución

Ejecutar el siguiente comando:

```bash
streamlit run app.py
```

## Validaciones
La aplicación verifica que:
- El nombre del producto no esté vacío.
- La masa inicial sea mayor que cero.
- La humedad inicial esté entre 0 y 100 %.
- La humedad final esté entre 0 y 100 %.
- La humedad final no supere la humedad inicial.

## Autores
## Autores

## Información académica

**Proyecto:** SecaAgro – Calculadora de balance de masa en el secado agrícola.

**Área:** Programación.

**Carrera:** Ingeniería Agroindustrial.

**Tipo de proyecto:** Desarrollo de una aplicación web.

**Integrantes:**
- Liseth Galvan
- Melissa Alvares
- Juan Ruiz
- Claudia Ucroz

## Tecnologías de desarrollo

- Python 3.13
- Visual Studio Code
- Streamlit
- Pandas
- Matplotlib

## Funcionalidad principal

La aplicación permite ingresar las características de un producto agrícola y calcular su balance de masa durante el proceso de secado, mostrando resultados numéricos, tablas y gráficas.