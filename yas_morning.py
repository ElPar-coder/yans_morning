import streamlit as st
import requests
from datetime import datetime, timedelta

# Configuration du bot Telegram
TELEGRAM_BOT_TOKEN = '7034880568:AAHHO-weYiLbhSF63OusOFoiB-eMDrTqosc'
TELEGRAM_CHAT_ID = '-1002242000827'

# Fonction pour envoyer un message à Telegram
def send_message_to_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    response = requests.post(url, data=data)
    return response.json()

# Fonction pour vérifier si l'utilisateur peut pointer aujourd'hui
def can_user_point_today():
    last_point_date = st.session_state.get('last_point_date')
    if last_point_date is None:
        return True  # Premier pointage de l'utilisateur

    today = datetime.now().date()
    return last_point_date < today

# Fonction pour enregistrer le pointage de l'utilisateur
def record_user_point():
    st.session_state.last_point_date = datetime.now().date()

# Fonction principale de l'application Streamlit
def yansmorning():
    st.subheader('Yans Morning - Système de pointage V1.0.0', divider='rainbow')
    now = datetime.now()
    today_date = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M:%S")
    st.write(f"**Date du jour :** {today_date} **Il est :** {current_time}")
    st.info('Les réponses seront envoyées au bureau de Enclo sur Telegram.', icon="ℹ️")
    
    # Affichage du bouton de pointage uniquement si l'utilisateur peut pointer aujourd'hui
    if can_user_point_today():
        reponse = st.radio("T'es cuck ?", ("Oui", "Non"))
        if st.button("Valider"):
            if reponse == "Oui":
                st.write("Sale cuck 🦆.")
                st.success(f'Pointage validé à {current_time} !', icon="✅")
                send_message_to_telegram(f"Il est cuck ce fdp aujourd'hui le {today_date} il a pointé à {current_time}.")
            else:
                st.write("OK j'fais un café ☕️")
                st.success(f'Pointage validé à {current_time} !', icon="✅")
                send_message_to_telegram(f"Miracle il n'est pas cuck aujourd'hui le {today_date} il a pointé à {current_time} go café.")
            
            # Enregistrement du pointage après validation
            record_user_point()
    else:
        st.write("T'as déjà pointé aujourd'hui.")

# Exécution de l'application Streamlit
if __name__ == "__main__":
    yansmorning()
