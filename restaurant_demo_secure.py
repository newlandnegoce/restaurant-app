import streamlit as st
import pandas as pd

# Configuration de la page
st.set_page_config(page_title="Gestion du Restaurant - Sécurisé", layout="wide")

# Définition des utilisateurs et rôles
users = {
    "admin": {"password": "admin123", "role": "Admin"},
    "serveur": {"password": "serveur123", "role": "Serveur"},
    "cuisine": {"password": "cuisine123", "role": "Cuisine"}
}

# Page de connexion
st.sidebar.title("🔐 Connexion")
username = st.sidebar.text_input("Nom d'utilisateur")
password = st.sidebar.text_input("Mot de passe", type="password")
login_btn = st.sidebar.button("Se connecter")

if login_btn:
    if username in users and users[username]["password"] == password:
        st.session_state["logged_in"] = True
        st.session_state["username"] = username
        st.session_state["role"] = users[username]["role"]
        st.sidebar.success(f"Bienvenue, {username}! Rôle: {users[username]['role']}")
    else:
        st.sidebar.error("Identifiants incorrects")

# Vérifier si l'utilisateur est connecté
if "logged_in" in st.session_state and st.session_state["logged_in"]:
    role = st.session_state["role"]
    
    # Interface selon le rôle de l'utilisateur
    st.title(f"🍽️ Gestion du Restaurant - {role}")

    if role == "Admin":
        section = st.sidebar.radio("Navigation", ["Tables", "Commandes", "Stocks", "Employés"])
    elif role == "Serveur":
        section = st.sidebar.radio("Navigation", ["Tables", "Commandes"])
    elif role == "Cuisine":
        section = st.sidebar.radio("Navigation", ["Commandes"])

    # Données
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

    # Affichage selon la section choisie
    if section == "Tables":
        st.header("🪑 Gestion des Tables")
        st.dataframe(tables_data)
    
    elif section == "Commandes":
        st.header("📋 Commandes en cours")
        st.dataframe(commandes_data)
    
    elif section == "Stocks" and role == "Admin":
        st.header("📦 Gestion des Stocks")
        st.dataframe(stocks_data)
    
    elif section == "Employés" and role == "Admin":
        st.header("👨‍🍳 Gestion des Employés")
        st.dataframe(employes_data)

    # Bouton de déconnexion
    if st.sidebar.button("Se déconnecter"):
        st.session_state["logged_in"] = False
        st.rerun()

else:
    st.warning("Veuillez vous connecter pour accéder à l'application.")
