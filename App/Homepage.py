import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Anime_recommendations', page_icon=':tada:', layout='wide')
# st.title('thighs')


def lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_movie = lottie_url("https://assets7.lottiefiles.com/packages/lf20_khzniaya.json")

with st.container():
    st.subheader('RecoMovie')
    st.write('This is a simple movie recommender')

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader('what the recommender does?')
        st.write('well, it gives you movie recommendations based on the input that u give in like a normal '
                 'recommendation system.')
        st.write("""
        you will get recommendations similar to the given movie.
        hence, if there is a movie that you love but cant find similar stuff
        this recommender will help you find your candy.
        so grab your popcorn and get your recommendation.
        """)

    with right_column:
        st_lottie(lottie_movie, height=300, key='movie')

with st.container():
    st.subheader("My socials:")
    st.write("[Instagram](https://www.youtube.com/)")
    st.write("[Github](https://www.youtube.com/)")
    st.write("[LinkedIn](https://www.youtube.com/)")