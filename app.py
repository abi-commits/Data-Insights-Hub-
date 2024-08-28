import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Data Dashboard")

uploaded_file = st.file_uploader("Choose a file",type=["csv","xlsx"])

if uploaded_file is not None:
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
        
    elif uploaded_file.name.endswith('.xlsx'):
        df = pd.read_excel(uploaded_file)

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())
    
    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select column to filter by", columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select value", unique_values)

    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)
    
    st.subheader("Plot Data")
    x_column = st.selectbox("Select x-axis column", columns)
    y_column = st.selectbox("Select y-axis column", columns)

    plot_type = st.selectbox("Select plot type", ["Line Chart", "Bar Chart", "Scatter Plot"])

    if st.button("Generate Plot"):
            try:
                if x_column not in filtered_df.columns or y_column not in filtered_df.columns:
                    st.error("Selected columns are not in the filtered data.")
                else:
                    if plot_type == "Line Chart":
                        st.line_chart(filtered_df.set_index(x_column)[y_column])
                    elif plot_type == "Bar Chart":
                        st.bar_chart(filtered_df.set_index(x_column)[y_column])
                    elif plot_type == "Scatter Plot":
                        fig, ax = plt.subplots()
                        ax.scatter(filtered_df[x_column], filtered_df[y_column])
                        ax.set_xlabel(x_column)
                        ax.set_ylabel(y_column)
                        ax.set_title(f"Scatter Plot of {y_column} vs {x_column}")
                        st.pyplot(fig)
            except Exception as e:
                st.error(f"Error generating plot: {e}")
else:
    st.write("Waiting on file upload...")
