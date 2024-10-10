import streamlit as st
from app import music_master
from PIL import Image

def main():
    options = ['MusicMaster', "Visuals"]
    choice = st.sidebar.selectbox("Menu", options, key='1')

    if choice == 'MusicMaster':
        music_master()

    elif choice == "Visuals":
        st.write("### Spotify Dashboard Visualization")
        image = Image.open("tableau_dashboard.png")
        st.image(image, caption="Spotify Tableau Dashboard", use_column_width=False, width=800)
        st.markdown("""
        **[Click here to view the Tableau Dashboard](https://public.tableau.com/app/profile/urzi.alessia/viz/spotify-api/Dashboard2?publish=yes)**  
        Please note that this will open the dashboard in a new tab.
        """)

    else:
        st.stop()

if __name__ == '__main__':
    main()