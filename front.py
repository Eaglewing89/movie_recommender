import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Movie recommendations", page_icon=":pie_chart", layout="wide"
)


# Load the data
@st.cache_data
def load_data(filename):
    df = pd.read_csv(filename)
    return df


df = load_data("numerical_dataframe.csv")

st.title("Movie recommender")
st.write(
    "Recommendations. About movies!"
)

st.header("Overall Statistics")
col_1_1, col_1_2 = st.columns(2)

with col_1_1:
    st.metric("Number of movies", f"{len(df):,}")

with col_1_2:
    columns_genres = list(df.filter(like="Genre:"))
    df_genre_sum = df[columns_genres].sum()
    st.metric("Most popular genre", f"{
              df_genre_sum.idxmax().lstrip("Genre: ")}")


st.image("tmdb_logo.svg", caption="API from themoviedb.org")
