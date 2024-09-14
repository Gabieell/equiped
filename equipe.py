import pandas as pd
import streamlit as st

# Função para encontrar os valores pagos dos pacientes
def encontrar_valores_pagamentos(agenda_df, pagamento_df):
    # Fazer a correspondência entre as duas planilhas usando o número de atendimento
    pagamentos_realizados = pd.merge(agenda_df, pagamento_df[['Atendimento', 'Vl liberado']], on='Atendimento', how='inner')
    
    # Selecionar as colunas desejadas
    resultado_df = pagamentos_realizados[['Data', 'Atendimento', 'Paciente', 'Categoria', 'Vl liberado']]
    
    return resultado_df

# Configuração da interface Streamlit
st.title("Sistema de Conferência de Pagamentos por Paciente")
st.write("Desenvolvido por Gabrielle Carvalho")

# Carregar as planilhas
uploaded_file_agenda = st.file_uploader("Escolha a planilha de agenda", type="xlsx")
uploaded_file_pagamento = st.file_uploader("Escolha a planilha de pagamento", type="xlsx")

if uploaded_file_agenda and uploaded_file_pagamento:
    # Carregar as planilhas
    agenda_df = pd.read_excel(uploaded_file_agenda)
    pagamento_df = pd.read_excel(uploaded_file_pagamento)

    # Encontrar os valores pagos
    resultado_df = encontrar_valores_pagamentos(agenda_df, pagamento_df)

    # Mostrar os resultados no aplicativo
    st.write("Valores pagos pelos pacientes atendidos:")
    st.dataframe(resultado_df)

    # Permitir download da planilha de resultados
    resultado_file = "valores_pagamentos.xlsx"
    resultado_df.to_excel(resultado_file, index=False)
    st.download_button(label="Baixar planilha de valores pagos", data=open(resultado_file, 'rb').read(), file_name=resultado_file)

else:
    st.write("Por favor, faça o upload das planilhas de agenda e pagamento.")
