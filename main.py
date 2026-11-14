import streamlit as st

st.set_page_config(page_title="InstaClone - Full App", layout="wide")

# ---------- SESSION - Login yaad rakhne ke liye ----------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user = ""
    st.session_state.dp = "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=200"
    st.session_state.my_posts = []
    st.session_state.blocked = []
    st.session_state.notifications = ["❤️ fashion_daily ne tumhari post like ki", "💬 foodie_girl ne comment kiya: Nice! 😍", "👤 fit_life ne tumhe follow kiya"]
    st.session_state.chats = {"fashion_daily": ["Hi! 😍", "Tumhari reel super thi"], "foodie_girl": ["Pizza khane chale? 🍕"]}

# ---------- LOGIN PAGE ----------
if not st.session_state.logged_in:
    st.markdown("<h1 style='text-align:center'>📸 InstaClone</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center'>Login karke apna Insta kholo</p>", unsafe_allow_html=True)
    u = st.text_input("Username - kuch bhi likho, jaise samiksha")
    p = st.text_input("Password", type="password")
    if st.button("Log In"):
        if u:
            st.session_state.logged_in = True
            st.session_state.user = u
            st.success(f"Welcome @{u} 🎉")
            st.rerun()
        else:
            st.error("Username to likho!")
    st.info("Demo ke liye koi bhi username/password chalega. Real Insta jesa login hai.")
    st.stop()

# ---------- LOGGED IN - TOP BAR ----------
col1, col2, col3 = st.columns([2,1,1])
with col1:
    st.markdown(f"### 📸 InstaClone | Hi, @{st.session_state.user} 👋")
with col2:
    if st.button("🔔 Notifications"):
        st.session_state.show_notif = True
with col3:
    if st.button("🚪 Log Out"):
        st.session_state.logged_in = False
        st.rerun()

# Notification dikhao
if st.session_state.get("show_notif"):
    st.subheader("🔔 Notifications")
    for n in st.session_state.notifications:
        st.write(n)
    if st.button("Notifications Band Karo"):
        st.session_state.show_notif = False
        st.rerun()

# ---------- SEARCH + CATEGORY ----------
st.subheader("🔍 Search & Explore")
search = st.text_input("Search karo - username, festival, wedding, gym, funny, study...", "festival")
category = st.selectbox("Category Chunno", ["All", "Festival 🎉", "Wedding 💍", "Games 🎮", "Study 📚", "Funny 😂", "Gym 💪", "Sports ⚽", "Nature 🌿", "Food 🍕", "Fashion 👗", "Dance 💃"])

# ---------- DATA - Pehle se bhare hue Posts/Reels ----------
POSTS = [
    {"user": "fashion_daily", "cat": "Festival 🎉", "type": "photo", "url": "https://images.unsplash.com/photo-1533174072545-7a4b6ad7a6c3?w=600", "caption": "Diwali Vibes ✨ #festival #diwali", "likes": "12.4K"},
    {"user": "wedding_diaries", "cat": "Wedding 💍", "type": "photo", "url": "https://images.unsplash.com/photo-1519741497674-611481863552?w=600", "caption": "Shaadi Season Started! ❤️ #wedding", "likes": "25K"},
    {"user": "foodie_girl", "cat": "Food 🍕", "type": "photo", "url": "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=600", "caption": "Best Pizza Ever! 🤤 #food", "likes": "8.2K"},
    {"user": "fit_life", "cat": "Gym 💪", "type": "photo", "url": "https://images.unsplash.com/photo-1517836357463-d25dfeac3438?w=600", "caption": "No Pain No Gain 💪 #gym", "likes": "15K"},
    {"user": "study_with_me", "cat": "Study 📚", "type": "photo", "url": "https://images.unsplash.com/photo-1434030216411-0b793f4b4173?w=600", "caption": "Exam Mode On 📚 #study", "likes": "5K"},
    {"user": "funny_reels", "cat": "Funny 😂", "type": "photo", "url": "https://images.unsplash.com/photo-1529626455594-4ff0802cfb7e?w=600", "caption": "Ye wala to funny tha 😂 #funny", "likes": "30K"},
]

