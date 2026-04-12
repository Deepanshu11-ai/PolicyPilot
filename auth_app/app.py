import streamlit as st
from auth import signup, login, logout

st.set_page_config(page_title="Auth System", layout="centered")

# Session state init
if "session" not in st.session_state:
    st.session_state.session = None


st.title("🔐 AI Insurance Auth")

menu = ["Login", "Signup"]
choice = st.sidebar.selectbox("Menu", menu)


# ---------------- SIGNUP ----------------
if choice == "Signup":
    st.subheader("Create Account")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Signup"):
        res = signup(email, password)

        if res.user:
            st.success("Account created! You can login now.")
        else:
            st.error("Signup failed")


# ---------------- LOGIN ----------------
if choice == "Login":
    st.subheader("Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        res = login(email, password)

        if res.session:
            st.session_state.session = res.session
            st.success("Logged in successfully")
        else:
            st.error("Invalid credentials")


# ---------------- DASHBOARD ----------------
if st.session_state.session:
    st.subheader("🎉 Welcome")

    user = st.session_state.session.user
    token = st.session_state.session.access_token

    st.write("User ID:", user.id)
    st.write("JWT Token:", token[:50] + "...")

    if st.button("Logout"):
        logout()
        st.session_state.session = None
        st.rerun()