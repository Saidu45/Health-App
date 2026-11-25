
import csv
from database import db


def export_survey_data():

    # Retrieve all survey records from MongoDB
    records = db.users.find()

    # Prepare CSV file location
    output_file = "data/healthcare_survey.csv"

    # Define CSV column headings
    fieldnames = [
        "age",
        "gender",
        "total_income",
        "utilities",
        "entertainment",
        "school_fees",
        "shopping",
        "healthcare",
        "created_at"
    ]

    # Open CSV file for writing
    with open(output_file, mode="w", newline="", encoding="utf-8") as file:

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        # Loop through MongoDB records
        for record in records:

            expenses = record.get("expenses", {})

            row = {
                "age": record.get("age"),
                "gender": record.get("gender"),
                "total_income": record.get("total_income"),
                "utilities": expenses.get("utilities", 0),
                "entertainment": expenses.get("entertainment", 0),
                "school_fees": expenses.get("school_fees", 0),
                "shopping": expenses.get("shopping", 0),
                "healthcare": expenses.get("healthcare", 0),
                "created_at": record.get("created_at")
            }

            writer.writerow(row)

    print("CSV export completed successfully!")
    print(f"File saved to: {output_file}")


if __name__ == "__main__":
    export_survey_data()
