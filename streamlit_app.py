import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


sns.set_theme(style="whitegrid")

# Cargar los datos
df = pd.read_csv('final_df.csv')

# Función para crear una visualización de dispositivos
def plot_device_distribution(df):
    plt.figure(figsize=(10, 6))
    device_count = df['device'].value_counts()
    sns.barplot(x=device_count.index, y=device_count.values, palette='viridis')
    plt.title('Distribución de Dispositivos Utilizados')
    plt.xlabel('Dispositivo')
    plt.ylabel('Número de Eventos')
    plt.xticks(rotation=45)
    return plt

# Función para crear una visualización de canales de origen
def plot_channel_efficiency(df):
    plt.figure(figsize=(14, 7))
    channel_count = df['source_channel'].value_counts()
    sns.barplot(x=channel_count.index, y=channel_count.values, palette='coolwarm')
    plt.title('Eficacia de los Canales de Origen')
    plt.xlabel('Canal de Origen')
    plt.ylabel('Número de Eventos')
    plt.xticks(rotation=45)
    return plt

# Configuración del layout del dashboard
st.set_page_config(layout="wide")

# Título del Dashboard
st.title('Dashboard de Análisis de Marketing')

# Columnas para las visualizaciones
col1, col2 = st.columns(2)

# Visualización en la primera columna
with col1:
    st.header("Distribución de Dispositivos")
    st.pyplot(plot_device_distribution(df))

# Visualización en la segunda columna
with col2:
    st.header("Eficacia de los Canales")
    st.pyplot(plot_channel_efficiency(df))

def plot_channel_efficiency(df):
    plt.figure(figsize=(14, 7))
    channel_count = df['source_channel'].value_counts().sort_values(ascending=False)
    sns.barplot(x=channel_count.index, y=channel_count.values, palette='coolwarm')
    plt.title('Eficacia de los Canales de Origen')
    plt.xlabel('Canal de Origen')
    plt.ylabel('Número de Eventos')
    plt.xticks(rotation=45)
    return plt


