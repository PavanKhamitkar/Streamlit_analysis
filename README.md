# Streamlit Analysis Dashboard

A data visualization dashboard built with Streamlit for analyzing report metrics data with interactive charts and insights.

## 🚀 Features

- **File Upload**: Secure CSV file handling with validation
- **Data Processing**: Automatic cleaning and datetime formatting
- **Interactive Visualizations**: Multiple chart types including:
  - Workspace Analysis
  - Temporal Analysis
  - Report Type Distribution
  - Capacity Utilization

## 📊 Available Visualizations

1. **Basic Information**
   - Complete dataset information
   - Raw data view

2. **Workspace Analysis**
   - Top 10 Workspaces by Report Count
   - Workspace Type Distribution

3. **Temporal Analysis**
   - Daily distribution (Day of Week)
   - Hourly distribution
   - Monthly trends
   - Year-Month heatmap

4. **Report Analytics**
   - Top Report Types
   - Dedicated Capacity Usage (%)

## 🛠️ Installation

## 🛠️ Installation

```bash
# Create and activate virtual environment (Windows)
python -m venv venv
.\venv\Scripts\activate

# Install all required packages
pip install streamlit pandas numpy matplotlib seaborn

# Alternative: Install from requirements.txt
pip install -r requirements.txt

# Clone the repository
git clone https://github.com/PavanKhamitkar/Streamlit_analysis.git

# Navigate to project directory
cd Streamlit_analysis

```

## 📝 Requirements

```text
streamlit
pandas
numpy
matplotlib
seaborn
```

## 🚦 Usage

1. Start the Streamlit server:
```bash
streamlit run app.py
```

2. Open your browser and navigate to `http://localhost:8501`

3. Upload the `Reports_Metric_Table_Demo.csv` file

4. Select visualization type from the dropdown menu

## 📄 Input Data Format

The application expects a CSV file named `Reports_Metric_Table_Demo.csv` with the following columns:

- `CREATED_DATE_TIME`
- `MODIFIED_DATE_TIME`
- `WORKSPACE_NAME`
- `REPORT_TYPE`
- `WORKSPACE_TYPE`
- `IS_ON_DEDICATED_CAPACITY`
- `REPORT_NAME`

## 📈 Visualization Details

- Uses Seaborn and Matplotlib for plotting
- Consistent styling with white grid background
- Custom color palettes:
  - `magma`: Workspace analysis
  - `coolwarm`: Day-wise distribution
  - `viridis`: Report types
  - `Blues`: Time-based heatmap

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---
