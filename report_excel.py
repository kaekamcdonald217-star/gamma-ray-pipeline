import os
import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.drawing.image import Image


def create_excel_report(df, statistics):


    filename = "Radiological_Final_Report.xlsx"


    # -----------------------------
    # the table to analyse the the constraints on the radiam equivalent and hazard index well i still need varification from sir if the limits are right and the use of words
    # -----------------------------

    assessment = []

    for _, row in df.iterrows():

        if row["Raeq"] <= 370:
            raeq_status = " its Within limit"
        else:
            raeq_status = "its Above limit"

        if row["AUI"] <= 2:
            aui_status = " its Within limit"
        else:
            aui_status = "its Above limit" 

        if row["Dose"] <= 58:
            dose_status = " its Within limit"
        else:
            dose_status = "its Above limit" 

        if row["AEDE"] <= 1:
            aede_status = " its Within limit"
        else:
            aede_status = "its Above limit"          

        if row["Hex"] <= 1:
            hex_status = "its Within limit"# like if its in limit or not in limit or maybe there is other ways to say it but i will leave it like this for now since i am not sure what is the best way to say it
        else:
            hex_status = "its above limit"

        if row["Hin"] <= 1:
            hin_status = "its Within limit"# like if its in limit or not in limit or maybe there is other ways to say it but i will leave it like this for now since i am not sure what is the best way to say it
        else:
            hin_status = "its above limit"

        assessment.append({

            "Sample": row["Sample"],
            "Raeq Status": raeq_status,
            "Hex Status": hex_status,
            "Hin Status": hin_status,
            "AEDE Status": aede_status,
            "AUI Status": aui_status,
            "Dose Status": dose_status


        })


    assessment_df = pd.DataFrame(assessment)


    # -----------------------------
    # on this section we will Write Excel data sheets like the results, uncertainties and analysis
    # -----------------------------

    with pd.ExcelWriter(filename,
                        engine="openpyxl") as writer:


        df.to_excel(
            writer,
            sheet_name="Results",
            index=False
        )


        uncertainty_columns = [

            "Sample",
            "±U",
            "±Th",
            "±K",
            "±Dose",
            "±AEDE",
            "±Raeq"

        ]


        df[uncertainty_columns].to_excel(

            writer,
            sheet_name="Uncertainties or errors",
            index=False

        )


        assessment_df.to_excel(

            writer,
            sheet_name="analysis",
            index=False

        )
        # -----------------------------
        # Statistical summary
        # -----------------------------

        statistics.to_excel(

              writer,
              sheet_name="Statistics",
              index=False)


    # -----------------------------
    # this section kinda just makes the excel report looks fancy just for the thrill of it leave with it mcdonald's style
    # -----------------------------

    wb = load_workbook(filename)


    for sheet in wb:

        for cell in sheet[1]:

            cell.font = Font(
                bold=True,
                color="FFFFFF"
            )

            cell.fill = PatternFill(

                "solid",
                fgColor="1F4E78"

            )

            cell.alignment = Alignment(
                horizontal="center"
            )


        for column in sheet.columns:

            max_length = 0

            column_letter = column[0].column_letter


            for cell in column:

                if cell.value:

                    max_length = max(
                        max_length,
                        len(str(cell.value))
                    )


            sheet.column_dimensions[
                column_letter
            ].width = max_length + 3


    wb.save(filename)


    print(
        "Final report is ready for u to see:",
        filename
    )

def add_graphs_to_excel():# not really needed but i will keep it for now since it is in the instructions and it is a good practice to have a function that adds graphs to the excel report

    filename = "Radiological_Final_Report.xlsx"

    wb = load_workbook(filename)

    BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
   )


    # Creating a graph sheet to put in excel

    if "Graphs" not in wb.sheetnames:
        ws = wb.create_sheet("Graphs")
    else:
        ws = wb["Graphs"]


    ws["A1"] = "Radiological Analysis Graphs"

    ws["A1"].font = Font(
        bold=True,
        size=16
    )


    # we are placing graphs as images into the "Graphs" sheet

    graphs = [

        ("Activity_Concentrations.png", "A3"),
        ("Absorbed_Dose_Rate.png", "A20"),
        ("Radium_Equivalent.png", "J3"),
        ("External_Hazard_Index.png", "J20"),
        ("Annual_Effective_Dose.png", "J54"),
        ("Activity_Utilization_Index.png", "A37"),
        ("Internal_Hazard_Index.png", "J37"),
        ("ELCR.png", "A54")

    ]


    for graph, position in graphs:

        graph_path = os.path.join(BASE_DIR, graph)

        if not os.path.exists(graph_path):
         print(f"Warning: graph not found: {graph_path}")
         continue

        img = Image(graph_path)

        img.width = 500
        img.height = 300

        ws.add_image(
            img,
            position
        )


    wb.save(filename)

    print("check the graphs are added to Excel report")    