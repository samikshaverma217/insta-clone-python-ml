import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="InstaClone ML", layout="wide")
st.markdown("<h1 style='text-align:center'>📸 InstaClone + ML</h1>", unsafe_allow_html=True)

# --- Top Tabs ---
tab1, tab2 = st.tabs(["📸 Feed / Photos", "🎬 Reels / Videos"])

with tab1:
    st.subheader("✨ ML Recommended For You")
    st.write("**travel_diaries** - Travel - ML Score: 95% Match")
    st.image("https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=600", width=400)
    st.write("❤️ 1250 likes | Mountains calling!")
    st.write("---")
    st.write("**foodie_girl** - Food - ML Score: 92% Match")
    st.image("https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=600", width=400)
    st.write("❤️ 890 likes | Best Pizza Ever!")

with tab2:
    st.subheader("🎬 Reels - Scroll karke dekho")
    st.write("**@travel_diaries** - Beach Reels 🏖️")
    st.video("https://storage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4")
    st.write("❤️ 5.2K | 💬 340 comments")
    st.write("---")
    st.write("**@fit_life** - Gym Reels 💪")
    st.video("https://storage.googleapis.com/gtv-videos-bucket/sample/ForBiggerEscapes.mp4")
    st.write("❤️ 8.1K | 💬 512 comments")

# --- ML Parts Neeche ---
st.subheader("🤖 ML: Spam Comment Detector")
comment = st.text_input("Comment likho, jaise 'free followers link'")
if comment:
    spam_words = ["free", "followers", "link", "click", "win", "money", "http"]
    if any(w in comment.lower() for w in spam_words):
        st.error("🚨 ML Result: SPAM COMMENT")
    else:
        st.success("✅ ML Result: SAFE COMMENT")

st.subheader("🏷️ ML: Hashtag Suggester")
cat2 = st.selectbox("Photo kis cheez ki hai?", ["Travel", "Food", "Fitness", "Tech", "Fashion"])
if st.button("Hashtag Generate Karo"):
    st.info(f"#{cat2.lower()} #viral #trending #explorepage #instagood")
