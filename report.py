from turtle import width

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os


BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
    )


def create_graphs(df):

    # -----------------------------
    # Activity Concentrations graph
    # -----------------------------

    plt.figure(figsize=(10, 5))

    x = np.arange(1, len(df) + 1)

    width = 0.25

    plt.bar(
        x - width,
        df["U"],
        width,
        label="238U"
    )

    plt.bar(
        x,
        df["Th"],
        width,
        label="232Th"
    )

    plt.bar(
        x + width,
        df["K"],
        width,
        label="40K"
    )

    plt.xlabel("Samples")
    plt.ylabel("Activity Concentration (Bq/kg)")
    plt.title("Radionuclide Activity Concentrations")

    plt.xticks(
        x,
        x,
        rotation=45
    )

    plt.legend()

    plt.grid(
        axis="y",
        alpha=0.3
    )

    plt.tight_layout()

    plt.savefig(
        os.path.join(
           BASE_DIR,
           "Activity_Concentrations.png"
        ),
        dpi=300
    )

    plt.close()

    # -----------------------------
    # Absorbed Dose Rate graph
    # -----------------------------

    plt.figure(figsize=(8, 5))

    x = np.arange(1, len(df) + 1)

    plt.bar(
        df["Sample"],
        df["Dose"],
        label="Dose Rate"
    )

    plt.axhline(
        58,
        color="red",
        linestyle="--",
        label="Limit 58 nGy/h"
        )


    plt.xlabel("Samples")
    plt.ylabel("Dose Rate (nGy/h)")
    plt.title("Absorbed Dose Rate")

    plt.xticks(
    x,
    x,
    rotation=45
    )

    plt.legend()
    plt.grid(axis="y")
    plt.tight_layout()

    plt.savefig(
        os.path.join(
            BASE_DIR,
            "Absorbed_Dose_Rate.png"
        ),
        dpi=300
    )

    plt.close()


    # -----------------------------
    # Radium Equivalent graph
    # -----------------------------

    plt.figure(figsize=(8, 5))

    x = np.arange(1, len(df) + 1)

    plt.bar(
        df["Sample"],
        df["Raeq"]
    )

    plt.axhline(
        370,
        color="red",
        linestyle="--",
        label="Limit 370 Bq/kg"
    )

    plt.xlabel("Samples")
    plt.ylabel("Raeq (Bq/kg)")
    plt.title("Radium Equivalent Activity")

    plt.xticks(x, x, rotation=45)

    plt.legend()
    plt.grid(axis="y")

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            BASE_DIR,
            "Radium_Equivalent.png"
        ),
        dpi=300
    )

    plt.close()


    # -----------------------------
    # External Hazard Index graph
    # -----------------------------

    plt.figure(figsize=(8, 5))

    x = np.arange(1, len(df) + 1)

    plt.bar(
        df["Sample"],
        df["Hex"]
    )

    plt.axhline(
        1,
        color="red",
        linestyle="--",
        label="Limit = 1"
    )

    plt.xlabel("Samples")
    plt.ylabel("Hex")
    plt.title("External Hazard Index")

    plt.xticks(x, x, rotation=45)
    
    plt.legend()
    plt.grid(axis="y")
    plt.tight_layout()

    plt.savefig(
        os.path.join(
            BASE_DIR,
            "External_Hazard_Index.png"
        ),
        dpi=300
    )

    plt.close()


    # -----------------------------
    # Activity Utilization Index
    # -----------------------------

    plt.figure(figsize=(8, 5))

    x = np.arange(1, len(df) + 1)

    plt.bar(
        df["Sample"],
        df["AUI"]
       
    )

    plt.axhline(
        2,
        color="red",
        linestyle="--",
        label="Limit = 2"
    )
    plt.xlabel("Sample")
    plt.ylabel("Activity Utilization Index")
    plt.title("Activity Utilization Index")

    plt.xticks(x, x, rotation=45)

    plt.legend()
    plt.grid(axis="y")
    plt.tight_layout()

    plt.savefig(
        os.path.join(
            BASE_DIR,
            "Activity_Utilization_Index.png"
        ),
        dpi=300
    )

    plt.close()


    # -----------------------------
    # Internal Hazard Index
    # -----------------------------

    plt.figure(figsize=(8, 5))

    x = np.arange(1, len(df) + 1)

    plt.bar(
        df["Sample"],
        df["Hin"]
       
    )

    plt.axhline(
        1,
        color="red",
        linestyle="--",
        label="Limit = 1"
    )

    plt.xlabel("Sample")
    plt.ylabel("Internal Hazard Index")
    plt.title("Internal Hazard Index")

    plt.xticks(x, x, rotation=45)

    plt.legend()
    plt.grid(axis="y")

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            BASE_DIR,
            "Internal_Hazard_Index.png"
        ),
        dpi=300
    )

    plt.close()


    # -----------------------------
    # Annual Effective Dose
    # -----------------------------

    plt.figure(figsize=(8, 5))

    x = np.arange(1, len(df) + 1)

    plt.bar(
        df["Sample"],
        df["AEDE"]
        
    )

    plt.axhline(
        1,
        color="red",
        linestyle="--",
        label="Limit = 1"
    )


    plt.xlabel("Sample")
    plt.ylabel("Annual Effective Dose (mSv/year)")
    plt.title("Annual Effective Dose")

    plt.xticks(x, x, rotation=45)
    plt.legend()
    plt.grid(axis="y")

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            BASE_DIR,
            "Annual_Effective_Dose.png"
        ),
        dpi=300
    )

    plt.close()


    # -----------------------------
    # Excess Lifetime Cancer Risk
    # -----------------------------

    plt.figure(figsize=(8, 5))

    x = np.arange(1, len(df) + 1)

    plt.bar(
        df["Sample"],
        df["ELCR"],
        label="Excess Lifetime cancer risk"
       
    )

    plt.xlabel("Sample")
    plt.ylabel("Excess Lifetime Cancer Risk")
    plt.title("Excess Lifetime Cancer Risk")

    plt.xticks(x, x, rotation=45)
    plt.legend()
    plt.grid(axis="y")

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            BASE_DIR,
            "ELCR.png"
        ),
        dpi=300
    )

    plt.close()


