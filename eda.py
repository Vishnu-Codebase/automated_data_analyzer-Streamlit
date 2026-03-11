import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def run_eda(df):

    st.write("Dataset Shape:", df.shape)

    st.write("Column Data Types")
    st.write(df.dtypes)

    st.write("Missing Values")
    st.write(df.isnull().sum())

    st.write("Statistical Summary")
    st.write(df.describe())

    numeric_columns = df.select_dtypes(include=['int64','float64']).columns

    if len(numeric_columns) > 0:

        st.subheader("Distribution Plots")

        for col in numeric_columns:

            fig, ax = plt.subplots()

            sns.histplot(df[col], kde=True, ax=ax)

            ax.set_title(f"Distribution of {col}")

            st.pyplot(fig)