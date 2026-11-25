# Healthcare Survey Application

## 1. Project Overview

The Healthcare Survey Application is a web-based application developed using Python and Flask. It collects participant demographic and financial information, stores survey responses in MongoDB Atlas, and supports data export and analysis.

The application was developed as part of the BAN6420 Final Project.

## 2. Main Features

- Participant age and gender collection.
- Total income collection.
- Monthly expense collection across five categories:
  - Utilities
  - Entertainment
  - School Fees
  - Shopping
  - Healthcare
- MongoDB Atlas database integration.
- CSV data export.
- Data cleaning and preparation using Python.
- Statistical analysis using Pandas and NumPy.
- Data visualization using Matplotlib and Seaborn.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Flask | Web application framework |
| MongoDB Atlas | Cloud database |
| PyMongo | MongoDB connection |
| HTML and CSS | User interface |
| JavaScript | Form interactions |
| Pandas | Data manipulation |
| NumPy | Numerical analysis |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Jupyter Notebook | Data analysis |

## 4. Project Structure

```text
Healthcare-Survey-Application/
│
├── data/
│   └── healthcare_survey.csv
│
├── exports/
│   ├── income_by_age.png
│   ├── gender_spending.png
│   ├── gender_summary.csv
│   └── financial_summary.csv
│
├── notebooks/
│
├── static/
├── templates/
│   └── index.html
│
├── app.py
├── database.py
├── models.py
├── export_data.py
├── healthcare_survey_analysis.ipynb
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## 5. Installation and Setup

### Prerequisites

- Python 3.12 or later
- MongoDB Atlas account
- Visual Studio Code (recommended)

### Create a virtual environment

```powershell
python -m venv .venv
```

### Activate the environment

```powershell
.\.venv\Scripts\Activate.ps1
```

### Install dependencies

```powershell
pip install -r requirements.txt
```

### Configure environment variables

Create a `.env` file using `.env.example` as a guide.

Set the following variables:

```text
MONGODB_URI=your_mongodb_connection_string
DATABASE_NAME=healthcare_survey
SECRET_KEY=your_generated_secret_key
```

Never commit your `.env` file or database credentials to GitHub.

## 6. Running the Application

Start the Flask application:

```powershell
python app.py
```

Open the local application in your browser:

```text
http://127.0.0.1:5000
```

## 7. Exporting Survey Data

Run:

```powershell
python export_data.py
```

The exported survey dataset is saved to:

```text
data/healthcare_survey.csv
```

## 8. Data Analysis

Open `healthcare_survey_analysis.ipynb` in Jupyter Notebook.

The analysis includes:

- Data loading and inspection.
- Data cleaning and validation.
- Descriptive statistics.
- Total expense calculations.
- Remaining income calculations.
- Average income analysis by age.
- Gender-based spending analysis.
- Data visualization.

## 9. Generated Outputs

The application produces the following analytical outputs:

| Output | Description |
|---|---|
| income_by_age.png | Income visualization by age |
| gender_spending.png | Spending comparison by gender |
| gender_summary.csv | Summary statistics by gender |
| financial_summary.csv | Overall financial summary |

## 10. Data Privacy and Security

- Database credentials are stored in environment variables.
- The `.env` file is excluded from version control.
- MongoDB Atlas provides cloud database storage.
- Survey records should be handled securely.
- Only authorized and appropriately consented survey information should be collected.

## 11. Project Limitations

The quality and reliability of the analysis depend on the number and representativeness of survey responses. Small datasets may not support reliable generalizations.

## 12. Conclusion

The Healthcare Survey Application demonstrates how a Flask web application can collect survey information, store it in MongoDB Atlas, export records to CSV, and support statistical analysis and visualization using Python.