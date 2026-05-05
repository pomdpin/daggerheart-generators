import streamlit as st

st.set_page_config(
    page_title="Daggerheart Generators"
)

st.write("# Welcome to Daggerheart Generator")

st.html(
    """
    Daggerheart Generator is a fan-made WebApp specifically created to help GMs prepare their Daggerheart adventure.
    
    <p>Create brand new NPCs with ancestry-based descriptions and unique traits with our NPC Generator !
    <br>Or generate a bunch of items for your party to loot from the chests of this dungeon they're exploring with our Loot Generator !
    <br>And of course, no treasure chest would be complete without some adversaries to fight against, with our Encounter Generator !

   <p>
   <p>All three generators are SRD-compliant and do not contain any official Daggerheart out content outside of the SRD. 
   <br>The Loot Generator contains fan-converted and homebrewed items.
   <br>All content  are available for free on GitHub, including the database for loots and adversaries.
   <ul>https://github.com/pomdpin/daggerheart-generators</ul>

   <p>These generators are completely free of use and do not require any account.
   <br>If you want, you can leave a tip to the creator at : https://ko-fi.com/yoannart91940
   <br>Need an illustration for your beloved PC, your BBEG or a that scene you have in mind ? You can order an art commission at : https://artistree.io/yoannart
   <p>
   <br>________________________________________
    <br><b>**Copyright/Attribution: Daggerheart**</b>
         <br>*This project is unofficial fan content and is not approved or endorsed in any way by Critical Role.*
         <br>*This product includes materials from the **Daggerheart System Reference Document 1.0**, **© Critical Role, LLC.** under the terms of the **Darrington Press Community Gaming (DPCGL) License**. More information can be found at https://www.daggerheart.com. There are no previous modifications by others.*
         <br>*All Rights Reserved. Sous licence **Black Book Editions**, tous droits réservés.*
    
"""
)