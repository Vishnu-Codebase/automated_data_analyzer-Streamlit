# Automated Data Analyzer

A simple **Streamlit-based data analysis tool** that lets users upload a CSV or Excel dataset, perform exploratory data analysis (EDA), generate summary statistics, visualize results, and export a report as an Excel workbook.

This project is designed to be **employer-ready**: it includes a clean UI, modular code organization, and clear setup instructions so others can run, test, and extend the application easily.

---

## ✅ Key Features

- Upload a CSV or Excel file via a web interface
- Display a data preview and summary statistics
- Perform exploratory data analysis (EDA) automatically
- Change column data types (e.g., string → datetime) and create binned categorical features
- Generate charts and export them
- Export a full Excel report with raw data + summary
- Download a bundled EDA + visuals package (charts + stats + report)

---

## 🚀 Getting Started

### Prerequisites

- Windows / macOS / Linux
- Python 3.11+ (project uses Python 3.14 in the venv but should work with 3.11+)
- Git (optional, for cloning)

### 1) Clone this repository

```bash
git clone <repo-url>
cd automated_data_analyzer
```

### 2) Create & activate a virtual environment

**Windows (PowerShell)**

```powershell
python -m venv .venv
& .\.venv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

### 4) Run the app

```bash
streamlit run app.py
```

Then open the URL shown in the console (usually http://localhost:8501).

---

## 🗂️ Project Structure

- `app.py` – Main Streamlit application entry point
- `eda.py` – Exploratory data analysis logic
- `analysis.py` – Core analysis routines and visualizations
- `report_generator.py` – Generates an Excel report with raw data and summaries
- `requirements.txt` – Python dependencies
- `output/` – Generated reports and charts

---

## � How It Works (Core Flow)

1. **`app.py`** is the UI layer. It accepts file uploads, shows previews, lets the user pick columns, and triggers analysis.
2. **`eda.py`** runs exploratory data analysis (EDA) on the uploaded dataset and displays descriptive stats and plots.
3. **`analysis.py`** performs the main computation (summary table and maybe charts) based on the selected value/category columns.
4. **`report_generator.py`** takes the raw data + analysis output and writes an Excel report to `output/report.xlsx`.

---

## �🧪 How to Use

1. Start the app with `streamlit run app.py`
2. Upload a `.csv` or `.xlsx` file
3. Select the value and category columns
4. Click **Generate Analysis** to view results and download:
   - A chart PNG
   - A full Excel report (`output/report.xlsx`)

---

## ✅ Notes / Improvements

- If the app fails to start due to missing packages, run:

```bash
pip install -r requirements.txt
```

- The generated output files are placed in `output/`.
- To add new analysis capabilities, extend `analysis.py` and/or `eda.py`.

---

## � Extension Ideas (Employer-Ready Enhancements)

Here are a few ways to make this project even more compelling for interviews or production use:

- **More chart types** (bar charts, histograms, boxplots, scatter matrices, heatmaps, etc.)
- **Multiple sheet exports**: generate an Excel report with separate sheets for raw data, summary stats, and visualizations
- **Filtering & cleaning steps**: allow users to filter rows, drop NaNs, normalize/standardize columns, or apply date parsing
- **Data profiling**: add a full profile report (e.g., using `pandas-profiling` / `ydata-profiling`) to surface data quality issues
- **Theme/custom styling**: add custom Streamlit themes, dark mode support, or brand colors
- **Upload history**: keep a history of recently uploaded datasets and let users re-run analysis quickly

---

## �📌 License

This project is provided as-is for demonstration and learning purposes.
