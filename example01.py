import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar datos
df = pd.DataFrame({
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'Population': [8398748, 3990456, 2705994, 2320268, 1680992],
    'Area': [468.9, 468.7, 227.3, 637.5, 517.6]
})
df
# Configurar la página
st.title('Ciudades de EE. UU.')
st.sidebar.title('Configuración')

# Barra lateral para seleccionar la ciudad
selected_city = st.sidebar.selectbox('Selecciona una ciudad', df['City'])

# Filtrar el DataFrame según la ciudad seleccionada
selected_city_data = df[df['City'] == selected_city]

# Mostrar información de la ciudad seleccionada
st.header(f'Información para {selected_city}')
st.write(f'Población: {selected_city_data["Population"].values[0]:,}')
st.write(f'Área: {selected_city_data["Area"].values[0]:,.2f} sq miles')

# Gráfico de barras interactivo con Plotly Express
fig = px.bar(df, x='City', y='Population', title='Población de Ciudades de EE. UU.')
st.plotly_chart(fig)

