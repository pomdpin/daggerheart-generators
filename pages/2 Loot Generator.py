"""
1 - importer le tableau de données
2 - séparer en fonction du types d'objets (?)
3 - demander le type d'objet voulu (choix multiples possibles ?)
4 - demander le niveau des objets (choix multiples possibles ?)
5 - demander le nombre d'objet voulu
6 - filtrer selon le type et le niveau d'objet
7 - random sample depuis le tableau
8 - si choix "Gold", calculer un nombre d'or à donner
9 - imprimer le resultat 
"""

import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="Loot Generator")

st.header("Loot Generator")

files = Path("files")
list_loot = pd.read_csv(files/"List_loot.csv", encoding='latin1', sep=";")

options_object = ["Item", "Consumable","Armor","Primary Weapon", "Secondary Weapon"]
options_tiers= ["Tier 1","Tier 2", "Tier 3", "Tier 4"]
selec_object = st.pills("What kind of objects do you want ? (multiple choices possible)", options_object, selection_mode = "multi")
selec_tiers = st.pills("What tier do you want ? (multiple choices possible)", options_tiers, selection_mode = "multi")
nbr_object = st.number_input("How many items do you want ?", min_value = 1, value = 1)

col1,col2 = st.columns(2)

with col2:
    if st.button("Open loot database"):
        st.dataframe(list_loot, use_container_width=True)

with col1:
    if st.button("Generate Loot") :
        loot_list=[]
        for i in range(nbr_object):
            if options_object == "All" and options_tiers == "All":
                loot = list_loot.sample(ignore_index=True)
                
            else:
                loot_by_type = list_loot[list_loot["Type"].str.contains('|'.join(selec_object))]
                loot_by_tier = loot_by_type[loot_by_type["Rarity"].str.contains('|'.join(selec_tiers))]
                loot = loot_by_tier.sample(ignore_index=True)
            
            loot = loot.to_dict()
            loot = {key: list(value.values())[0] for key, value in loot.items()}
            loot_list.append(loot)

        cols_per_row = 2
        cols = st.columns(cols_per_row)

    for i, loot in enumerate(loot_list):
        with cols[i % cols_per_row]:
            st.markdown(f"""
            <div style="border: 1px solid #ccc; padding: 10px; border-radius: 5px; margin-bottom: 20px;">
                <h5>{loot['Name']}</h5>
                {loot['Type']} | {loot['Rarity']}
                <br><i>{loot.get('Description', 'N/A')}</i>
            </div>
            """, unsafe_allow_html=True)

st.write("""
         ________________________________________
         **Copyright/Attribution: Daggerheart**
         \r*This project is unofficial fan content and is not approved or endorsed in any way by Critical Role.*
         \r*This product includes materials from the **Daggerheart System Reference Document 1.0**, **© Critical Role, LLC.** under the terms of the **Darrington Press Community Gaming (DPCGL) License**. More information can be found at https://www.daggerheart.com. There are no previous modifications by others.*
         \r*All Rights Reserved. Sous licence **Black Book Editions**, tous droits réservés.*""")