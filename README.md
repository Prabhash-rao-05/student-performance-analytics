# Student Performance Analytics System

A Python-based data analytics project that analyzes student academic performance using **Python, Pandas, and NumPy**. The system calculates student totals and averages, assigns grades, identifies pass/fail results, analyzes subject performance, identifies top performers, and exports reports to CSV files.

## Project Overview

The Student Performance Analytics System helps analyze academic data and generate meaningful insights from student marks and attendance. It uses Pandas for data manipulation, NumPy for numerical calculations, and reusable Python functions to perform the analysis efficiently.

The project uses a dataset containing 30 fictional student records across three subjects: Python, Mathematics, and Statistics.

## Features

- Load student data from a CSV file.
- Store and process student records using a Pandas DataFrame.
- Calculate total marks and average marks for each student.
- Assign grades based on academic performance.
- Determine pass/fail status.
- Calculate class average, highest average, and lowest average.
- Analyze average marks for individual subjects.
- Identify the top five student performers.
- Analyze student attendance.
- Export student performance and subject analysis reports to CSV files.
- Validate the dataset and test core functions.

## Technologies Used

- **Python** — core programming and application logic.
- **Pandas** — data loading, DataFrame operations, and analysis.
- **NumPy** — numerical calculations and conditional operations.
- **CSV** — storage of student records and generated reports.
- **Git and GitHub** — version control and project hosting.

## Project Structure

```text
student-performance-analytics/
│
├── data/
│   └── students.csv
│
├── output/
│   ├── student_performance_report.csv
│   └── subject_analysis.csv
│
├── .gitignore
├── check_dataset.py
├── functions.py
├── main.py
├── test_functions.py
├── requirements.txt
├── README.md
└── Project_Documentation.md
```

## Dataset Description

The dataset is stored in `data/students.csv` and contains 30 fictional student records.

| Column | Description |
|---|---|
| Student_ID | Unique student identifier |
| Name | Student name |
| Department | Student department |
| Python | Marks obtained in Python |
| Mathematics | Marks obtained in Mathematics |
| Statistics | Marks obtained in Statistics |
| Attendance | Student attendance percentage |

Marks and attendance are represented as percentages or values between 0 and 100.

## Grading System

The system assigns grades according to the student's average marks. A student who scores below 40 in any subject receives an F grade.

| Grade | Average Marks |
|---|---:|
| A+ | 90–100 |
| A | 80–89.99 |
| B | 70–79.99 |
| C | 60–69.99 |
| D | 50–59.99 |
| F | Below 50 |

**Pass/Fail Rule:** A student passes only if their grade is not F. Therefore, scoring below 40 in any subject results in failure, even if the overall average is 50 or higher.

## Installation and Setup

### 1. Open the project folder

Open the project directory in Visual Studio Code.

### 2. Create and activate a virtual environment

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If the virtual environment already exists, activate it using the second command.

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

The project requires Python, Pandas, and NumPy.

## How to Run the Project

Run the following commands from the project root directory.

### Validate the dataset

```powershell
python check_dataset.py
```

### Run the analytics system

```powershell
python main.py
```

### Run the basic tests

```powershell
python test_functions.py
```

The main program displays class statistics, subject-wise averages, top performers, and student performance information. It also generates CSV reports in the `output/` directory.

## Project Results

The current dataset produces the following results:

| Metric | Result |
|---|---:|
| Total Students | 30 |
| Students Passed | 24 |
| Students Failed | 6 |
| Class Average | 70.29 |
| Highest Student Average | 96.33 |
| Lowest Student Average | 38.33 |
| Average Attendance | 85.27% |

### Subject-wise Average

| Subject | Average Marks |
|---|---:|
| Statistics | 70.90 |
| Mathematics | 70.60 |
| Python | 69.37 |

### Top Five Performers

| Rank | Student | Average | Grade |
|---:|---|---:|---|
| 1 | Aditi Kulkarni | 96.33 | A+ |
| 2 | Priya Reddy | 94.00 | A+ |
| 3 | Ananya Singh | 91.67 | A+ |
| 4 | Vivaan Shah | 90.33 | A+ |
| 5 | Simran Kaur | 89.33 | A |

These results are based on the current dataset. They may change if the student records are modified.

## Output Files

After running `main.py`, the system generates:

- `output/student_performance_report.csv` — student details, marks, total, average, grade, and pass/fail status.
- `output/subject_analysis.csv` — subject-wise performance summary.

## Testing and Validation

The project includes a dataset validation script and basic function tests. The dataset validation checks the data shape, unique student IDs, missing values, and valid marks. The test script verifies basic functionality and prints a success message when the assertions pass.

## Learning Outcomes

Through this project, the following concepts are demonstrated:

- Python functions, loops, conditions, and modular programming.
- NumPy calculations and conditional operations.
- Pandas DataFrames and CSV data handling.
- Data validation and exploratory data analysis.
- Grade calculation and performance classification.
- Report generation and basic testing.

## Future Enhancements

- Build an interactive dashboard using Streamlit.
- Add visualizations using Matplotlib or Seaborn.
- Include semester-wise performance comparisons.
- Add filters by department and grade.
- Generate downloadable PDF reports.

## Conclusion

The Student Performance Analytics System demonstrates how Python, Pandas, and NumPy can be used to process academic records and generate useful performance insights. It provides a simple, reusable foundation for student data analysis and automated reporting.

**Project status:** Core analytics, CSV report generation, dataset validation, and basic testing are implemented.