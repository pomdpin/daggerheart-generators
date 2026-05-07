# app.py
import streamlit as st
import random
import json
from pathlib import Path
import namemaker

# Load your data
app_folder = Path("files")

# Streamlit UI
on = st.toggle("Toggle to switch to English")

if on:
    st.set_page_config(page_title="NPCs Generator")
    st.header("NPCs Generator")
    nombre_pnj = st.number_input("How many NPCs ?", min_value=1, value=1)
else :
    st.set_page_config(page_title="Générateur de PNJs")
    st.header("Générateur de PNJs")
    nombre_pnj = st.number_input("Combien de PNJs ?", min_value=1, value=1)

# Load data based on language
file_name = "heritage_en.json" if on else "heritage_fr.json"
file_descr = "description_en.json" if on else "description_fr.json"
age_terme = "years old" if on else "ans"

with open(app_folder/"prenoms_noms.json", encoding="utf-8") as names:
    names = json.load(names)
with open(app_folder/file_name, encoding="utf-8") as heritage:
    heritages = json.load(heritage)
with open(app_folder/file_descr, encoding="utf-8") as description:
    descriptions = json.load(description)

option_ancestry = list(heritages["Ascendance"].keys())
if on :
    ascendance = st.pills("Choose one or several ancestries to generate from:", option_ancestry)
    create = st.button("Generate")
else:
    ascendance = st.pills("Choisissez une ou plusieurs ascendances à partir desquelles générer:", option_ancestry, selection_mode="multi")
    create = st.button("Générer")

if not ascendance:
    ascendance = option_ancestry
# Ensure `ascendance` is always a list
elif isinstance(ascendance, str):
    ascendance = [ascendance]


if create:
    set_prenoms = namemaker.make_name_set(names["Prénoms"], order=3, name_len_func=len, clean_up=True)
    set_noms = namemaker.make_name_set(names["Noms de famille"], order=3, name_len_func=len, clean_up=True)

    pnjs = []
    for _ in range(nombre_pnj):
        tier = random.randint(1,4)
        name = set_prenoms.make_name()
        surname = set_noms.make_name()
        descr_general = []
        descr_asc = []
        classe = random.choice(heritages["Classe"])
        ascendance_random = random.choice(ascendance)
        age = random.randint(heritages["Ascendance"][ascendance_random]["age_min"], heritages["Ascendance"][ascendance_random]["age_max"])
        taille = random.randint(heritages["Ascendance"][ascendance_random]["taille_min"], heritages["Ascendance"][ascendance_random]["taille_max"])
        community = random.choice(list(heritages["Communauté"].keys()))
        personnality = random.choice(heritages["Communauté"][community])

        for categorie in descriptions["General"]:
            descr_general.append(random.choice(descriptions["General"][categorie]))

        for categorie in descriptions["Ascendance"][ascendance_random]:
            valeur = random.choice(descriptions["Ascendance"][ascendance_random][categorie])
            descr_asc.append(valeur)
            if categorie == "Style" and ("chauve" in valeur or "bald" in valeur):
                continue

        phrase_descr_asc = " ".join(descr_asc)

        if on:
            pnj_name = f"""{name} {surname} - Tier {tier} 
            \r {community} {classe}"""
            pnj_desc = f"""**Description**: {age} {age_terme} and around {round(taille/5)*5}cm tall {ascendance_random} with {descr_general[0]} eyes. {phrase_descr_asc.capitalize()}. Wearing {descr_general[1]} {descr_general[2]}.
            \r**Quirk**: {descr_general[3]}"""
            #\r**Occupation**: 
            #\r**Home**:"""
        else :
            pnj_name = f"""{name} {surname} - Tier {tier}
            \r {classe} de la {community}"""
            pnj_desc = f"""**Description** : {ascendance_random} de {age}{age_terme} aux yeux {descr_general[0]} et mesurant environ {round(taille/5)*5}cm. {phrase_descr_asc.capitalize()}. Vêtu {descr_general[1]} {descr_general[2]}.
            \r**Personnalité** : {descr_general[3]}"""
            #\r**Métier** : 
            #\r**Ville** : """

        pnjs.append((pnj_name, pnj_desc))

    cols_per_row = 2
    cols = st.columns(cols_per_row)
    for i, (pnj_name, pnj_desc) in enumerate(pnjs):
        with cols[i % cols_per_row]:
            st.markdown(f"""
        <div style="border: 1px solid #ccc; padding: 10px; border-radius: 5px; margin-bottom: 20px;">
            <h5>{pnj_name}</h5>
            {pnj_desc}</div>""", unsafe_allow_html=True)

st.write("""
         ________________________________________
         **Copyright/Attribution: Daggerheart**
         \r*This project is unofficial fan content and is not approved or endorsed in any way by Critical Role.*
         \r*This product includes materials from the **Daggerheart System Reference Document 1.0**, **© Critical Role, LLC.** under the terms of the **Darrington Press Community Gaming (DPCGL) License**. More information can be found at https://www.daggerheart.com. There are no previous modifications by others.*
         \r*All Rights Reserved. Sous licence **Black Book Editions**, tous droits réservés.*""")