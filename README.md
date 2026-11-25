# Healthcare Survey Application

## 1. Project Overview

The Healthcare Survey Application is a web-based application developed using Python and Flask as part of the BAN6420 Final Project.

The application collects demographic and financial information from survey participants, including age, gender, total income, and monthly expenses across five categories.

The collected information is stored in MongoDB Atlas, a cloud-based database. The application also supports exporting survey records to CSV files for further processing, statistical analysis, and visualization using Python.

The project demonstrates the integration of web development, cloud database management, data engineering, and business analytics.

## 2. Project Objectives

The main objectives of this project are to:

- Develop a web-based healthcare survey application.
- Collect participant demographic and financial information.
- Store survey responses in MongoDB Atlas.
- Implement a Python class named `User` to represent survey participants.
- Export collected survey records into CSV format.
- Clean and prepare survey data using Python.
- Conduct descriptive statistical analysis.
- Develop visualizations showing income patterns by age and spending patterns by gender.
- Deploy the application online to demonstrate its functionality.

## 3. Main Features

### 3.1 Participant Information Collection

The application collects the following participant information:

- Age
- Gender
- Total income

### 3.2 Monthly Expense Collection

Participants can select their applicable expense categories and enter the corresponding amounts.

The five expense categories are:

1. Utilities
2. Entertainment
3. School Fees
4. Shopping
5. Healthcare

### 3.3 Database Integration

Survey responses are stored in MongoDB Atlas using PyMongo.

### 3.4 Data Export

The application includes a Python script that retrieves survey records from MongoDB Atlas and exports them into a CSV file.

### 3.5 Data Analysis and Visualization

The project uses Python libraries to clean, analyze, summarize, and visualize the collected information.

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Flask | Web application framework |
| MongoDB Atlas | Cloud database |
| PyMongo | MongoDB database connection |
| HTML | Web page structure |
| CSS | User interface styling |
| JavaScript | Form interactions |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Jupyter Notebook | Interactive data analysis |
| Gunicorn | Production application server |
| Git and GitHub | Source code management |
| Render | Application hosting and deployment |

## 5. Project Structure

