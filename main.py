                 import streamlit as st
st.set_page_config(page_title="InstaClone", layout="wide")

# ---------- 10 ALAG-ALAG ACCOUNTS - Sabke alag face ----------
USERS = {
    "sana_fashion": {"name": "Sana Khan", "gender": "girl", "pic": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=300", "bio": "Fashion 👗 | Delhi | Collab DM 💌", "followers": ["aarav_travel","priya_food","rohan_fit"], "following": ["aarav_travel","priya_food"], "audio": "🎵 Mood: Happy - Arijit Singh", "posts": [
        {"type":"photo","url":"https://images.unsplash.com/photo-1524504388940-b1c1722653e1?w=600","cap":"New Dress ✨ #fashion"},
        {"type":"photo","url":"https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?w=600","cap":"Shoot Day 📸 #fashion"}],
        "reels": [{"url":"https://videos.pexels.com/video-files/7677253/7677253-hd_1920_1080_30fps.mp4","cap":"Wedding Look ✨"}],
        "highlights": ["Diwali ✨","Shoot 📸","Travel ✈️"]},
    "aarav_travel": {"name": "Aarav Sharma", "gender": "boy", "pic": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=300", "bio": "Traveller ✈️ | Mountains ❤️ | Vlogger", "followers": ["sana_fashion","rohan_fit"], "following": ["sana_fashion","tommy_dog"], "audio": "🎵 Mood: Travelling - Mountains", "posts": [
        {"type":"photo","url":"https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=600","cap":"Manali Trip 🏔️ #travel"},
        {"type":"photo","url":"https://images.unsplash.com/photo-1469474968028-56623f02e42e?w=600","cap":"Nature Love 🌿 #travel"}],
        "reels": [{"url":"https://videos.pexels.com/video-files/2169880/2169880-hd_1920_1080_30fps.mp4","cap":"Mountain View 🏔️"}],
        "highlights": ["Manali 🏔️","Goa 🏖️"]},
    "priya_food": {"name": "Priya Singh", "gender": "girl", "pic": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=300", "bio": "Foodie 🍕 | Home Chef | Delhi Food Tour", "followers": ["sana_fashion","aarav_travel","tommy_dog"], "following": ["sana_fashion"], "audio": "🎵 Mood: Hungry 😋", "posts": [
        {"type":"photo","url":"https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=600","cap":"Best Pizza 🍕 #food"},
        {"type":"photo","url":"https://images.unsplash.com/photo-1567620905732-2d1ec7ab7445?w=600","cap":"Pancakes 🥞 #food"}],
        "reels": [{"url":"https://videos.pexels.com/video-files/3298762/3298762-hd_1920_1080_25fps.mp4","cap":"Street Food 🍕"}],
        "highlights": ["Pizza 🍕","Cafe ☕"]},
    "rohan_fit": {"name": "Rohan Verma", "gender": "boy", "pic": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=300", "bio": "Gym 💪 | Fitness Coach | No Pain No Gain", "followers": ["sana_fashion","aarav_travel"], "following": ["sana_fashion","aarav_travel"], "audio": "🎵 Mood: Gym Mode 🔥", "posts": [
        {"type":"photo","url":"https://images.unsplash.com/photo-1517836357463-d25dfeac3438?w=600","cap":"Gym Day 💪 #gym"},
        {"type":"photo","url":"https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=600","cap":"Workout 🔥 #gym"}],
        "reels": [{"url":"https://videos.pexels.com/video-files/4754030/4754030-hd_1920_1080_25fps.mp4","cap":"Gym Motivation 💪"}],
        "highlights": ["Gym 💪","Diet 🥗"]},
    "tommy_dog": {"name": "Tommy The Dog", "gender": "animal", "pic": "https://images.unsplash.com/photo-1543466835-00a7907e9de1?w=300", "bio": "Cute Dog 🐶 | Daily Cuteness | Follow for treats", "followers": ["priya
                