REELS = [
    {"user": "dance_queen", "cat": "Dance 💃", "url": "https://videos.pexels.com/video-files/5309381/5309381-hd_1920_1080_25fps.mp4", "caption": "New Dance Trend 💃 #dance"},
    {"user": "fashion_daily", "cat": "Fashion 👗", "url": "https://videos.pexels.com/video-files/7677253/7677253-hd_1920_1080_30fps.mp4", "caption": "Wedding Look ✨ #fashion #wedding"},
    {"user": "fit_life", "cat": "Gym 💪", "url": "https://videos.pexels.com/video-files/4754030/4754030-hd_1920_1080_25fps.mp4", "caption": "Gym Motivation 🔥 #gym"},
    {"user": "sports_hub", "cat": "Sports ⚽", "url": "https://videos.pexels.com/video-files/3195394/3195394-hd_1920_1080_25fps.mp4", "caption": "Football Skills ⚽ #sports"},
    {"user": "foodie_girl", "cat": "Food 🍕", "url": "https://videos.pexels.com/video-files/3298762/3298762-hd_1920_1080_25fps.mp4", "caption": "Street Food Tour 🍕 #food"},
]

# Search filter
if search and search not in ["festival"]:
    POSTS = [p for p in POSTS if search.lower() in p["user"].lower() or search.lower() in p["caption"].lower() or search.lower() in p["cat"].lower()]
    REELS = [r for r in REELS if search.lower() in r["user"].lower() or search.lower() in r["caption"].lower()]
if category != "All":
    POSTS = [p for p in POSTS if category in p["cat"]]
    REELS = [r for r in REELS if category in r["cat"]]

tab1, tab2, tab3, tab4, tab5 = st.tabs(["🏠 Feed", "🎬 Reels", "➕ Post / Story", "💬 Chat", "👤 Profile"])

# ---------- FEED ----------
with tab1:
    st.subheader("Stories")
    s1, s2, s3, s4 = st.columns(4)
    for col, name in zip([s1,s2,s3,s4], ["fashion_daily","foodie_girl","fit_life","wedding_diaries"]):
        with col:
            st.image("https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=200", width=70)
            st.write(f"@{name}")
            st.caption("🟢 Story")
    st.write("---")
    for i, p in enumerate(POSTS):
        if p["user"] in st.session_state.blocked:
            continue
        st.write(f"**@{p['user']}** - {p['cat']}  •  {p['caption']}")
        st.image(p["url"], width=400)
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            if st.button(f"❤️ {p['likes']}", key=f"like{i}"):
                st.success("Liked!")
        with c2:
            if st.button("💬 Comment", key=f"c{i}"):
                st.write("💬 Nice pic! 😍")
        with c3:
            if st.button("🚫 Block", key=f"b{i}"):
                st.session_state.blocked.append(p["user"])
                st.warning(f"@{p['user']} Blocked!")
                st.rerun()
        with c4:
            if st.button("🗑️ Delete", key=f"d{i}"):
                st.info("Ye demo post hai, apni post Profile se delete kar sakte ho")
        st.write("---")
    # Tumhari khud ki posts
    for p in st.session_state.my_posts:
        st.write(f"**@{st.session_state.user} (You)** - {p['caption']}")
        if p["type"] == "image":
            st.image(p["data"], width=400)
        else:
            st.video(p["data"])
        st.write("---")

# ---------- REELS ----------
with tab2:
    st.subheader("🎬 Reels - Scroll Karo")
    for i, r in enumerate(REELS):
        if r["user"] in st.session_state.blocked:
            continue
        st.write(f"**@{r['user']}** - {r['cat']} - {r['caption']}")
        st.video(r["url"])
        cc1, cc2, cc3 = st.columns(3)
        with cc1:
            if st.button("❤️ Like", key=f"rl{i}"):
                st.success("Reel Liked ❤️")
        with cc2:
            if st.button("💬 Comment", key=f"rc{i}"):
                st.write("Amazing! 🔥")
        with cc3:
            if st.button("🚫 Block", key=f"rb{i}"):
                st.session_state.blocked.append(r["user"])
                st.rerun()
        st.write("---")
    if not REELS:
        st.warning("Is category me koi reel nahi, All select karo")

