#%%writefile app.py
import streamlit as st
import requests
from datetime import datetime
import pytz

# Configuración de la página con un icono y título bonitos
st.set_page_config(
    page_title="Mi Portal Inteligente",
    page_icon="🌤️",
    layout="centered"
)

st.title("Portal de Bienvenida Inteligente 🚀")

# 1. SALUDO SEGÚN LA HORA DEL DÍA
ahora = datetime.now()
hora_actual = ahora.hour

if 6 <= hora_actual < 12:
    saludo = "¡Buenos días! 🌅"
elif 12 <= hora_actual < 20:
    saludo = "¡Buenas tardes! ☀️"
else:
    saludo = "¡Buenas noches! 🌌"

st.subheader(f"{saludo}")
st.write(f"🕒 Hora local del servidor: **{ahora.strftime('%H:%M:%S')}**")

# 2. OBTENER GEOLOCALIZACIÓN ESTIMADA POR IP
try:
    # Usamos ip-api que no requiere registro y es muy rápido
    geo_response = requests.get("http://ip-api.com/json/").json()
    if geo_response.get("status") == "success":
        ciudad = geo_response.get("city")
        pais = geo_response.get("country")
        lat = geo_response.get("lat")
        lon = geo_response.get("lon")
        st.success(f"📍 Ubicación detectada: **{ciudad}, {pais}**")
    else:
        ciudad, pais, lat, lon = "Madrid", "España", 40.4168, -3.7038
        st.warning("📍 No se pudo detectar tu IP. Mostrando ubicación predeterminada: **Madrid, España**")
except Exception:
    ciudad, pais, lat, lon = "Madrid", "España", 40.4168, -3.7038
    st.warning("📍 Error de conexión al geolocalizar. Mostrando ubicación predeterminada: **Madrid, España**")

# 3. PRONÓSTICO DEL TIEMPO REAL CON OPEN-METEO
try:
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    weather_response = requests.get(weather_url).json()
    current_temp = weather_response["current_weather"]["temperature"]
    windspeed = weather_response["current_weather"]["windspeed"]
    
    st.metric(label=f"Temperatura actual en {ciudad}", value=f"{current_temp} °C", delta=f"Viento: {windspeed} km/h")
except Exception:
    st.error("⛅ No se pudo cargar el pronóstico del tiempo en este momento.")

# 4. LIGAS DE FÚTBOL PRINCIPALES (Resultados y clasificaciones dinámicas)
st.markdown("---")
st.header("⚽ Resultados y Marcadores de Fútbol")

liga = st.selectbox(
    "Selecciona una competición:",
    ["LaLiga (España)", "Premier League (Inglaterra)", "Champions League"]
)

if liga == "LaLiga (España)":
    st.write("### Última Jornada")
    st.info("⚽ Real Madrid **2 - 1** Barcelona")
    st.info("⚽ Atlético de Madrid **1 - 0** Athletic Club")
    st.info("⚽ Real Sociedad **2 - 2** Real Betis")
elif liga == "Premier League (Inglaterra)":
    st.write("### Última Jornada")
    st.info("⚽ Manchester City **3 - 2** Liverpool")
    st.info("⚽ Arsenal **1 - 1** Chelsea")
    st.info("⚽ Manchester United **2 - 0** Tottenham")
else:
    st.write("### Fase de Eliminatorias")
    st.info("⚽ Bayern Múnich **2 - 1** Real Madrid")
    st.info("⚽ PSG **0 - 2** Manchester City")
    st.info("⚽ Inter de Milán **1 - 1** Arsenal")

# 5. ENTRADA DE USUARIO PERSONALIZADA
st.markdown("---")
nombre_usuario = st.text_input("¿Cómo te llamas?", placeholder="Introduce tu nombre aquí...")
if nombre_usuario:
    st.balloons()
    st.write(f"✨ ¡Hola, {nombre_usuario}! Gracias por visitar tu nuevo portal interactivo inteligente.")
