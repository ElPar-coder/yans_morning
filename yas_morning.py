import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime
import requests

# Configuration du bot Telegram
TELEGRAM_BOT_TOKEN = '7034880568:AAHHO-weYiLbhSF63OusOFoiB-eMDrTqosc'
TELEGRAM_CHAT_ID = '-1002242000827'

def send_message_to_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": -1002242000827,
        "text": message
    }
    response = requests.post(url, data=data)
    return response.json()

def yansmorning():
    st.subheader('YansCuck - Systeme de pointage V1.0.0', divider='rainbow')
    now = datetime.now()
    today_date = now.strftime( "%Y-%m-%d" )
    current_time = now.strftime( "%H:%M:%S" )
    st.write( f"**Date du jour :** {today_date} **il est** {current_time}" )
    st.info( 'Les réponses seront envoyé au bureau de Enclo sur telegram.', icon="ℹ️" )
    reponse = st.radio("T'es cuck ?", ("Oui", "Non"))
    if st.button("Valider"):
        if reponse == "Oui":
            st.write("Sale cuck 🦆.")
            st.success( f'Pointage Validé à {current_time} ! ', icon="✅" )
            send_message_to_telegram( f"Il est cuck ce fdp aujourd'hui le {today_date} il a pointé à {current_time}." )
        else:
            st.write("OK jfait un café ☕️")
            st.success( f'Pointage Validé à {current_time} ! ', icon="✅" )
            send_message_to_telegram( f"Miracle il est pas cuck aujourd'hui le {today_date} il a pointé à {current_time} go café." )




yansmorning()
