import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



sns.set_theme(style="whitegrid")

# Cargar los datos
df = pd.read_csv('final_df.csv')



# Configuración del layout del dashboard
st.set_page_config(layout="wide")

# Título del Dashboard
st.title('Dashboard de Análise da Campanha de Marketing da SuperFruits')

# Columnas para las visualizaciones
col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)
col7 = st.columns(1)



def plot_age_range_distribution(df):
    # Contar la frecuencia de cada rango de edad único
    age_range_counts = df['age'].value_counts()

    # Crear la figura y el gráfico de barras
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x=age_range_counts.index, y=age_range_counts.values, palette='coolwarm', ax=ax)
    ax.set_title('Distribución por Rango de Edad en la Campaña')
    ax.set_xlabel('Rango de Edad')
    ax.set_ylabel('Frecuencia')
    ax.set_xticklabels(age_range_counts.index, rotation=45)
    plt.tight_layout()

    return fig

with col1:
    st.header("Conseguimos atingir os clientes ideais?")
    st.subheader('O público-alvo principal são indivíduos de 18 a 30 anos. O gráfico "Idade do Cliente" indica que a maioria das visitas ocorre exatamente nessa faixa etária, seguido pelo grupo de 31 a 34 anos. Isso mostra uma correspondência efetiva entre o público-alvo e os usuários que estão interagindo com o serviço.')
    st.pyplot(plot_age_range_distribution(df))

def plot_channel_efficiency(df):
    plt.figure(figsize=(12, 6))
    channel_count = df['source_channel'].value_counts().sort_values(ascending=False)
    sns.barplot(x=channel_count.index, y=channel_count.values, palette='coolwarm')
    plt.title('Eficacia de los Canales de Origen')
    plt.xlabel('Canal de Origen')
    plt.ylabel('Número de Eventos')
    plt.xticks(rotation=45)
    return plt

def plot_device_distribution_pie(df):
    device_count = df['device'].value_counts()
    colors = sns.color_palette('coolwarm', len(device_count))
    
    # Criar a figura e o gráfico de pizza
    fig, ax = plt.subplots(figsize=(12, 6))
    wedges, texts, autotexts = ax.pie(device_count, labels=device_count.index, autopct='%1.1f%%', startangle=140, colors=colors)
    
    # Adicionar sombreamento para um efeito pseudo-3D
    for w in wedges:
        w.set_edgecolor('black')
        w.set_linewidth(1)
        w.set_linestyle('-')
    
    ax.set_title('Distribuição de Dispositivos Utilizados')
    return fig

# No seu dashboard Streamlit
with col2:
    st.header("Os nossos anúncios devem ser dirigidos a um ecrã de telefone ou de computador?")
    st.subheader('O gráfico "Dispositivos do Cliente" mostra uma clara preferência por dispositivos móveis em relação a desktops.')
    st.pyplot(plot_device_distribution_pie(df))


def plot_performance_by_channel(df, selected_element):
    # Filtrar o dataframe pelo tipo de interação selecionado
    filtered_df = df[df['element'] == selected_element]
    
    # Contar o número de eventos por plataforma de mídia social
    channel_count = filtered_df['source_channel'].value_counts()
    
    # Criar a figura e o gráfico de barras
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x=channel_count.index, y=channel_count.values, palette='coolwarm', ax=ax)
    ax.set_title(f'Desempenho por Plataforma de Mídia Social - {selected_element}')
    ax.set_xlabel('Plataforma de Mídia Social')
    ax.set_ylabel('Número de Eventos')
    ax.set_xticklabels(channel_count.index, rotation=45)
    plt.tight_layout()
    return fig


