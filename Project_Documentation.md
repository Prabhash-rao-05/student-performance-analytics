# Project Documentation: Student Performance Analytics System

## 1. Introduction

The Student Performance Analytics System is a Python-based data analysis project designed to evaluate student academic performance. It processes student records, calculates marks and averages, assigns grades, identifies pass/fail status, and summarizes performance across subjects.

The project demonstrates practical use of Python, Pandas, and NumPy for data processing and analysis.

## 2. Objectives

The main objectives of the project are:

1. Read and process student data from a CSV file.
2. Organize student records in a Pandas DataFrame.
3. Calculate total marks and average marks for each student.
4. Assign grades according to defined grading rules.
5. Determine student pass/fail status.
6. Calculate class-level performance statistics.
7. Analyze subject-wise average marks.
8. Identify the top five student performers.
9. Export the results into CSV reports.
10. Apply reusable functions and basic testing practices.

## 3. Tools and Technologies

| Technology | Purpose |
|---|---|
| Python | Application logic and programming |
| Pandas | Data loading, processing, and analysis |
| NumPy | Numerical calculations and conditional operations |
| CSV | Dataset and report storage |
| Visual Studio Code | Development environment |
| Git | Version control |

## 4. Dataset Description

The input dataset is stored in `data/students.csv`.

It contains 30 fictional student records with the following columns:

| Column | Description |
|---|---|
| Student_ID | Unique identifier for each student |
| Name | Student's name |
| Department | Academic department |
| Python | Marks in Python |
| Mathematics | Marks in Mathematics |
| Statistics | Marks in Statistics |
| Attendance | Attendance percentage |

The dataset is used to demonstrate academic performance analysis. It is not intended to represent real students or official academic records.

### Dataset Validation

The dataset validation script checks:

- The shape of the dataset.
- Whether student IDs are unique.
- Whether missing values exist.
- Whether marks are within the range of 0 to 100.

The current dataset contains 30 records and seven input columns, with unique student IDs, no missing values, and valid marks.

## 5. System Requirements

The project requires:

- Python installed on the computer.
- Pandas.
- NumPy.
- Visual Studio Code or another Python-compatible editor.
- A terminal to execute Python scripts.

Install the required libraries using:

```powershell
python -m pip install -r requirements.txt
```

## 6. Project Architecture

The project is organized into separate modules for data validation, analysis, execution, testing, and report generation.

### Main Components

**`data/students.csv`**

Contains the input student dataset.

**`check_dataset.py`**

Validates the dataset by checking record count, columns, unique IDs, missing values, and marks.

**`functions.py`**

Contains reusable functions for loading data, calculating totals and averages, assigning grades, determining pass/fail status, calculating statistics, analyzing subjects, identifying top performers, and exporting reports.

**`main.py`**

Runs the analysis workflow, displays results, and generates output reports.

**`test_functions.py`**

Contains basic assertions to test core functions.

**`output/`**

Stores the generated CSV reports.

## 7. Methodology

The system follows these steps:

1. Load the CSV dataset using Pandas.
2. Validate the input data.
3. Calculate the total marks for each student across Python, Mathematics, and Statistics.
4. Calculate average marks by dividing total marks by the number of subjects.
5. Assign grades based on the average marks and subject-level passing requirement.
6. Determine pass/fail status.
7. Calculate class statistics.
8. Calculate average marks for each subject.
9. Identify the top five performers.
10. Export student and subject analysis reports to CSV files.

## 8. Grade Calculation

The system uses the following grading thresholds:

| Grade | Average Marks |
|---|---:|
| A+ | 90–100 |
| A | 80–89.99 |
| B | 70–79.99 |
| C | 60–69.99 |
| D | 50–59.99 |
| F | Below 50 |

A student also receives an F grade if they score below 40 in any individual subject. The pass/fail result is determined from the final grade.

A student passes when the grade is not F. Otherwise, the student fails.

## 9. Functions and Responsibilities

The `functions.py` module contains the following functions:

| Function | Responsibility |
|---|---|
| `load_data()` | Loads student records from the CSV file |
| `calculate_totals()` | Calculates total marks for each student |
| `calculate_averages()` | Calculates average marks for each student |
| `assign_grades()` | Assigns grades using the grading rules |
| `calculate_pass_fail()` | Determines pass/fail status |
| `get_class_statistics()` | Calculates class-level statistics |
| `get_subject_analysis()` | Calculates subject-wise performance |
| `get_top_performers()` | Returns the highest-performing students |
| `export_reports()` | Saves analysis results as CSV files |

These functions make the program modular, easier to maintain, and reusable.

## 10. Results and Analysis

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

### Subject-wise Analysis

| Subject | Average Marks |
|---|---:|
| Statistics | 70.90 |
| Mathematics | 70.60 |
| Python | 69.37 |

Statistics has the highest average among the three subjects in the current dataset, while Python has the lowest average.

### Top Five Students

| Rank | Student | Average Marks | Grade |
|---:|---|---:|---|
| 1 | Aditi Kulkarni | 96.33 | A+ |
| 2 | Priya Reddy | 94.00 | A+ |
| 3 | Ananya Singh | 91.67 | A+ |
| 4 | Vivaan Shah | 90.33 | A+ |
| 5 | Simran Kaur | 89.33 | A |

These results are specific to the current sample dataset.

## 11. Generated Reports

The system generates two report files.

### Student Performance Report

File: `output/student_performance_report.csv`

This report contains student details, subject marks, total marks, average marks, grades, and pass/fail status.

### Subject Analysis Report

File: `output/subject_analysis.csv`

This report contains subject-wise summary information, including average marks.

The reports can be opened in Microsoft Excel, Google Sheets, or another application that supports CSV files.

## 12. Testing

The project includes `test_functions.py`, which uses Python assertions to check basic functionality.

Run the tests using:

```powershell
python test_functions.py
```

The current basic test script prints `All basic tests passed!` when its assertions pass.

The dataset validation script can be run separately:

```powershell
python check_dataset.py
```

## 13. Execution Instructions

Open the project folder in Visual Studio Code.

Activate the existing virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies if necessary:

```powershell
python -m pip install -r requirements.txt
```

Validate the dataset:

```powershell
python check_dataset.py
```

Run the main program:

```powershell
python main.py
```

Run the tests:

```powershell
python test_functions.py
```

After execution, check the `output/` directory for the generated reports.

## 14. Limitations

- The analysis is based on a sample dataset containing 30 fictional students.
- The system currently analyzes three academic subjects.
- The results depend on the input data and grading rules.
- The project produces CSV reports rather than an interactive web dashboard.
- The basic test script does not replace comprehensive automated testing.

## 15. Future Scope

The system can be extended by:

1. Creating an interactive dashboard with Streamlit.
2. Adding charts and visualizations with Matplotlib.
3. Comparing student performance across semesters.
4. Adding department-wise and grade-wise filters.
5. Supporting more subjects and larger datasets.
6. Generating PDF reports.
7. Adding more comprehensive automated tests.

## 16. Conclusion

The Student Performance Analytics System demonstrates how Python, Pandas, and NumPy can be used to process student records, calculate academic performance, classify grades, analyze subjects, and generate reports.

The project applies core Python programming concepts, data manipulation, numerical computation, reusable functions, validation, and basic testing to a practical academic analytics problem.