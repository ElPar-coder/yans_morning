import streamlit as st
from datetime import datetime, timedelta

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
                # Enregistrement du pointage après validation
                record_user_point()
            else:
                st.write("OK j'fais un café ☕️")
                st.success(f'Pointage validé à {current_time} !', icon="✅")
                # Enregistrement du pointage après validation
                record_user_point()
    else:
        st.write("Désolé, vous avez déjà pointé aujourd'hui.")

# Exécution de l'application Streamlit
if __name__ == "__main__":
    yansmorning()
