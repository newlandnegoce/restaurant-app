import streamlit as st
import pandas as pd

# Configuration de la page
st.set_page_config(page_title="Gestion du Restaurant", layout="wide")

st.title("🍽️ Gestion du Restaurant - Démo")

# Navigation
st.sidebar.header("Navigation")
section = st.sidebar.radio("Choisissez une section :", ["Tables", "Commandes", "Stocks", "Employés"])

# Données initiales
tables_data = pd.DataFrame([
    {"Table_ID": 1, "Status": "Disponible", "Capacity": 4},
    {"Table_ID": 2, "Status": "Occupée", "Capacity": 2},
    {"Table_ID": 3, "Status": "Disponible", "Capacity": 6}
])

commandes_data = pd.DataFrame([
    {"Order_ID": 101, "Table_ID": 2, "Items": "Pizza, Soda", "Status": "En cours", "Total_Price": 15.50},
    {"Order_ID": 102, "Table_ID": 3, "Items": "Salade, Eau", "Status": "Servi", "Total_Price": 10.00}
])

stocks_data = pd.DataFrame([
    {"Item_ID": 1, "Item_Name": "Tomates", "Quantity": 50, "Unit_Price": 0.5},
    {"Item_ID": 2, "Item_Name": "Pâtes", "Quantity": 20, "Unit_Price": 1.5},
    {"Item_ID": 3, "Item_Name": "Fromage", "Quantity": 30, "Unit_Price": 2.0}
])

employes_data = pd.DataFrame([
    {"Employee_ID": 1, "Name": "Alice", "Role": "Serveuse", "Shift": "Matin"},
    {"Employee_ID": 2, "Name": "Bob", "Role": "Cuisinier", "Shift": "Soir"},
    {"Employee_ID": 3, "Name": "Charlie", "Role": "Gérant", "Shift": "Journée"}
])

# Affichage des sections
if section == "Tables":
    st.header("🪑 Gestion des Tables")
    st.dataframe(tables_data)

elif section == "Commandes":
    st.header("📋 Commandes en cours")
    st.dataframe(commandes_data)

elif section == "Stocks":
    st.header("📦 Gestion des Stocks")
    st.dataframe(stocks_data)

elif section == "Employés":
    st.header("👨‍🍳 Gestion des Employés")
    st.dataframe(employes_data)
