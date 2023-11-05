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
st.text("Por Martha Dominguez de Gouveia")

# Columnas para las visualizaciones
col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)
st.title('Responder à pergunta-chave de marketing: No próximo mês o orçamento é aumentado para 1200€, e o Marketing vai duplicar para 400€ o que vai gastar num canal. Qual é que deve ser escolhido? Devemos focar o nosso marketing no Instagram ou no TikTok na próxima campanha? ')

st.markdown("""
    <style>
    .font {
        font-size:26px;
    }
    </style>
    <div class="font">
        <p>Após uma análise detalhada dos dados das campanhas anteriores e considerando o aumento do orçamento para 1200€, 
        com uma duplicação do investimento num canal específico até 400€, recomendamos alocar o orçamento adicional ao canal que 
        demonstrou o melhor retorno sobre o investimento (ROI).</p> 
        <p>A nossa análise mostrou que o custo por clique e o custo por conversão variam significativamente entre os diferentes canais. 
        Com base nos dados atuais, o Instagram e o TikTok são os dois principais candidatos para o investimento adicional.</p>
        <p>Para tomar uma decisão informada, devemos considerar não apenas o custo por interação, mas também a qualidade e a taxa de 
        conversão dessas interações. Se o objetivo é maximizar a quantidade de interações pelo menor custo, então o canal com o menor 
        custo por clique deve ser escolhido. Se o objetivo é obter o maior número de conversões pelo menor custo, então o canal com o 
        menor custo por conversão deve ser priorizado.</p>
        <p>Com isso em mente, e dado que o custo por conversão e o custo por clique foram mais favoráveis no Instagram em comparação 
        com o TikTok, sugerimos alocar o aumento do orçamento ao Instagram. Esta recomendação é baseada no desempenho atual e poderá 
        ser ajustada conforme os dados mais recentes forem analisados.</p>
    </div>
    """, unsafe_allow_html=True)

st.text('Atenciosamente')
st.text('Martha Dominguez de Gouveia')
st.text('Equipe de Análise de Dados')

col7, col8 = st.columns(2)






def plot_age_range_distribution(df):
    
    age_range_counts = df['age'].value_counts()

    # Crear la figura y el gráfico de barras
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x=age_range_counts.index, y=age_range_counts.values, palette='coolwarm', ax=ax)
    ax.set_title('Distribuição por faixa etária na campanha')
    ax.set_xlabel('Faixa etária')
    ax.set_ylabel('Frequência')
    ax.set_xticklabels(age_range_counts.index, rotation=45)
    plt.tight_layout()

    return fig

with col1:
    st.header("Conseguimos atingir os clientes ideais?")
    st.text('O público-alvo principal são indivíduos de 18 a 30 anos. O gráfico "Idade do Cliente" indica que a maioria das visitas ocorre exatamente nessa faixa etária, seguido pelo grupo de 31 a 34 anos. Isso mostra uma correspondência efetiva entre o público-alvo e os usuários que estão interagindo com o serviço.')
    st.pyplot(plot_age_range_distribution(df))

def plot_channel_efficiency(df):
    plt.figure(figsize=(12, 6))
    channel_count = df['source_channel'].value_counts().sort_values(ascending=False)
    sns.barplot(x=channel_count.index, y=channel_count.values, palette='coolwarm')
    plt.title('Eficácia dos canais de origem')
    plt.xlabel('Canal de origem')
    plt.ylabel('Número de eventos')
    plt.xticks(rotation=45)
    return plt

def plot_device_distribution_pie(df):
    device_count = df['device'].value_counts()
    colors = sns.color_palette('coolwarm', len(device_count))
    
    
    fig, ax = plt.subplots(figsize=(12, 6))
    wedges, texts, autotexts = ax.pie(device_count, labels=device_count.index, autopct='%1.1f%%', startangle=140, colors=colors)
    
    
    for w in wedges:
        w.set_edgecolor('black')
        w.set_linewidth(1)
        w.set_linestyle('-')
    
    ax.set_title('Distribuição de Dispositivos Utilizados')
    return fig


with col2:
    st.header("Os nossos anúncios devem ser dirigidos a um ecrã de telefone ou de computador?")
    st.text('O gráfico "Dispositivos do Cliente" mostra uma clara preferência por dispositivos móveis em relação a desktops.')
    st.pyplot(plot_device_distribution_pie(df))


def plot_performance_by_channel(df, selected_element):
    
    filtered_df = df[df['element'] == selected_element]
    
    
    channel_count = filtered_df['source_channel'].value_counts()
    
    
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
    st.text('Considerando que o público-alvo é mais jovem e provavelmente mais engajado em plataformas sociais como TikTok, Facebook e Instagram, esses canais podem estar apresentando um melhor desempenho. LinkedIn e Twitter podem não ser tão eficazes para o público mais jovem, que procura conteúdo de entretenimento e socialização.')
    
    
    interaction_types = ['comment', 'like', 'buy', 'share', 'follow']
    selected_interaction = st.selectbox("Escolha o tipo de interação:", interaction_types)
    
    
    st.pyplot(plot_performance_by_channel(df, selected_interaction))  



