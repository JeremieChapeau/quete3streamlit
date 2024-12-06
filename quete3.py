import streamlit as st

# Vérifier l'état d'authentification et la page courante dans le session_state
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "page" not in st.session_state:
    st.session_state.page = "Accueil"  # Par défaut, la page est "Accueil"

# Fonction d'authentification
def authenticate(username, password):
    """Fonction simple d'authentification."""
    return username == "WILDER" and password == "PONEY"

# Interface de login
def login():
    """Interface de login."""
    st.title("Connexion")
    st.write("Le nom d'utilisateur est **WILDER** et le mot de passe est **PONEY**.")
    username = st.text_input("Nom d'utilisateur")
    password = st.text_input("Mot de passe", type="password")
    if st.button("Se connecter"):
        if authenticate(username, password):
            st.session_state.authenticated = True
            st.session_state.page = "Accueil"  # Accueil après la connexion
            st.success("Connexion réussie !")  # Message de succès
        else:
            st.error("Identifiant ou mot de passe incorrect.")  # Message d'erreur

# Page d'accueil
def accueil_page():
    """Page d'accueil."""
    st.title("Bienvenue sur ma page !")
    st.image(
        "https://th.bing.com/th/id/OIP.mhFHg5q6XrLcD_DyKS7DlgAAAA?rs=1&pid=ImgDetMain",
        caption="Bienvenue sur ma page !"
    )

# Page avec les photos de poneys
def album_page():
    """Page principale avec les photos de poneys."""
    st.title("Album de Poneys")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://i.pinimg.com/736x/77/39/95/773995b212c3ef71664427c26c277405--happy-faces-shetland-ponies.jpg", caption="Bob")
    with col2:
        st.image("https://petpress.net/wp-content/uploads/2020/03/funny-horse.jpg", caption="Jean-mi")
    with col3:
        st.image("https://i.pinimg.com/736x/e9/a8/06/e9a806c1ca08db93425a1d93c7abd7d5.jpg", caption="Tony")

# Barre latérale de navigation
def navigation():
    """Barre latérale de navigation."""
    with st.sidebar:
        st.header("Navigation")
        if st.button("Accueil"):
            st.session_state.page = "Accueil"
        if st.button("Poney"):
            st.session_state.page = "Poneys"
        if st.button("Se déconnecter"):
            st.session_state.authenticated = False
            st.session_state.page = "Accueil"  # Retour à la page d'accueil après déconnexion

# Vérifier si l'utilisateur est authentifié
if st.session_state.authenticated:
    navigation()  # Afficher la barre de navigation
    if st.session_state.page == "Accueil":
        accueil_page()  # Afficher la page d'accueil
    elif st.session_state.page == "Poneys":
        album_page()  # Afficher l'album de poneys
else:
    login()  # Afficher l'interface de login si non authentifié