# ---------- POST / STORY ----------
with tab3:
    st.subheader("➕ Naya Post / Story / Audio Note")
    choice = st.radio("Kya dalna hai?", ["Post - Photo/Video", "Story - 24hrs", "Close Friends Story 🔒", "Audio Note 🎙️"])
    caption = st.text_input("Caption / Audio Note likho - jaise 'Diwali vibes ✨' ya 'Mood: Happy 🎵'")
    uploaded = st.file_uploader("Photo/Video chuno", type=["jpg","png","jpeg","mp4"])
    if uploaded:
        if uploaded.type.startswith("image"):
            st.image(uploaded, width=400)
            st.session_state.my_posts.append({"type":"image","data":uploaded,"caption":caption})
        else:
            st.video(uploaded)
            st.session_state.my_posts.append({"type":"video","data":uploaded,"caption":caption})
        if st.button("Post Karo 🚀"):
            st.balloons()
            st.success(f"Ho gaya! {choice} post ho gaya. Feed me jake dekho!")
    if choice == "Audio Note 🎙️":
        st.info("🎵 Audio Note: Tumhara mood yaha likha jayega - " + caption if caption else "Apna mood likho upar")
    if choice == "Close Friends Story 🔒":
        st.warning("🔒 Ye story sirf Close Friends ko dikhegi - fashion_daily, foodie_girl")

# ---------- CHAT ----------
with tab4:
    st.subheader("💬 Chats")
    chat_user = st.selectbox("Kisko message karna hai?", list(st.session_state.chats.keys()))
    for msg in st.session_state.chats[chat_user]:
        st.write(f"**@{chat_user}:** {msg}")
    new_msg = st.text_input("Message likho...")
    if st.button("Send ➡️"):
        if new_msg:
            st.session_state.chats[chat_user].append(f"You: {new_msg}")
            st.rerun()
    if st.button(f"Block @{chat_user}"):
        st.session_state.blocked.append(chat_user)
        st.warning("Blocked!")

# ---------- PROFILE ----------
with tab5:
    st.subheader("👤 My Profile")
    dp_file = st.file_uploader("Apni DP lagao 📸", type=["jpg","png","jpeg"])
    if dp_file:
        st.session_state.dp = dp_file
        st.success("DP lag gayi!")
    st.image(st.session_state.dp, width=120)
    st.write(f"**@{st.session_state.user}**")
    st.write(f"**{len(st.session_state.my_posts)+120} Posts | 1.2K Followers | 450 Following**")
    st.write("Bio: ML + Python Student | InstaClone Creator ✨ | 🎵 Audio: Happy")
    st.write(f"🚫 Blocked Log: {', '.join(st.session_state.blocked) if st.session_state.blocked else 'Koi nahi'}")
    if st.button("Unblock Sabko"):
        st.session_state.blocked = []
        st.rerun()
    st.write("---")
    st.subheader("🔍 Account Search - Private/Public Check")
    acc = st.text_input("Username likho - fashion_daily, foodie_girl, fit_life")
    ALL_USERS = {"fashion_daily": ("Sana Khan - Public ✅", "45K"), "foodie_girl": ("Priya - Public ✅", "8.2K"), "fit_life": ("Rohan - Public ✅", "25K"), "wedding_diaries": ("Aisha - Private 🔒", "10K")}
    if acc:
        if acc in ALL_USERS:
            st.success(f"@{acc} - {ALL_USERS[acc][0]} | Followers: {ALL_USERS[acc][1]}")
            if "Private" in ALL_USERS[acc][0]:
                st.warning("🔒 Private Account - Follow Request bhejna padega, posts nahi dikhenge")
            else:
                st.info("✅ Public Account - Posts dekh sakte ho, Feed me hai")
        else:
            st.warning(f"@{acc} nahi mila - Private ho sakta hai ya naam galat hai")

# ---------- ML ----------
st.write("---")
st.subheader("🤖 ML: Spam + Hashtag")
cc = st.text_input("Comment check karo - spam hai ya nahi?")
if cc:
    if any(w in cc.lower() for w in ["free","link","followers","click","win"]):
        st.error("🚨 ML: SPAM COMMENT")
    else:
        st.success("✅ ML: SAFE COMMENT")
cat2 = st.selectbox("Photo kiski hai?", ["Festival","Wedding","Gym","Study","Funny"])
if st.button("Hashtag Banao"):
    st.info(f"#{cat2.lower()} #viral #trending #explorepage #instagood #reels")
