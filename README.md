# Gamma-Ray Spectroscopy Radiological Assessment Pipeline

An automated Python pipeline for calculating radionuclide activity concentrations (238U, 232Th, and 40K) and evaluating radiological hazard indices from gamma-ray spectroscopy peak area data.

## Features
* **Calibration & Activity Concentrations:** Computes calibration constants (K) and sample activity concentrations (Bq/kg) with full error propagation.
* **Radiological Hazard Assessment:** Calculates key radiation protection metrics and compares them against international safety limits:
  * **Absorbed Dose Rate (D)** (nGy/h)
  * **Annual Effective Dose Equivalent (AEDE)** (mSv/year)
  * **Radium Equivalent Activity (Ra_eq)** (Bq/kg)
  * **External & Internal Hazard Indices (H_ex, H_in)**
  * **Activity Utilization Index (AUI)**
  * **Excess Lifetime Cancer Risk (ELCR)**
* **Automated Visualization:** Generates 300-DPI bar charts with regulatory limit thresholds for each parameter.
* **Comprehensive Reporting:** Exports a multi-sheet formatted Excel workbook (`Radiological_Final_Report.xlsx`) containing results, propagated uncertainties, compliance analysis, statistical summaries, embedded plots, and a plain-text interpretation summary.

## Project Structure
```text
gamma-pipeline/
├── main.py              # Main pipeline controller and Excel data ingestion
├── calculations.py      # Physics equations and uncertainty propagation functions
├── reference_data.py    # Standard reference material parameters (U, Th, K)
├── report.py            # Matplotlib graph generation, statistics, and text summary
├── report_excel.py      # Formatted multi-sheet Excel report builder
├── samples.xlsx         # Input workbook ('Samples' and 'Reference' sheets)
├── requirements.txt     # Python dependencies
├── .gitignore           # Ignored cache and output files
└── README.md            # Project documentation
```

## Input Data Format (`samples.xlsx`)
Ensure `samples.xlsx` is in the root directory and contains two sheets:
1. **`Reference` sheet:** Columns `Reference Material` (`U`, `Th`, `K`), `Peak Area`, `Peak Area Error`, `Activity (Bq/kg)`, and `Activity Error (Bq/kg)`.
2. **`Samples` sheet:** Columns `Sample`, `U_Area`, `U_Error`, `Th_Area`, `Th_Error`, `K_Area`, and `K_Error`.

## Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd gamma-ray-pipeline
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the pipeline:**
   ```bash
   python main.py
   ```