def create_interpretation(df):

    interpretation_file = os.path.join(
        BASE_DIR,
        "Radiological_Interpretation.txt"
    )

    with open(
        interpretation_file,
        "w"
    ) as file:

        file.write(
            "Radiological Assessment Summary\n"
        )

        file.write(
            "=" * 40
        )

        file.write(
            "\n\n"
        )

        for _, row in df.iterrows():

            sample = row["Sample"]
            Raeq = row["Raeq"]
            Hex = row["Hex"]
            Hin = row["Hin"]
            Dose = row["Dose"]
            AEDE = row["AEDE"]
            AUI = row["AUI"]

            file.write(
                f"Sample: {sample}\n"
            )

            file.write(
                "-" * 30
            )

            file.write(
                "\n"
            )
            #---------------------------
            # Radium equivalent (Raeq) assessment
            #---------------------------
            file.write(
                f"Radium equivalent activity (Raeq): "
                f"{Raeq:.2f} Bq/kg\n"
            )

            if Raeq <= 370:

                file.write(
                    "Raeq status: Within recommended limit "
                    "(370 Bq/kg)\n"
                )

            else:

                file.write(
                    "Raeq status: ABOVE recommended limit "
                    "(370 Bq/kg)\n"
                )


           #---------------------------
           # Activity Utilization Index
           #---------------------------
            file.write(
                f"Activity utilisation index (AUI): "
                f"{AUI:.2f}\n"
            )

            if AUI <= 2:

                file.write(
                    " AUI status: Within recommended limit "
                    "(2)\n"
                )

            else:

                file.write(
                    "AUI status: ABOVE recommended limit "
                    "(2)\n"
                )    

            #---------------------------
            # Anual efective dose Equivalence
            #---------------------------
            file.write(
                f"Anual Efective Dose (AEDE): "
                f"{AEDE:.2f} msv/y\n"
            )

            if AEDE <= 1:

                file.write(
                    " AEDE status: Within recommended limit "
                    "(1 msv/y)\n"
                )

            else:

                file.write(
                    "AEDE status: ABOVE recommended limit "
                    "(1 msv/y)\n"
                )    

            #---------------------------
            # Absorbed dose rate(dose)
            #---------------------------
            file.write(
                f"Dose Rate (Dose) "
                f"{Dose:.2f} nGy/h\n"
            )

            if Dose <= 58:

                file.write(
                    " Dose status: Within recommended limit "
                    "(58 nGy/h)\n"
                )

            else:

                file.write(
                    "Dose status: ABOVE recommended limit "
                    "(58 nGy/h)\n"
                )   
            #---------------------------
            # External hazard index (Hex) assessment
            #---------------------------
            file.write(
                f"External hazard index (Hex): "
                f"{Hex:.3f}\n"
            )

            if Hex <= 1:

                file.write(
                    "Hex status: Radiation hazard is negligible\n"
                )

            else:

                file.write(
                    "Hex status: ABOVE unity; "
                    "increased external radiation hazard indicated\n"
                )

            #---------------------------
            # Internal hazard index (Hin) assessment
            #---------------------------
            file.write(
                f"Internal hazard index (Hin): "
                f"{Hin:.3f}\n"
            )

            if Hin <= 1:

                file.write(
                    "Hin status: Radiation hazard is negligible\n"
                )

            else:

                file.write(
                    "Hin status: ABOVE unity; "
                    "increased internal radiation hazard indicated\n"
                )

            file.write(
                "\n\n"
            )

def create_statistics_summary(df):

    # Columns to summarize
    columns = [
        "U",
        "±U",
        "Th",
        "±Th",
        "K",
        "±K",
        "Dose",
        "±Dose",
        "AEDE",
        "Raeq",
        "±Raeq",
        "Hex",
        "Hin",
        "ELCR",
        "AUI"
        
    ]

    # Create an empty list for the statistical results
    statistics = []

    # Calculate statistics for each parameter
    for column in columns:

        statistics.append({
            "Parameter": column,
            "Average (Mean)": df[column].mean(),
            "Standard Deviation": df[column].std(),
            "Minimum": df[column].min(),
            "Maximum": df[column].max()
        })

    # Convert the list into a DataFrame
    statistics = pd.DataFrame(statistics)

    return statistics