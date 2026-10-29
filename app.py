import streamlit as st

st.set_page_config(
    page_title="Conversor de Temperatura",
    page_icon="🌡️",
    layout="centered"
)

st.title("🌡️ Conversor de Temperatura")
st.write("Aplicación interactiva para convertir valores entre distintas escalas térmicas.")

st.divider()

st.subheader("Calculadora de Temperatura")

# Entrada del valor numérico
temperatura = st.number_input("Ingresa la temperatura a convertir:", value=0.0, format="%.2f")

# Selección de unidades
origen = st.selectbox(
    "Convertir desde:",
    ["Celsius (°C)", "Fahrenheit (°F)", "Kelvin (K)"]
)

destino = st.selectbox(
    "Convertir hacia:",
    ["Celsius (°C)", "Fahrenheit (°F)", "Kelvin (K)"]
)

if st.button("Convertir"):
    # Conversión
    if origen == destino:
        resultado = temperatura
    elif origen == "Celsius (°C)":
        if destino == "Fahrenheit (°F)":
            resultado = (temperatura * 9/5) + 32
        elif destino == "Kelvin (K)":
            resultado = temperatura + 273.15
    elif origen == "Fahrenheit (°F)":
        if destino == "Celsius (°C)":
            resultado = (temperatura - 32) * 5/9
        elif destino == "Kelvin (K)":
            resultado = (temperatura - 32) * 5/9 + 273.15
    elif origen == "Kelvin (K)":
        if destino == "Celsius (°C)":
            resultado = temperatura - 273.15
        elif destino == "Fahrenheit (°F)":
            resultado = (temperatura - 273.15) * 9/5 + 32

    # Mostrar resultado
    st.metric("Resultado", f"{resultado:.2f}")
    st.success(f"**{temperatura}** de *{origen}* equivalen a **{resultado:.2f}** en *{destino}*.")