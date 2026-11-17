import pandas as pd
import calculations as calc
import report
import report_excel
import os

# -------------------------------------------------

# Reference peak areas
# Reference data is taken automatically from Excel

# -------------------------------------------------

excel_file = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "samples.xlsx"
)

df = pd.read_excel(
    excel_file,
    sheet_name="Samples",
    engine="openpyxl"
)

# -------------------------------------------------
# Read reference data excel taking
# -------------------------------------------------

reference_df = pd.read_excel(
    excel_file,
    sheet_name="Reference",
    engine="openpyxl"
)
#--------------------------------------------------
# minimum detection activity(MDA) excel taking
#--------------------------------------------------







# -------------------------------------------------
# Get reference values automatically
# -------------------------------------------------

U_ref = reference_df[
    reference_df["Reference Material"] == "U"
 ].iloc[0]

Th_ref = reference_df[
    reference_df["Reference Material"] == "Th"
].iloc[0]

K_ref = reference_df[
    reference_df["Reference Material"] == "K"
].iloc[0]

# Uranium reference values

U_reference_area = U_ref["Peak Area"]
U_reference_error = U_ref["Peak Area Error"]
U_reference_activity = U_ref["Activity (Bq/kg)"]
U_activity_error = U_ref["Activity Error (Bq/kg)"]

# Thorium reference values

Th_reference_area = Th_ref["Peak Area"]
Th_reference_error = Th_ref["Peak Area Error"]
Th_reference_activity = Th_ref["Activity (Bq/kg)"]
Th_activity_error = Th_ref["Activity Error (Bq/kg)"]

# Potassium reference values

K_reference_area = K_ref["Peak Area"]
K_reference_error = K_ref["Peak Area Error"]
K_reference_activity = K_ref["Activity (Bq/kg)"]
K_activity_error = K_ref["Activity Error (Bq/kg)"]

# Calibration constants K of the elements and uncertainties

KU, sKU = calc.calibration_constant(
    U_reference_area,
    U_reference_activity,
    U_reference_error,
    U_activity_error
)

KTh, sKTh = calc.calibration_constant(
    Th_reference_area,
    Th_reference_activity,
    Th_reference_error,
    Th_activity_error
)

KK, sKK = calc.calibration_constant(
    K_reference_area,
    K_reference_activity,
    K_reference_error,
    K_activity_error
)

# Read sample data from excel file uploaded by as in the same excel as reference data

results = []

for _, row in df.iterrows():

    # for this command there it skips any empty sample rows so to not cause an issue with the calculations

    if pd.isna(row["Sample"]):
        continue

    # this part checks for missing columns

    required_columns = [
        "U_Area",
        "U_Error",
        "Th_Area",
        "Th_Error",
        "K_Area",
        "K_Error"
    ]

    if row[required_columns].isna().any():
        print(f"Skipping {row['Sample']}: missing either columns or row please")
        continue

    Cu, sCu = calc.activity_concentration(
        row["U_Area"],
        row["U_Error"],
        KU,
        sKU
    )

    Cth, sCth = calc.activity_concentration(
        row["Th_Area"],
        row["Th_Error"],
        KTh,
        sKTh
    )

    Ck, sKk = calc.activity_concentration(
        row["K_Area"],
        row["K_Error"],
        KK,
        sKK
    )

    D = calc.absorbed_dose(
        Cu,
        Cth,
        Ck
    )

    sD = calc.dose_error(
        sCu,
        sCth,
        sKk
    )

    AEDE = calc.annual_effective_dose(D)

    sAEDE = calc.annual_effective_dose_error(sD)

    Raeq = calc.radium_equivalent(
        Cu,
        Cth,
        Ck
    )

    sRaeq = calc.radium_error(
        sCu,
        sCth,
        sKk
    )

    Hex = calc.hazard_index(
        Cu,
        Cth,
        Ck
    )

    Hin = calc.int_hazard_index(
        Cu,
        Cth,
        Ck
    )

    AUI_val = calc.AUI(
        Cu,
        Cth,
        Ck
    )

    ELCR = calc.ELCR(AEDE)

    # ELCR from annual effective dose (mSv/year), using a 70-year lifetime
    # and a 0.057 per Sv risk coefficient.

    results.append({

        "Sample": row["Sample"],

        "U": Cu,
        "±U": sCu,

        "Th": Cth,
        "±Th": sCth,

        "K": Ck,
        "±K": sKk,

        "Dose": D,
        "±Dose": sD,

        "AEDE": AEDE,
        "±AEDE": sAEDE,

        "Raeq": Raeq,
        "±Raeq": sRaeq,

        "Hex": Hex,
        "Hin": Hin,

        "ELCR": ELCR,

        "AUI": AUI_val,

    })


# -------------------------------------------------
# Create output DataFrame
# -------------------------------------------------

output = pd.DataFrame(results)

print(output)

# -------------------------------------------------
# Create statistical summary
# -------------------------------------------------

statistics = report.create_statistics_summary(output)

print("\nStatistical Summary:")
print(statistics)

# -------------------------------------------------
# Create graphs and interpretation
# -------------------------------------------------

report.create_graphs(output)

report.create_interpretation(output)

# -------------------------------------------------
# Create final Excel report
# -------------------------------------------------

report_excel.create_excel_report(output, statistics)

report_excel.add_graphs_to_excel()

print("\nCalculation complete.")
print("Final report created successfully.")