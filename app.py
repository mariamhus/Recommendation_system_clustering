import streamlit as st
import pandas as pd
import joblib
import numpy as np

Model = joblib.load("Model.pkl")
Inputs = joblib.load("Inputs.pkl")

def recommend_top_n_categories(user_id, rfm_df, cluster_category, n=3):
    # Get the cluster for the user
    user_cluster = rfm_df[rfm_df['CustomerID'] == user_id]['cluster'].values[0]
    
    # Get the top n categories for that cluster
    top_n_categories = cluster_category[cluster_category['cluster'] == user_cluster].nlargest(n, 'count')['category']
    
    return top_n_categories.tolist()

def main():
    st.title("Recommendation system")
    user_id = st.number_input(
    "Insert user ID, Must be a number", value=None, placeholder="Type a number..."
)
    top_3_categories = recommend_top_n_categories(user_id, rfm_df, cluster_category, n=3)
st.write(f"Top 3 Recommended Categories for User {user_id}: {top_3_categories}")
main()
