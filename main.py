import streamlit as st
st.set_page_config(page_title="InstaClone", layout="wide")

USERS = {
"sana_fashion": {"name": "Sana Khan", "pic": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=300", "bio": "Fashion | Delhi", "audio": "Mood: Happy", "posts": ["https://images.unsplash.com/photo-1524504388940-b1c1722653e1?w=600", "https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?w=600"], "reels": ["https://videos.pexels.com/video-files/7677253/7677253-hd_1920_1080_30fps.mp4"], "followers": ["aarav_travel", "priya_food"], "following": ["aarav_travel"]},
"aarav_travel": {"name": "Aarav Sharma", "pic": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=300", "bio": "Traveller | Mountains", "audio": "Mood: Travelling", "posts": ["https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=600"], "reels": ["https://videos.pexels.com/video-files/2169880/2169880-hd_1920_1080_30fps.mp4"], "followers": ["sana_fashion"], "following": ["sana_fashion"]},
"priya_food": {"name": "Priya Singh", "pic": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=300", "bio": "Foodie | Home Chef", "audio": "Mood: Hungry", "posts": ["https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=600"], "reels": ["https://videos.pexels.com/video-files/3298762/3298762-hd_1920_1080_25fps.mp4"], "followers": ["sana_fashion"], "following": ["sana_fashion"]},
"rohan_fit": {"name": "Rohan Verma", "pic": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=300", "bio": "Gym | Fitness Coach", "audio": "Mood: Gym Mode", "posts": ["https://images.unsplash.com/photo-1517836357463-d25dfeac3438?w=600"], "reels": ["https://videos.pexels.com/video-files/4754030/4754030-hd_1920_1080_25fps.mp4"], "followers": ["sana_fashion"], "following": ["sana_fashion"]},
"tommy_dog": {"name": "Tommy The Dog", "pic": "https://images.unsplash.com/photo-1543466835-00a7907e9de1?w=300", "bio": "Cute Dog | Daily Cuteness", "audio": "Mood: Playful", "posts": ["https://images.unsplash.com/photo-1543466835-00a7907e9de1?w=600"], "reels": ["https://videos.pexels.com/video-files/3195394/3195394-hd_1920_1080_25fps.mp4"], "followers": ["priya_food"], "following": ["priya_food"]},
"cat_lover": {"name": "Mimi The Cat", "pic": "https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?w=300", "bio": "Cat | Queen of House", "audio": "Mood: Sleepy", "posts": ["https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?w=600"], "reels": ["https://videos.pexels.com/video-files/3129671/3129671-hd_1920_1080_30fps.mp4"], "followers": ["tommy_dog"], "following": ["tommy_dog"]}
}

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user = "samiksha"
    st.session_state.bio = "Hi! I am Samiksha | ML Student"
    st.session_state.view_profile = None
    st.session_state.my_posts = []
    st.session_state.blocked = []

if not st.session_state.logged_in:
    st.markdown("<h1 style='text-align:center'>InstaClone</h1>", unsafe_allow_html=True)
    u = st.text_input("Username")
    p = st.text_input("Password", type="password")
    if st.button("Log In"):
        if u:
            st.session_state.logged_in = True
            st.session_state.user = u
            st.rerun()
    st.stop()

st.markdown("### InstaClone")
c1, c2, c3 = st.columns(3)
with c1:
    if st.button("Bell"):
        st.info("sana_fashion ne like kiya, priya_food ne comment kiya")
with c2:
    if st.button("Chat"):
        st.info("sana_fashion: Hi! | priya_food: Pizza chale?")
with c3:
    if st.button("My Profile"):
        st.session_state.view_profile = "MY"
        st.rerun()

search = st.text_input("Search - sana, aarav, priya, rohan, tommy, cat...")
category = st.selectbox("Category", ["All", "Festival", "Wedding", "Gym", "Food", "Fashion", "Travel", "Animal"])

if st.session_state.view_profile:
    if st.button("Back to Feed"):
        st.session_state.view_profile = None
        st.rerun()
    if st.session_state.view_profile == "MY":
        st.subheader(st.session_state.user)
        st.image("https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=200", width=120)
        st.write("Posts: " + str(len(st.session_state.my_posts)))
        st.write("Bio: " + st.session_state.bio)
        st.write("Audio Note: Happy")
        with st.expander("Settings & Edit Profile"):
            nb = st.text_area("Bio badlo", st.session_state.bio)
            if st.button("Save Bio"):
                st.session_state.bio = nb
                st.success("Saved!")
            if st.button("Log Out"):
                st.session_state.logged_in = False
                st.rerun()
        with st.expander("Dashboard"):
            st.write("Views: 1240 | Likes: 5480 | New Followers: +128")
        st.subheader("Naya Post")
        cap = st.text_input("Caption")
        up = st.file_uploader("Photo/Video", type=["jpg", "png", "mp4"])
        if up:
            if st.button("Post Karo"):
                st.session_state.my_posts.append({"type": "image", "data": up, "caption": cap})
                st.balloons()
                st.rerun()
        for post in st.session_state.my_posts:
            st.image(post["data"], width=300)
            st.write(post["caption"])
    else:
        uname = st.session_state.view_profile
        d = USERS[uname]
        st.image(d["pic"], width=120)
        st.subheader("@" + uname)
        st.write(d["name"])
        st.write(d["bio"])
        st.write(d["audio"])
        st.write("Posts: " + str(len(d["posts"])) + " | Followers: " + str(len(d["followers"])) + " | Following: " + str(len(d["following"])))
        st.write("Followers List:")
        for f in d["followers"]:
            st.write("- @" + f + " - " + USERS[f]["name"])
            if st.button("View " + f, key="view" + f):
                st.session_state.view_profile = f
                st.rerun()
        st.write("Highlights: Diwali | Shoot | Travel")
        t1, t2 = st.tabs(["Posts", "Reels"])
        with t1:
            for url in d["posts"]:
                st.image(url, width=350)
                st.write("Likes: 2.4K")
        with t2:
            for url in d["reels"]:
                st.video(url)
        if st.button("Block " + uname):
            st.session_state.blocked.append(uname)
            st.session_state.view_profile = None
            st.rerun()
    st.stop()

st.subheader("Feed - Sabke alag-alag posts")
for uname, d in USERS.items():
    if uname in st.session_state.blocked:
        continue
    if search and search.lower() not in uname.lower():
        continue
    st.image(d["pic"], width=50)
    if st.button("View @" + uname, key="feed" + uname):
        st.session_state.view_profile = uname
        st.rerun()
    for url in d["posts"]:
        st.image(url, width=400)
        st.write(d["name"] + " - " + d["bio"])
    st.write("---")

st.subheader("Reels")
for uname, d in USERS.items():
    for url in d["reels"]:
        st.write("@" + uname + " ka Reel")
        st.video(url)

st.subheader("ML: Spam Detector")
cc = st.text_input("Comment check karo")
if cc:
    if "free" in cc.lower() or "link" in cc.lower():
        st.error("SPAM")
    else:
        st.success("SAFE")
