import streamlit as st
from datetime import datetime

# Fonction principale de l'application Streamlit
def yansmorning():
    st.subheader('Yans Morning - Système de pointage V1.0.0', divider='rainbow')
    now = datetime.now()
    today_date = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M:%S")
    st.write(f"**Date du jour :** {today_date} **Il est :** {current_time}")
    st.info('Les réponses seront envoyées au bureau de Enclo sur Telegram.', icon="ℹ️")
    
    # Vérifier si le bouton a déjà été cliqué
    if 'button_clicked' not in st.session_state:
        st.session_state.button_clicked = False
    
    if not st.session_state.button_clicked:
        reponse = st.radio("T'es cuck ?", ("Oui", "Non"))
        if st.button("Valider"):
            st.session_state.button_clicked = True
            if reponse == "Oui":
                st.write("Sale cuck 🦆.")
                st.success(f'Pointage validé à {current_time} !', icon="✅")
                # Appeler la fonction pour envoyer un message Telegram ici
            else:
                st.write("OK j'fais un café ☕️")
                st.success(f'Pointage validé à {current_time} !', icon="✅")
                # Appeler la fonction pour envoyer un message Telegram ici
    else:
        st.write("Vous avez déjà pointé aujourd'hui.")

# Exécution de l'application Streamlit
if __name__ == "__main__":
    yansmorning()