def plot_likes_by_hour(df):
    
    df['time'] = pd.to_datetime(df['time'], errors='coerce')       
    likes_df = df[df['element'] == 'like'].copy()   
    likes_df['hour'] = likes_df['time'].dt.hour    
    likes_per_hour = likes_df.groupby('hour').size()    
    sns.set(style="whitegrid")   
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x=likes_per_hour.index, y=likes_per_hour.values, palette='coolwarm', ax=ax)   
    ax.set_title('Número de "Likes" por Hora do Dia')
    ax.set_xlabel('Hora do Dia')
    ax.set_ylabel('Número de "Likes"')
        
    return fig


with col4:
    st.header("A que horas do dia é que recebemos mais likes?")
    st.text('As horas com o maior número de "likes" são às 12h e às 22h, com 11 "likes" cada. Isso confirma o que foi visto no gráfico, onde essas duas barras são as mais altas.')
    st.pyplot(plot_likes_by_hour(df))

def plot_purchases_by_hour(df):
    
    purchases_by_hour = df[df['element'] == 'buy'].groupby('hour').size().reset_index(name='count')
    
    
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=purchases_by_hour, x='hour', y='count', marker='o', color='green')
    plt.title('Distribuição das compras por hora do dia')
    plt.xlabel('Hora do dia')
    plt.ylabel('Número de compras')
    plt.xticks(range(9, 24))
    plt.grid(True)
    plt.tight_layout()  
    return plt    

with col5:
    st.header("A que horas do dia obtemos mais compras?")
    st.text('A análise indica que as horas do dia com o maior número de compras são às 11h e às 12h, ambas com 8 compras. Isso sugere que há um pico de atividade de compra no final da manhã.')
    st.pyplot(plot_purchases_by_hour(df)) 

def plot_top_likes_days(df):
    
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    
    
    likes_by_date = df[df['event_type'] == 'click'].groupby('date').size().reset_index(name='count')
    likes_by_date_sorted = likes_by_date.sort_values('count', ascending=True)

    
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(likes_by_date_sorted.head(15)['date'].dt.strftime('%Y-%m-%d'), likes_by_date_sorted.head(15)['count'])
    ax.set_title('Dias com mais interesse na campanha.)
    ax.set_xlabel('Data')
    ax.set_ylabel('Número de cliques')
    ax.set_xticklabels(likes_by_date_sorted.head(15)['date'].dt.strftime('%Y-%m-%d'), rotation=90)
    plt.tight_layout()

    return fig

with col6:
    st.header("Quando é que a campanha que teve melhor desempenho?")
    st.text('Com base no gráfico de barras, podemos ver que a campanha teve o melhor desempenho no dia 12 de maio de 2022, onde houve o maior número de cliques.')
    st.pyplot(plot_top_likes_days(df))




buy_counts = df[df['element'] == 'buy']['source_channel'].value_counts()


campaign_cost = 200
cost_per_conversion = campaign_cost / buy_counts


cost_per_conversion_df = pd.DataFrame(cost_per_conversion).reset_index()
cost_per_conversion_df.columns = ['source_channel', 'cost_per_conversion']


def plot_cost_per_conversion(cost_per_conversion_df):
    plt.figure(figsize=(10, 6))
    sns.barplot(x='source_channel', y='cost_per_conversion', data=cost_per_conversion_df, palette='coolwarm')
    plt.title('Custo por conversão por canal de origem')
    plt.xlabel('Canal de origem')
    plt.ylabel('Custo por conversão (Euros)')
    return plt

#


with col7:
    st.header("Custo por conversão por canal de origem")
    st.pyplot(plot_cost_per_conversion(cost_per_conversion_df))



click_counts = df[df['event_type'] == 'click']['source_channel'].value_counts()


cost_per_click = campaign_cost / click_counts


cost_per_click_df = pd.DataFrame(cost_per_click).reset_index()
cost_per_click_df.columns = ['source_channel', 'cost_per_click']

def plot_cost_per_click(cost_per_click_df):
    plt.figure(figsize=(10, 6))
    sns.barplot(x='source_channel', y='cost_per_click', data=cost_per_click_df, palette='coolwarm')
    plt.title('Custo por clique por canal de origem')
    plt.xlabel('Canal de origem')
    plt.ylabel('Custo por clique (Euros)')
    return plt

with col8:  
    st.header("Custo por clique por canal de origem")
    st.pyplot(plot_cost_per_click(cost_per_click_df))