with col3:
    st.header("Todos os canais estão a ter sucesso?")
    st.subheader('Considerando que o público-alvo é mais jovem e provavelmente mais engajado em plataformas sociais como TikTok, Facebook e Instagram, esses canais podem estar apresentando um melhor desempenho. LinkedIn e Twitter podem não ser tão eficazes para o público mais jovem, que procura conteúdo de entretenimento e socialização.')
    
    # Criar um seletor para os tipos de interação
    #interaction_types = df['element'].unique()
    interaction_types = ['comment', 'like', 'buy', 'share', 'follow']
    selected_interaction = st.selectbox("Escolha o tipo de interação:", interaction_types)
    
    # Mostrar o gráfico com base no tipo de interação selecionado
    st.pyplot(plot_performance_by_channel(df, selected_interaction))  



def plot_likes_by_hour(df):
    # Certifique-se de que a coluna 'time' é do tipo datetime
    df['time'] = pd.to_datetime(df['time'], errors='coerce')
    
    # Filtrar apenas as linhas onde 'element' é 'like'
    likes_df = df[df['element'] == 'like'].copy()

    # Criar a coluna 'hour' usando loc para evitar o SettingWithCopyWarning
    likes_df['hour'] = likes_df['time'].dt.hour

    # Agrupar pelo horário e contar as ocorrências
    likes_per_hour = likes_df.groupby('hour').size()

    # Configurar o estilo do Seaborn
    sns.set(style="whitegrid")

    # Criar a figura e o gráfico de barras
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x=likes_per_hour.index, y=likes_per_hour.values, palette='coolwarm', ax=ax)

    # Adicionar títulos e rótulos
    ax.set_title('Número de "Likes" por Hora do Dia')
    ax.set_xlabel('Hora do Dia')
    ax.set_ylabel('Número de "Likes"')
    
    # Retorna a figura contendo o gráfico
    return fig

# No seu dashboard Streamlit
with col4:
    st.header("A que horas do dia é que recebemos mais likes?")
    st.subheader('As horas com o maior número de "likes" são às 12h e às 22h, com 11 "likes" cada. Isso confirma o que foi visto no gráfico, onde essas duas barras são as mais altas.')
    st.pyplot(plot_likes_by_hour(df))

def plot_purchases_by_hour(df):
    # Filtrar el dataframe para eventos de compra ('buy')
    purchases_by_hour = df[df['element'] == 'buy'].groupby('hour').size().reset_index(name='count')
    
    # Crear el gráfico de líneas para las compras por hora del día
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=purchases_by_hour, x='hour', y='count', marker='o', color='green')
    plt.title('Distribución de Compras por Hora del Día')
    plt.xlabel('Hora del Día')
    plt.ylabel('Número de Compras')
    plt.xticks(range(9, 24))
    plt.grid(True)
    plt.tight_layout()  # Ajustar la disposición para que no cortemos los labels
    return plt    

with col5:
    st.header("A que horas do dia obtemos mais compras?")
    st.subheader('A análise indica que as horas do dia com o maior número de compras são às 11h e às 12h, ambas com 8 compras. Isso sugere que há um pico de atividade de compra no final da manhã.')
    st.pyplot(plot_purchases_by_hour(df)) 

def plot_top_likes_days(df):
    # Convertir la columna 'date' a tipo datetime si aún no lo es
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    
    # Filtrar por 'like' y agrupar por fecha
    likes_by_date = df[df['event_type'] == 'click'].groupby('date').size().reset_index(name='count')
    likes_by_date_sorted = likes_by_date.sort_values('count', ascending=True)

    # Crear la figura y el gráfico de barras
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(likes_by_date_sorted.head(15)['date'].dt.strftime('%Y-%m-%d'), likes_by_date_sorted.head(15)['count'])
    ax.set_title('Días con Más Interacion en la Campaña')
    ax.set_xlabel('Fecha')
    ax.set_ylabel('Número de Clicks')
    ax.set_xticklabels(likes_by_date_sorted.head(15)['date'].dt.strftime('%Y-%m-%d'), rotation=90)
    plt.tight_layout()

    return fig

with col6:
    st.header("Quando é que a campanha que teve melhor desempenho?")
    st.subheader('Com base no gráfico de barras, podemos ver que a campanha teve o melhor desempenho no dia 12 de maio de 2022, onde houve o maior número de cliques.')
    st.pyplot(plot_top_likes_days(df))


