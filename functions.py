import numpy as np
import pandas as pd
from pathlib import Path
SUBJECTS = ["Python", "Mathematics", "Statistics"]
def load_data(file_path="data/students.csv"):
    df = pd.read_csv(file_path)
    required_columns = ["Student_ID", "Name", "Department", *SUBJECTS, "Attendance"]
    missing_columns = set(required_columns) - set(df.columns)
    if missing_columns:
        raise ValueError(f"Missing required columns: {sorted(missing_columns)}")
    if df.empty:
        raise ValueError("The dataset contains no student records.")
    if df["Student_ID"].isna().any() or df["Student_ID"].duplicated().any():
        raise ValueError("Student IDs must be present and unique.")
    if df[["Name", "Department"]].isna().any().any():
        raise ValueError("Student names and departments cannot be missing.")
    numeric_columns = SUBJECTS + ["Attendance"]
    for column in numeric_columns:
        df[column] = pd.to_numeric(df[column], errors="raise")
    if df[numeric_columns].isna().any().any():
        raise ValueError("Marks and attendance cannot be missing.")
    if not df[SUBJECTS].apply(lambda col: col.between(0, 100)).all().all():
        raise ValueError("Subject marks must be between 0 and 100.")
    if not df["Attendance"].between(0, 100).all():
        raise ValueError("Attendance must be between 0 and 100.")
    return df
def calculate_totals(df):
    df = df.copy()
    df["Total_Marks"] = df[SUBJECTS].sum(axis=1)
    return df
def calculate_averages(df):
    df = df.copy()
    marks = df[SUBJECTS].to_numpy(dtype=float)
    df["Average_Marks"] = np.mean(marks, axis=1).round(2)
    return df
def assign_grades(df):
    df = df.copy()
    def get_grade(row):
        if (row[SUBJECTS] < 40).any():
            return "F"
        average = row["Average_Marks"]
        if average >= 90:
            return "A+"
        elif average >= 80:
            return "A"
        elif average >= 70:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 50:
            return "D"
        return "F"
    df["Grade"] = df.apply(get_grade, axis=1)
    return df
def calculate_pass_fail(df):
    df = df.copy()
    df["Result"] = np.where(df["Grade"] == "F", "Fail", "Pass")
    return df
def get_class_statistics(df):
    averages = df["Average_Marks"].to_numpy(dtype=float)
    return {
        "total_students": len(df),
        "passed": int((df["Result"] == "Pass").sum()),
        "failed": int((df["Result"] == "Fail").sum()),
        "class_average": round(float(np.mean(averages)), 2),
        "highest_average": round(float(np.max(averages)), 2),
        "lowest_average": round(float(np.min(averages)), 2),
        "average_attendance": round(float(np.mean(df["Attendance"])), 2)
    }
def get_subject_analysis(df):
    return df[SUBJECTS].mean().round(2).sort_values(ascending=False)
def get_top_performers(df, count=5):
    return df.sort_values(
        by=["Average_Marks", "Name"],
        ascending=[False, True]
    ).head(count)
def export_reports(df, output_dir="output"):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    student_report = output_path / "student_performance_report.csv"
    subject_report = output_path / "subject_analysis.csv"
    df.to_csv(student_report, index=False)
    subject_averages = df[SUBJECTS].mean().sort_values(ascending=False)
    subject_df = subject_averages.rename_axis("Subject").reset_index(name="Average_Marks")
    subject_df.to_csv(subject_report, index=False)
    print("\nReports exported successfully!")
    print(f"Student report: {student_report}")
    print(f"Subject report: {subject_report}")

