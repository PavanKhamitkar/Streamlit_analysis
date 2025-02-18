import streamlit as st
import pandas as pd
import numpy as np
import io
import matplotlib.pyplot as plt
import seaborn as sns

# Title of the dashboard
st.title("Streamlit Analysis Dashboard")

# Upload file section
uploaded_file = st.file_uploader("Upload a CSV (Reports_Metric_Table_Demo.csv) file", type=["csv"])

if uploaded_file:
    # Check if the uploaded file name matches the expected file
    if uploaded_file.name != "Reports_Metric_Table_Demo.csv":
        st.error("Please upload only 'Reports_Metric_Table_Demo.csv'")
    else:
        # Read the uploaded CSV into a DataFrame
        df = pd.read_csv(uploaded_file)

        # Dropping rows with missing values in critical date columns
        df = df.dropna(subset=['CREATED_DATE_TIME', 'MODIFIED_DATE_TIME'])

        # Filling other missing values with 'Unknown'
        df.fillna("Unknown", inplace=True)

        # Convert date columns to datetime format
        df['CREATED_DATE_TIME'] = pd.to_datetime(df['CREATED_DATE_TIME'], errors='coerce')
        df['MODIFIED_DATE_TIME'] = pd.to_datetime(df['MODIFIED_DATE_TIME'], errors='coerce')

        # Create a Year-Month column for time-based analysis
        df['YearMonth'] = df['CREATED_DATE_TIME'].dt.to_period('M')

        # Set a consistent style for plots
        sns.set(style="whitegrid")

        # Display the dataframe if button is clicked
        if st.button("Show DataFrame"):
            st.dataframe(df)

        # Dropdown menu to select chart type
        chart_type = st.selectbox(
            "Select the type of chart you want to see:",
            ["Display dataset info", "Top 10 Workspaces by Report Count", "Reports Created Per Day of the Week",
             "Reports Created Per Hour of the Day", "Top Report Types", "Workspace Type Distribution",
             "Reports Created Over Time", "Reports on Dedicated Capacity (%)", "Heatmap of Reports Created Per Month-Year"]
        )

        # Display dataset info
        if chart_type == "Display dataset info":
            st.header("Dataset Info:")
            buffer = io.StringIO()
            df.info(buf=buffer)
            st.text(buffer.getvalue())

        # Top 10 Workspaces by Report Count
        elif chart_type == "Top 10 Workspaces by Report Count":
            plt.figure(figsize=(10,5))
            top_workspaces = df['WORKSPACE_NAME'].value_counts().head(10)
            sns.barplot(x=top_workspaces.values, y=top_workspaces.index, palette="magma")
            plt.xlabel("Count")
            plt.ylabel("Workspace Name")
            plt.title("Top 10 Workspaces by Report Count")
            st.pyplot(plt)

        # Reports Created Per Day of the Week
        elif chart_type == "Reports Created Per Day of the Week":
            plt.figure(figsize=(8,5))
            df['DayOfWeek'] = df['CREATED_DATE_TIME'].dt.day_name()
            sns.countplot(x=df['DayOfWeek'], order=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], palette="coolwarm")
            plt.xlabel("Day of the Week")
            plt.ylabel("Number of Reports")
            plt.title("Reports Created Per Day of the Week")
            st.pyplot(plt)

        # Reports Created Per Hour of the Day
        elif chart_type == "Reports Created Per Hour of the Day":
            plt.figure(figsize=(10,5))
            sns.histplot(df['CREATED_DATE_TIME'].dt.hour, bins=24, kde=True, color="green")
            plt.xlabel("Hour of the Day")
            plt.ylabel("Number of Reports")
            plt.title("Reports Created Per Hour of the Day")
            st.pyplot(plt)

        # Top 10 Report Types
        elif chart_type == "Top Report Types":
            plt.figure(figsize=(10,5))
            report_type_counts = df['REPORT_TYPE'].value_counts().head(10)
            sns.barplot(x=report_type_counts.values, y=report_type_counts.index, palette="viridis")
            plt.xlabel("Count")
            plt.ylabel("Report Type")
            plt.title("Top 10 Report Types")
            st.pyplot(plt)

        # Workspace Type Distribution
        elif chart_type == "Workspace Type Distribution":
            plt.figure(figsize=(8,4))
            workspace_type_counts = df['WORKSPACE_TYPE'].value_counts()
            sns.barplot(x=workspace_type_counts.values, y=workspace_type_counts.index, palette="coolwarm")
            plt.xlabel("Count")
            plt.ylabel("Workspace Type")
            plt.title("Workspace Type Distribution")
            st.pyplot(plt)

        # Reports Created Over Time
        elif chart_type == "Reports Created Over Time":
            plt.figure(figsize=(16,8))
            reports_per_month = df['YearMonth'].value_counts().sort_index()
            reports_per_month.plot(kind='line', marker='o', color='b')
            plt.xlabel("Year-Month")
            plt.ylabel("Number of Reports")
            plt.title("Reports Created Over Time")
            plt.xticks(rotation=45)
            plt.grid(True)
            st.pyplot(plt)

        # Reports on Dedicated Capacity (%)
        elif chart_type == "Reports on Dedicated Capacity (%)":
            plt.figure(figsize=(7,4))
            dedicated_capacity_counts = df['IS_ON_DEDICATED_CAPACITY'].value_counts(normalize=True) * 100
            dedicated_capacity_counts.plot(kind='bar', color=['green', 'red'])
            plt.ylabel("Percentage")
            plt.title("Reports on Dedicated Capacity (%)")
            plt.xticks([0, 1], ["No", "Yes"], rotation=0)
            st.pyplot(plt)

        # Heatmap of Reports Created Per Month-Year
        elif chart_type == "Heatmap of Reports Created Per Month-Year":
            pivot_table = df.pivot_table(index=df['CREATED_DATE_TIME'].dt.year, columns=df['CREATED_DATE_TIME'].dt.month, values='REPORT_NAME', aggfunc='count')
            plt.figure(figsize=(10,6))
            sns.heatmap(pivot_table, cmap="Blues", annot=True, fmt=".0f")
            plt.xlabel("Month")
            plt.ylabel("Year")
            plt.title("Heatmap of Reports Created Per Month-Year")
            st.pyplot(plt)
