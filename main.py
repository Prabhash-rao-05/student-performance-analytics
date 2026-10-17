from functions import export_reports
from functions import (
    load_data,
    calculate_totals,
    calculate_averages,
    assign_grades,
    calculate_pass_fail,
    get_class_statistics,
    get_subject_analysis,
    get_top_performers
)
def main():
    try:
        df = load_data()
        df = calculate_totals(df)
        df = calculate_averages(df)
        df = assign_grades(df)
        df = calculate_pass_fail(df)
        stats = get_class_statistics(df)
        subjects = get_subject_analysis(df)
        top_students = get_top_performers(df)
        export_reports(df)
        print("\n" + "=" * 65)
        print("          STUDENT PERFORMANCE ANALYTICS SYSTEM")
        print("=" * 65)
        print(f"\nTotal Students       : {stats['total_students']}")
        print(f"Students Passed      : {stats['passed']}")
        print(f"Students Failed      : {stats['failed']}")
        print(f"Class Average        : {stats['class_average']}")
        print(f"Highest Average      : {stats['highest_average']}")
        print(f"Lowest Average       : {stats['lowest_average']}")
        print(f"Average Attendance   : {stats['average_attendance']}%")
        print("\n" + "-" * 65)
        print("                  SUBJECT-WISE ANALYSIS")
        print("-" * 65)
        for subject, average in subjects.items():
            print(f"{subject:<20}: {average:.2f}")
        print("\n" + "-" * 65)
        print("                    TOP 5 PERFORMERS")
        print("-" * 65)
        print(top_students[
            ["Student_ID", "Name", "Average_Marks", "Grade"]
        ].to_string(index=False))
        print("\n" + "-" * 65)
        print("                 COMPLETE STUDENT REPORT")
        print("-" * 65)
        print(df[
            ["Student_ID", "Name", "Department", "Total_Marks",
             "Average_Marks", "Grade", "Result", "Attendance"]
        ].to_string(index=False))
        print("\n" + "=" * 65)
        print("              ANALYSIS COMPLETED SUCCESSFULLY")
        print("=" * 65)
    except (ValueError, FileNotFoundError, pd.errors.ParserError) as error:
        print(f"\nError: {error}")
if __name__ == "__main__":
    import pandas as pd
    main()
