
import streamlit as st
import random

# ✅ Parola segreta (accetta "cromo vanadio" o "cromovanadio")
st.set_page_config(page_title="Magic 8Ball Marketers", page_icon="🎱")

st.markdown("<h1 style='text-align: center;'>🎱 L'oracolo di Marketers</h1>", unsafe_allow_html=True)

# --- FILASTROCCA ORACOLARE ---
st.markdown(
    "🔐 Parla l’Oracolo:\n\n"
    "Parla l’Oracolo, la voce è chiara,  \n"
    "ma apre la porta solo a chi impara.  \n"
    "Dario parlava con tono deciso,  \n"
    "di punte speciali e metallo preciso.  \n"
    "Non era acciaio, non era titanio,  \n"
    "la punta era in:"
)

# 🔒 Campo password
pwd = st.text_input("Inserisci la parola chiave:", type="password")

# Normalizza la password: minuscolo + niente spazi
risposta = pwd.lower().strip().replace(" ", "")

if risposta == "cromovanadio":
    st.success("🔮 La sfera ha riconosciuto la tua energia, viandante del funnel.")
    st.write("🧘‍♀️ Il tuo tasso di conversione interiore ha già formulato la domanda.")

    if st.button("Chiedi alla Sfera"):
        risposte = [
            "L’Oracolo vede 0 vendite.",
            "Quel template figo ha già ucciso 14 conversioni.",
            "Il karma del CPM è instabile oggi.",
            "Quel PDF gratuito non lo vuole nessuno.",
            "Chiedi a Dario.",
            "Quel funnel ha più buchi della tua nicchia.",
            "Hai creato un’offerta. Ma nessuno l’ha chiesta.",
            "Il tuo tone of voice è un voice over di noia.",
            "Sei troppo crazy per Cresi.",
            "Nessuno cliccherà quel pulsante. Neanche tua madre.",
            "Il CPM non è il problema. Sei tu.",
            "L’unica cosa che hai convertito è tempo in ansia.",
            "L’energia del retargeting è disturbata.",
            "L'Oracolo è favorevole alla revisione del copy. Non alla pubblicazione.",
            "Non scalare oggi. I venti del funnel sono contrari.",
            "Ogni volta che non invii la tua newsletter una fatina muore.",
        ]
        st.markdown(f"🧠 **La sfera risponde:**<br><br>👉 _{random.choice(risposte)}_", unsafe_allow_html=True)

elif pwd:
    st.error("🌀 L’Oracolo non risponde a tentativi goffi.")