The project is organized into the following directories and files:

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
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│   └── index.html
│
├── app.py
├── database.py
├── models.py
├── export_data.py
├── healthcare_survey_analysis.ipynb
├── requirements.txt
├── Procfile
├── .env.example
├── .gitignore
├── .ebignore
└── README.md
```

**Description of important files:**

| File | Description |
|---|---|
| `app.py` | Main Flask application and survey submission routes |
| `database.py` | MongoDB Atlas connection configuration |
| `models.py` | Defines the Python `User` class |
| `export_data.py` | Retrieves survey records and exports them to CSV |
| `index.html` | Contains the survey form |
| `requirements.txt` | Lists the Python dependencies |
| `Procfile` | Defines the production startup command |
| `healthcare_survey_analysis.ipynb` | Contains the data cleaning, analysis, and visualization workflow |
| `.env.example` | Provides an example of the required environment variables |
| `.gitignore` | Excludes sensitive and unnecessary files from Git |

## 6. Installation and Setup

### 6.1 Prerequisites

The following software and services are required:

- Python 3.12 or later
- MongoDB Atlas account
- Visual Studio Code (recommended)
- Git
- A web browser
- Jupyter Notebook

### 6.2 Clone the Repository

Clone the project from GitHub:

```bash
git clone https://github.com/Saidu45/Health-App.git
```

Navigate into the project directory:

```bash
cd Health-App
```

### 6.3 Create a Virtual Environment

Create a Python virtual environment:

```powershell
python -m venv .venv
```

Activate the environment in Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 6.4 Install Dependencies

Install the required Python packages:

```powershell
python -m pip install -r requirements.txt
```

### 6.5 Configure Environment Variables

Create a `.env` file in the project root directory.

Use `.env.example` as a reference and configure the following variables:

```text
MONGODB_URI=your_mongodb_connection_string
DATABASE_NAME=healthcare_survey
SECRET_KEY=your_generated_secret_key
```

Replace the placeholder values with your actual configuration.

**Security note:** Never upload `.env` to GitHub or include it in the final submission ZIP. Database credentials and secret keys must remain private.

## 7. MongoDB Atlas Configuration

MongoDB Atlas is used as the cloud database for storing survey responses.

The database configuration includes:

- Database name: `healthcare_survey`
- Collection name: `users`
- Database connection: PyMongo
- Connection configuration: Environment variables

The Flask application connects to MongoDB Atlas through the configuration defined in `database.py`.

When a participant submits a survey, the application creates a `User` object and stores the resulting document in the `users` collection.

## 8. Running the Application Locally

After installing the dependencies and configuring the environment variables, start the Flask application:

```powershell
python app.py
```

Open the following address in your browser:

```text
http://127.0.0.1:5000
```

The survey form will be displayed.

Participants can enter their demographic information, total income, and selected expense amounts before submitting the survey.

The application validates submitted information and saves valid survey records to MongoDB Atlas.

## 9. Data Export

The project includes `export_data.py`, which retrieves survey records from MongoDB Atlas and exports them into CSV format.

Run the following command:

```powershell
python export_data.py
```

The exported dataset is saved to:

```text
data/healthcare_survey.csv
```

The CSV file contains the following fields:

- Age
- Gender
- Total Income
- Utilities
- Entertainment
- School Fees
- Shopping
- Healthcare
- Created At

Expense categories that were not selected are represented by zero values in the exported dataset.

The CSV file can subsequently be loaded into Jupyter Notebook for analysis.

## 10. Data Cleaning and Preparation

The exported survey dataset is processed using Pandas and NumPy.

The data preparation process includes:

- Loading the CSV dataset.
- Inspecting the dataset structure.
- Checking missing values.
- Identifying duplicate records.
- Converting columns into appropriate data types.
- Validating age and income values.
- Checking expense values for invalid entries.
- Calculating total expenses.
- Calculating remaining income.

The following financial calculations are used:

**Total Expenses**

Total Expenses = Utilities + Entertainment + School Fees + Shopping + Healthcare

**Remaining Income**

Remaining Income = Total Income - Total Expenses

These calculations provide additional information for understanding participants' financial patterns.

## 11. Data Analysis and Visualization

The project uses Jupyter Notebook for statistical analysis and visualization.

Open the notebook:

```text
healthcare_survey_analysis.ipynb
```

The analysis includes the following activities:

### 11.1 Descriptive Statistics

Descriptive statistics are used to summarize the collected survey information.

These include:

- Mean
- Median
- Minimum
- Maximum
- Standard deviation
- Participant counts

### 11.2 Income Analysis by Age

The analysis examines income patterns across different participant ages.

The visualization compares average income across age groups represented in the dataset.

Generated output:

```text
exports/income_by_age.png
```

### 11.3 Gender-Based Spending Analysis

The analysis compares average spending across the five expense categories by gender.

The categories examined include:

- Utilities
- Entertainment
- School Fees
- Shopping
- Healthcare

Generated output:

```text
exports/gender_spending.png
```

### 11.4 Summary Tables

The notebook also generates summary tables containing financial and demographic statistics.

Generated files:

```text
exports/gender_summary.csv
exports/financial_summary.csv
```

## 12. Generated Analytical Outputs

The project produces the following analytical outputs:

| Output File | Description |
|---|---|
| `income_by_age.png` | Visualization of average income by participant age |
| `gender_spending.png` | Comparison of average spending across categories by gender |
| `gender_summary.csv` | Summary of participant counts and average financial indicators by gender |
| `financial_summary.csv` | Overall financial summary |

The generated charts can also be used in presentations and reports.

## 13. Online Deployment

### 13.1 Deployment Platform

The Healthcare Survey Application was successfully deployed using Render.

Render provides the hosting environment for the Flask application, allowing users to access the survey form through a web browser.

Live application:

https://healthcare-survey-application.onrender.com/

### 13.2 Deployment Configuration

The Render service uses the following configuration:

| Setting | Configuration |
|---|---|
| Service type | Web Service |
| Runtime | Python |
| Source repository | GitHub |
| Branch | main |
| Build command | `pip install -r requirements.txt` |
| Start command | `gunicorn app:app` |
| Database | MongoDB Atlas |

Environment variables are configured through the Render dashboard rather than committed to the source code repository.

### 13.3 Deployment Verification

The deployed application was tested to verify that:

- The survey homepage loads successfully.
- Participants can complete the survey form.
- Valid survey submissions are accepted.
- Submitted records are stored in MongoDB Atlas.
- The records can subsequently be retrieved through the local CSV export script.

### 13.4 AWS Deployment Limitation

AWS Elastic Beanstalk was initially considered as the deployment platform for this project.

However, AWS account activation required accepting a paid account plan. To avoid unexpected hosting charges, AWS deployment was not completed.

Render was therefore used as an alternative hosting platform to demonstrate the application's online functionality.

The application was successfully deployed and tested using Render and MongoDB Atlas.

## 14. Data Privacy and Security

The application incorporates basic security and data protection practices.

These include:

- Storing database connection details in environment variables.
- Excluding `.env` from Git version control.
- Keeping database credentials private.
- Using input validation for submitted survey information.
- Restricting MongoDB network access to configured addresses and ranges.
- Using HTTPS through the hosting platform.
- Avoiding the inclusion of sensitive credentials in the submission ZIP.

Survey information should only be collected with appropriate authorization and consent.

For demonstrations and academic submissions, fictional or appropriately anonymized records should be used.

## 15. Project Limitations

The project has some limitations:

1. **Sample size:** The reliability and representativeness of the analysis depend on the number and quality of survey responses.

2. **Self-reported information:** Financial information is provided by participants and may not always reflect their exact financial circumstances.

3. **Analytical limitations:** The analysis primarily focuses on descriptive statistics and visual comparisons rather than predictive modelling.

4. **Hosting limitations:** The Render free service may sleep after a period of inactivity, resulting in a delay when the application is accessed again.

5. **AWS deployment:** AWS Elastic Beanstalk deployment was not completed because the available AWS account required a paid plan.

## 16. Conclusion

The Healthcare Survey Application demonstrates the development of a complete survey-based web application using Python and Flask.

The application collects demographic and financial information, stores survey responses in MongoDB Atlas, and supports exporting the collected records into CSV format.

Python libraries, including Pandas, NumPy, Matplotlib, and Seaborn, are used to clean, analyze, summarize, and visualize the collected information.

The application was successfully deployed using Render, demonstrating how a cloud-hosted Flask application can communicate with a cloud database and support an online data collection workflow.

Overall, the project demonstrates practical applications of web development, database integration, data management, and statistical analysis in a healthcare survey context.

## 17. Project Links

**Live Application:**  
https://healthcare-survey-application.onrender.com/

**GitHub Repository:**  
https://github.com/Saidu45/Health-App

**Course:** BAN6420 Final Project

**Project Name:** Healthcare Survey Application
