import streamlit as st 
import random
import string
import re

def check_password_strength(password):
    score = 0
    feedback = []
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password Should be at least 8 characters long.")
        
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
        
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")
        
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Incluide at least one special character (!@#$%^&*).")
        
    if score == 4:
        return "✅ Strong Password! Your Password is secure.", "greeen"
    elif score == 3:
        return "💀 Moderate Password - Add more security features.", "orange"
    else:
        return "❌ Weak Password - Improve using the suggestions above.", "red"

def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters # Inclued all letters (a-z -- A-Z)
    
    if use_digits:
        characters += string.digits # Adds number (0-9) if selected
    if use_special:
        characters += string.punctuation
        
    return ''.join(random.choice(characters) for _ in range(length))

st.set_page_config(page_title="Password Strength Meter", page_icon="🔐")

st.title("🔐 Password Strength Checker")
st.markdown("<p style='font-size:18px; color:gray;'>Check your password's strength and get security tipw!</p>", unsafe_allow_html=True)

password = st.text_input("🔑 Enter your password:", type="password")
if password:
    strength, color = check_password_strength(password)
    st.markdown(f"<p style='color:{color}; font-weight:bold;'>{strength}</p>", unsafe_allow_html=True)
if st.button("Check Password Strength"):
    check = check_password_strength(password)

st.markdown("---")
st.title("🔁 Password Generator ⚡")

length = st.slider("Select Password length", min_value=8, max_value=32, value=12)

use_digits = st.checkbox("Include Digits")

use_special = st.checkbox("Inclde Special Characters")

if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special)
    st.write(f"Genereated Password: `{password}`")

st.markdown("---")
st.subheader("Why Strong Password Matter?")
st.info("A strong password keeps your accounts secure. Use a mix of letters, numbers and symbols.")

st.markdown("---")
st.write("Build by [Muhammad Kamran](https://github.com/KamranYT)")