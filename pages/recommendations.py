import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Recommendations", layout="wide")


# Load the data
@st.cache_data
def load_data(filename):
    df = pd.read_csv(filename)
    return df


df = load_data("numerical_dataframe.csv")
df = df.set_index("original_title")

df_clean = load_data("clean_dataframe.csv")
df_clean = df_clean.set_index("original_title")


st.title("Movie recommendations")

# Sidebar filters
st.sidebar.header("Movie recommender")

movie_name = st.sidebar.selectbox("Select a movie", df.index.values.tolist())

recommendations = st.sidebar.number_input(
    "Number of recommendations", min_value=1, max_value=100, value=5)

movie = df.loc[movie_name]
distances = np.linalg.norm(df-movie, axis=1)
indexes = np.argpartition(distances, recommendations)

st.write(f"Movies similar to {movie_name}")
st.write(df_clean.iloc[indexes[:recommendations]])
