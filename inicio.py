import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    st.set_page_config(page_title="Inicio", page_icon="🏠",layout="wide")
    st.title("Bienvenido a mi aplicación de Streamlit")
    st.write("Esta es la página de inicio. Aquí puedes consultar informacion sobre el total de la población en Colombia por departamento.")

    df = pd.read_csv("datos/poblacion.csv")
    st.dataframe(df.head())
    st.write("Estadísticas descriptivas:")
    st.write(df.describe())

    fig = px.bar(df, x='Departamento', y='Poblacion', title='Población por Departamento en Colombia')
    st.plotly_chart(fig)

    fig_pie = px.pie(df, names='Departamento', values='Poblacion', title='Distribución de la Población por Departamento')
    st.plotly_chart(fig_pie)

    st.sidebar.title("Navegación")
    st.sidebar.write("Selecciona una página para navegar:")
    paguina = st.sidebar.selectbox("Páginas", ["Inicio", "Análisis", "Predicciones"])

    if paguina == "Inicio":
        st.write("Estás en la página de inicio.")   
    elif paguina == "Análisis":
        st.write("Aquí puedes realizar análisis de datos.")     
    elif paguina == "Predicciones":
        st.write("Aquí puedes realizar predicciones basadas en tus datos.")
        


if __name__ == "__main__":    
    main()
