import streamlit as st
import random

st.set_page_config(page_title="InstaClone + API", layout="wide")
st.markdown("<h1 style='text-align:center'>📸 InstaClone - Search Reels</h1>", unsafe_allow_html=True)

# Bina API Key ke - Real Pexels Videos ka Database
VIDEOS = {
    "travel": [
        "https://videos.pexels.com/video-files/2169880/2169880-hd_1920_1080_30fps.mp4",
        "https://videos.pexels.com/video-files/3571264/3571264-hd_1920_1080_30fps.mp4",
    ],
    "cat": [
        "https://videos.pexels.com/video-files/3195394/3195394-hd_1920_1080_25fps.mp4",
        "https://videos.pexels.com/video-files/3129671/3129671-hd_1920_1080_30fps.mp4",
    ],
    "gym": [
        "https://videos.pexels.com/video-files/4754030/4754030-hd_1920_1080_25fps.mp4",
        "https://videos.pexels.com/video-files/4165422/4165422-hd_1920_1080_25fps.mp4",
    ],
    "beach": [
        "https://videos.pexels.com/video-files/1093662/1093662-hd_1920_1080_30fps.mp4",
        "https://videos.pexels.com/video-files/1409899/1409899-hd_1920_1080_25fps.mp4",
    ],
    "food": [
        "https://videos.pexels.com/video-files/3298762/3298762-hd_1920_1080_25fps.mp4",
        "https://videos.pexels.com/video-files/3298761/3298761-hd_1920_1080_25fps.mp4",
    ]
}

search = st.text_input("🔍 Search karo - travel, cat, gym, beach, food", "travel").lower().strip()

if search in VIDEOS:
    st.success(f"Showing Reels for: {search}")
    for i, link in enumerate(VIDEOS[search]):
        st.write(f"**@creator_{search}_{i+1}** - #{search} #viral #reels")
        st.video(link)
        st.write("❤️ 5.2K | 💬 340 comments")
        st.write("---")
else:
    st.warning("Is word ke liye video nahi hai, try karo: travel, cat, gym, beach, food")
    st.write("Niche wale sab videos dekh lo:")
    for k, links in VIDEOS.items():
        st.video(links[0])

st.subheader("🤖 ML: Spam Comment Detector")
comment = st.text_input("Comment likho")
if comment:
    if any(w in comment.lower() for w in ["free", "link", "followers", "click"]):
        st.error("🚨 ML Result: SPAM")
    else:
        st.success("✅ ML Result: SAFE")
