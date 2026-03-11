import pandas as pd

def generate_excel_report(df, summary):

    with pd.ExcelWriter("output/report.xlsx") as writer:

        df.to_excel(
            writer,
            sheet_name="Raw Data",
            index=False
        )

        summary.to_excel(
            writer,
            sheet_name="Summary"
        )