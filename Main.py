import streamlit as st

st.set_page_config(
    page_title="Daggerheart Generators"
)

st.write("# Welcome to Daggerheart Generator")

st.html(
    """
    Daggerheart Generator is a fan-made WebApp specifically created to help GMs prepare their Daggerheart adventure.
    <p>
    <p>Create brand new NPCs with ancestry-based descriptions and unique traits with our NPC Generator !
    <br>Or generate a bunch of items for your party to loot from the chests of this dungeon they're exploring with our Loot Generator !
    <br>And of course, no treasure chest would be complete without some adversaries to fight against, with our Encounter Generator !

   <p>
   <p>All three generators are SRD-compliant and do not contain any official Daggerheart out content outside of the SRD. The Loot Generator contains fan-converted and homebrewed items.
   <br>These generators are completely free of use and do not require any account.
   <p>All content  are available for free on <a href = "https://github.com/pomdpin/daggerheart-generators" target="_blank">GitHub</a>, including the database for loots and adversaries.
   <br>If you want, you can leave a tip to the creator at : <a href="https://ko-fi.com/yoannart91940" target="_blank">https://ko-fi.com/yoannart91940</a>
   <br>Need an illustration for your beloved PC, your BBEG or a that scene you have in mind ? You can order an art commission at : <a href="https://artistree.io/yoannart" target="_blank">https://artistree.io/yoannart</a>
   <p>
   <br>________________________________________
    <br><b>**Copyright/Attribution: Daggerheart**</b>
         <br>*This project is unofficial fan content and is not approved or endorsed in any way by Critical Role.*
         <br>*This product includes materials from the **Daggerheart System Reference Document 1.0**, **© Critical Role, LLC.** under the terms of the **Darrington Press Community Gaming (DPCGL) License**. More information can be found at https://www.daggerheart.com. There are no previous modifications by others.*
         <br>*All Rights Reserved. Sous licence **Black Book Editions**, tous droits réservés.*
    
"""
)