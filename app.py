import streamlit as st

def calculate_volumes(belag_hoehe, estrich_hoehe, daemmung_hoehe, hoehe, flaeche):
    estrich_volumen = flaeche * estrich_hoehe
    beschuettung_hoehe = hoehe - belag_hoehe - estrich_hoehe - daemmung_hoehe
    beschuettung_volumen = flaeche * beschuettung_hoehe

    return estrich_volumen, beschuettung_volumen

st.title("Volumenberechnung für Estrich und Beschüttung")

belag_hoehe = st.number_input("Bitte Belagshöhe eingeben:", value=0.0)
estrich_hoehe = st.number_input("Bitte Estrichhöhe eingeben:", value=0.0)
daemmung_hoehe = st.number_input("Bitte Dämmungshöhe eingeben:", value=0.0)
hoehe = st.number_input("Bitte Gesamthöhe eingeben:", value=0.0)
flaeche = st.number_input("Bitte Fläche eingeben:", value=0.0)

if st.button("Berechnen"):
    estrich_volumen, beschuettung_volumen = calculate_volumes(belag_hoehe, estrich_hoehe, daemmung_hoehe, hoehe, flaeche)

    st.write("Volumen Estrich: {:.2f} m^3".format(estrich_volumen))
    st.write("Volumen Beschüttung: {:.2f} m^3".format(beschuettung_volumen))
