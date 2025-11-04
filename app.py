import streamlit as st
import pandas as pd
import plotly_express as px


# import dataset to dataframe
df_exopl = pd.read_csv('Treated_exoplanets_dataset.csv')
df_exopl = df_exopl[df_exopl['pl_rade'] < 25]
df_exopl.reset_index(inplace=True)

# criando o cabeçalho e outras informações do aplicativo
st.title('Tripleten')
st.title('Sprint 5 - Projeto')
'FSG'
st.header('Apresentação do dataset de exoplanetas')
'Anos de exploração espacial, em busca de planetas semelhantes ao que habitamos, geraram montanhas de informação sobre os Exoplanetas que encontramos espaço a fora. Empresas como a NASA disponibilizam esses dados de forma pública, e podem ser acessados pelo link:'
'https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=PS'
''
'Esse pequeno dashboard busca mostrar algumas relações interessantes que encontrei sobre os dados apresentados'
'Seu código fonte pode ser encontrado no github:'
'https://github.com/fernandogoudard-pixel/Tripleten_sprint_5'
''
st.header('Graficos:')
'Esse dashboard é separado em dois tipos de gráficos, um histograma e um grafico de dispersão'
'O Histograma mostra a relação de tamanho dos planetas descobertos, com opção para separa os dados em ano de descoberta e telescópio usado para a descoberta'
'O grafico de dispersão mostra a relação entre o tamanho dos planetas e seu período orbital'
'É possível alternar entre eles com a seguinte caixa:'

# lógica operacional dos botões:
graph_hist = st.checkbox('Mostrar Histograma')
if graph_hist:
    title ='Numero de exoplanetas descobertos'
    labels = {
            'pl_rade':'Raio do exoplaneta (Raios Terra)',
            'disc_year':'Ano de descoberta',
            'disc_telescope':'Telescópio'
        }
    # mostrar histograma
    # botões para seleção entre simples, por ano, e por telescópio
    simples = st.button('Histograma Simples')
    tele = st.button('Histograma por telescópio')
    ano = st.button('Histograma por ano')
    if tele:
        fig = px.histogram(df_exopl, 
                            x='pl_rade', 
                            color='disc_year',
                            title=title,
                            labels=labels,)
        fig.update_layout(yaxis_title = 'Exoplanetas')
        st.plotly_chart(fig,  width='stretch')
    if ano:
        fig = px.histogram(df_exopl, 
                            x='pl_rade', 
                            color='disc_year',
                            title=title,
                            labels=labels,)
        fig.update_layout(yaxis_title = 'Exoplanetas')
        st.plotly_chart(fig,  width='stretch')
    if simples:
        fig = px.histogram(df_exopl, 
                            x='pl_rade',
                            title=title,
                            labels=labels,)
        fig.update_layout(yaxis_title = 'Exoplanetas')
        st.plotly_chart(fig,  width='stretch')
        
else:
    # mostrar grafico de dispersão
    title ='Exoplanetas: Raio por periodo orbital'
    labels = {
        'pl_rade':'Raio do exoplaneta (Raios Terra)',
        'pl_orbper':'Período orbital (Dias)'
    }
    # sample para limitar a quantidade de itens no gráfico
    # durante testes tentar exibir mais de 1000 pontos no gráfico fez com que os pontos
    # ficassem invisiveis no streamlit
    fig = px.scatter(df_exopl[(df_exopl['pl_orbper'] < 800)].sample(1000, random_state = 15), 
                    x='pl_rade',
                    y='pl_orbper',
                    labels = labels,
                    title = title,)
    st.plotly_chart(fig, width='stretch')
