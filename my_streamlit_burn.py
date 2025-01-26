import streamlit as st
import pandas as pd

# App Title
st.title("Burning Man Community Platform")
st.subheader("Next-Generation Digital Sandbox for Burners")

# Navigation Menu
menu = st.sidebar.selectbox("Navigate", ["Home", "Virtual Playa", "Skill Swap", "Sustainability Tracker", "Event Organizer"])

# Home Page
if menu == "Home":
    st.image("https://via.placeholder.com/800x400", caption="Welcome to the Burning Man Platform", use_column_width=True)
    st.write("""
    Welcome to the Burning Man Next-Generation Community Platform! 
    Explore, collaborate, and connect with Burners from around the world.
    """)
    st.write("Navigate using the sidebar to explore different features.")

# Virtual Playa Page
elif menu == "Virtual Playa":
    st.header("Explore the Virtual Playa")
    st.write("Discover art installations, camps, and performances happening virtually.")
    events = {
        "Art Installations": ["The Man", "Temple of Reflection", "Infinite Sands"],
        "Camps": ["Camp 1: Radical Inclusion", "Camp 2: Gifting Hub", "Camp 3: Leave No Trace"],
        "Performances": ["Fire Dancing", "DJ Night", "Sunrise Meditation"]
    }
    for category, items in events.items():
        st.subheader(category)
        st.write(", ".join(items))

# Skill Swap Page
elif menu == "Skill Swap":
    st.header("Global Skill Swap")
    st.write("Offer your skills or request help from other Burners.")
    skill_offers = st.text_area("What skills can you offer?")
    skill_needs = st.text_area("What skills are you looking for?")
    if st.button("Submit Skill Swap"):
        st.success("Your skill swap has been submitted!")

# Sustainability Tracker Page
elif menu == "Sustainability Tracker":
    st.header("Track Your Sustainability Efforts")
    st.write("Log and measure your contributions to the environment.")
    practices = st.multiselect(
        "Select eco-friendly practices:",
        ["Recycling", "Using Renewable Energy", "Composting", "Reducing Waste"]
    )
    if st.button("Log Practices"):
        st.success(f"Logged practices: {', '.join(practices)}")
    st.metric("Your Sustainability Score", len(practices) * 10)

# Event Organizer Page
elif menu == "Event Organizer":
    st.header("Event Organizer")
    st.write("Create or view upcoming events.")
    event_name = st.text_input("Event Name")
    event_date = st.date_input("Event Date")
    event_desc = st.text_area("Event Description")
    if st.button("Create Event"):
        st.success(f"Event '{event_name}' has been created!")
    st.subheader("Upcoming Events")
    st.write("1. Art Exhibit on Jan 30th\n2. Campfire Tales on Feb 5th")

# Footer
st.sidebar.info("Burning Man Platform | Designed for Radical Self-Expression")