# -*- coding: utf-8 -*-
"""11/19.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Mhw0XKUBEcdtNQYKPqvJhBmWeyCd4QCq
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title("CSV Data Visualization App")

# File uploader for two CSV files
uploaded_file_1 = st.file_uploader("Upload CSV File 1", type=["csv"])
uploaded_file_2 = st.file_uploader("Upload CSV File 2", type=["csv"])

if uploaded_file_1 is not None and uploaded_file_2 is not None:
    # Read the CSV files
    data_1 = pd.read_csv(uploaded_file_1)
    data_2 = pd.read_csv(uploaded_file_2)

    # Display the previews of both files
    st.write("### Data Preview (File 1)")
    st.dataframe(data_1)
    st.write("### Data Preview (File 2)")
    st.dataframe(data_2)

    # Dropdown for selecting columns for File 1
    columns_1 = data_1.columns.tolist()
    x_column_1 = st.selectbox("Select X-axis column for File 1", columns_1, key="x1")
    y_column_1 = st.selectbox("Select Y-axis column for File 1", columns_1, key="y1")

    # Dropdown for selecting columns for File 2
    columns_2 = data_2.columns.tolist()
    x_column_2 = st.selectbox("Select X-axis column for File 2", columns_2, key="x2")
    y_column_2 = st.selectbox("Select Y-axis column for File 2", columns_2, key="y2")

    # Dropdown for graph type
    graph_type = st.selectbox(
        "Select Graph Type",
        ["Line", "Scatter", "Bar"]
    )

    # Plot button
    if st.button("Plot Graph"):
        fig, ax = plt.subplots(figsize=(10, 6))  # Create a single plot

        # Plot for File 1 with a different color
        if graph_type == "Line":
            ax.plot(data_1[x_column_1], data_1[y_column_1], label=f"File 1: {y_column_1} vs {x_column_1}", color='blue', marker='o')
        
        elif graph_type == "Scatter":
            ax.scatter(data_1[x_column_1], data_1[y_column_1], label=f"File 1: {y_column_1} vs {x_column_1}", color='blue')
        
        elif graph_type == "Bar":
            ax.bar(data_1[x_column_1], data_1[y_column_1], label=f"File 1: {y_column_1} vs {x_column_1}", alpha=0.5)

        # Plot for File 2 with a different color
        if graph_type == "Line":
            ax.plot(data_2[x_column_2], data_2[y_column_2], label=f"File 2: {y_column_2} vs {x_column_2}", color='red', marker='o')
        
        elif graph_type == "Scatter":
            ax.scatter(data_2[x_column_2], data_2[y_column_2], label=f"File 2: {y_column_2} vs {x_column_2}", color='red')
        
        elif graph_type == "Bar":
            ax.bar(data_2[x_column_2], data_2[y_column_2], label=f"File 2: {y_column_2} vs {x_column_2}", alpha=0.5)

        # Add labels and title
        ax.set_xlabel(f"{x_column_1} (File 1) and {x_column_2} (File 2)")
        ax.set_ylabel("Values")
        ax.set_title(f"{y_column_1} vs {x_column_1} (File 1) and {y_column_2} vs {x_column_2} (File 2)")
        
        # Show legend to differentiate the two datasets
        ax.legend()

        st.pyplot(fig)

else:
    st.info("Please upload both CSV files to get started.")
