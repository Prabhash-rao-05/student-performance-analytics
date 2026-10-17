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
df = load_data()
df = calculate_totals(df)
df = calculate_averages(df)
df = assign_grades(df)
df = calculate_pass_fail(df)
print("First 5 processed students:")
print(df[["Student_ID", "Name", "Total_Marks", "Average_Marks", "Grade", "Result"]].head().to_string(index=False))
print("\nClass Statistics:")
for key, value in get_class_statistics(df).items():
    print(f"{key.replace('_', ' ').title()}: {value}")
print("\nSubject-wise Average Marks:")
print(get_subject_analysis(df).to_string())
print("\nTop 5 Performers:")
print(get_top_performers(df)[["Student_ID", "Name", "Average_Marks", "Grade"]].to_string(index=False))
assert len(df) == 30
assert df["Student_ID"].nunique() == 30
assert df["Total_Marks"].between(0, 300).all()
assert df["Average_Marks"].between(0, 100).all()
assert (df["Result"] == "Pass").sum() + (df["Result"] == "Fail").sum() == 30
assert len(get_top_performers(df)) == 5
assert get_subject_analysis(df).is_monotonic_decreasing
print("\nAll basic tests passed!")
