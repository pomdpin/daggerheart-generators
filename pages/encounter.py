"""
DAGGERHEART - ENCOUNTER GENERATOR
1 - Import the file
2 - Ask for the number of players
3 - Calculate battle points
4 - Ask for the party's tier
5 - Option to adjust tier (affects BP)
6 - Choose an environment
7 - Option to increase damage by 2d4 (-2BP)
"""

import streamlit as st
from pathlib import Path
import pandas as pd
import random

files = Path("files")
adversary_list = pd.read_csv(files/"list_adversaries.csv", sep=";")

option_tier = ["Lower the Tier (+1BP)", "Keep the same tier", "Increase the Tier (-2BP)"]
option_damage = ["No", "Yes (-2BP)"]
option_envt = ["Arctic", "Cave", "Coast", "Desert", "Dungeons", "Forest", "Grassland", "Mountain", "Ruins", "Sea", "Swamp", "Urban"]

st.title("Daggerheart")
st.header("Encounter Generator")

col1, col2 = st.columns(2)

with col1:
    nbr_player = st.number_input("How many players in your party?", value=1, min_value=1)
    tier = st.pills("Do you want to change the adversaries' Tier?", option_tier, default="Keep the same tier")
with col2:
    PC_tier = st.number_input("Which tier is your party?", value=1, min_value=1)
    damage = st.pills("Do you want to increase the adversaries' damage by 2d4?", option_damage, default="No")
terrains = st.pills("What kind of environmental terrain do you want?", option_envt, default="Urban")

battlepoints = 3 * nbr_player + 2

if "Lower" in tier:
    battlepoints += 1
    PC_tier -= 1
elif "Increase" in tier:
    battlepoints -= 2
    PC_tier += 1
if "Yes" in damage:
    battlepoints -= 2

st.subheader(f"You have {battlepoints} Battle Points")

adversary_type = {
    "Social": 1,
    "Support": 1,
    "Minion": 1,
    "Horde": 2,
    "Skulk": 2,
    "Range": 2,
    "Standard": 2,
    "Leader": 3,
    "Bruiser": 4,
    "Solo": 5
}

# Define adversary groups for logic (Minion/Leader))
adversary_groups = {
    "Minion": ["Leader"],
    "Leader": ["Minion"]
}

remaining_bp = battlepoints
encounter = []
max_leaders = 1
max_solos = 3
type_counts = {"Leader": 0, "Solo": 0}

if st.button("Generate Encounter"):
    while remaining_bp > 0:
        # Filter by tier, terrain, and affordable types
        affordable_types = [adv_type for adv_type, cost in adversary_type.items() if cost <= remaining_bp]
        filtered_list = adversary_list[
            (adversary_list["Tier"] == PC_tier) &
            (adversary_list["Terrain"].str.contains(terrains, na=False)) &
            (adversary_list["Type"].isin(affordable_types))
        ]
        
        if filtered_list.empty:
            st.warning("No adversaries match the current filters. Try adjusting your criteria.")
            break

         # Sample a random adversary
        adversary = filtered_list.sample(ignore_index=True).iloc[0].to_dict()
        adversary_cost = adversary_type[adversary["Type"]]
        adversary_type_name = adversary["Type"]

        # Skip if the type is Leader or Solo and the limit is reached
        if adversary_type_name in type_counts:
            if type_counts[adversary_type_name] >= (max_leaders if adversary_type_name == "Leader" else max_solos):
                continue

        # Check if the adversary belongs to a group (Minion/Leader or Pirate)
        if adversary["Type"] in adversary_groups:
            required_types = adversary_groups[adversary["Type"]]
            required_filtered_list = adversary_list[
                (adversary_list["Tier"] == PC_tier) &
                (adversary_list["Terrain"].str.contains(terrains, na=False)) &
                (adversary_list["Type"].isin(required_types)) &
                (adversary_list["Type"].isin(affordable_types))
            ]

            if not required_filtered_list.empty:
                # Sample a required adversary (e.g., Leader for Minions)
                required_adversary = required_filtered_list.sample(ignore_index=True).iloc[0].to_dict()
                required_cost = adversary_type[required_adversary["Type"]]
                required_type_name = required_adversary["Type"]

                # Check if we can afford both
                if remaining_bp - (adversary_cost + required_cost) >= 0:
                    encounter.append(adversary)
                    encounter.append(required_adversary)
                    remaining_bp -= (adversary_cost + required_cost)
                    
                    # Update counts for both types
                    if adversary_type_name in type_counts:
                        type_counts[adversary_type_name] += 1
                    if required_type_name in type_counts:
                        type_counts[required_type_name] += 1
                    continue

                # If we can't afford the group, skip this adversary
                else:
                    continue

            # If no required adversary is available, skip this adversary
            else:
                continue

        # If no group logic applies, or we can't afford the group, proceed normally
        if remaining_bp - adversary_cost >= 0:
            encounter.append(adversary)
            remaining_bp -= adversary_cost

             # Update counts for the type
            if adversary_type_name in type_counts:
                type_counts[adversary_type_name] += 1

        solo_count = sum(1 for adv in encounter if adv["Type"] == "Solo")
        if solo_count >= 2:
            remaining_bp -= 2
            

# Display the encounter as cards
cols_per_row = 2
cols = st.columns(cols_per_row)

for i, adversary in enumerate(encounter):
    with cols[i % cols_per_row]:
        st.markdown(f"""
        <div style="height: 300px; border: 1px solid #ccc; padding: 10px; border-radius: 5px; margin-bottom: 20px;">
            <h5>{adversary['Name']}</h5>
            Tier {adversary['Tier']} | {adversary['Type']}
            <br><i>{adversary.get('Description', 'N/A')}</i>
        </div>
        """, unsafe_allow_html=True)

st.write("""
         ________________________________________
         **Copyright/Attribution: Daggerheart**
         \r*This project is unofficial fan content and is not approved or endorsed in any way by Critical Role.*
         \r*This product includes materials from the **Daggerheart System Reference Document 1.0**, **© Critical Role, LLC.** under the terms of the **Darrington Press Community Gaming (DPCGL) License**. More information can be found at https://www.daggerheart.com. There are no previous modifications by others.*
         \r*All Rights Reserved. Sous licence **Black Book Editions**, tous droits réservés.*""")