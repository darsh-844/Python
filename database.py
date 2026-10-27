import numpy as np
import pandas as pd
from scipy import stats

np.random.seed(42)
n = 40
df = pd.DataFrame({    
    "Student_ID": range(1, n + 1),
    "Branch": np.random.choice(["CSE", "ECE", "ME", "CE"], n),
    "Study_Hours": np.round(np.random.uniform(1, 8, n), 1),
    "Attendance": np.random.randint(55, 100, n),
})
df["Marks"] = np.clip(
    np.round(30 + 5 * df["Study_Hours"] + 0.2 * df["Attendance"] + np.random.normal(0, 6, n)),
    0, 100).astype(int)
print("=====================================================================================")
print(df)
print("=====================================================================================")
print(df.head())

#====================== Task 1 ======================

def get_grade(marks):
    if marks >= 75:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "F"

print("=====================================================================================")
df["Grade"]=df["Marks"].apply(get_grade)
print("=====================================================================================")
print(df[["Student_ID", "Marks", "Grade"]].head())
print("=====================================================================================")
print(df["Grade"].value_counts())

#====================== Task 2 ======================

low_attendance_marks=[
    marks
    for marks, attendance in zip(df["Marks"], df["Attendance"])
    if attendance < 75
]
print("=====================================================================================")
print(low_attendance_marks)

marks_list = df["Marks"].tolist()

high_marks=list(filter(lambda x: x>70, marks_list))
print("=====================================================================================")
print(high_marks)

print("=====================================================================================")
print("Total Students above 70:", len(high_marks))

marks_list=df["Marks"].tolist()

grace_marks=list(map(lambda x: min(x+5, 100), marks_list))
print("=====================================================================================")
print("Original Marks:", marks_list)
print("Grace Marks:", grace_marks)

#====================== Task 3 ======================

def summary(*values, round_to=2):
    if len(values) == 0:
        result = {
            "Count": 0,
            "Minimum": None,
            "Maximum": None,
            "Average": None
        }
    else:
        result = {
            "Count": len(values),
            "Minimum": min(values),
            "Maximum": max(values),
            "Average": round(sum(values) / len(values), round_to)
        }
    return result
    
print("=====================================================================================")
print(summary(10, 20, 30)) # Test Case 1
print(summary(*df["Marks"])) # Test Case 2

#====================== Task 4 ======================

df.to_csv("students.csv", index=False)

print("=====================================================================================")
print("CSV file saved successfully.")

def load_data(filename):
    try:
        data=pd.read_csv(filename)
        return data
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None
    except pd.errors.EmptyDataError:
        print(f"File '{filename}' is empty.")
        return None

students=load_data("students.csv")

if students is not None:
    print("=====================================================================================")
    print(students.head())

students2=load_data("wrongfile.csv")

#====================== Task 5 ======================

branch_stats = df.groupby("Branch")[["Marks", "Study_Hours"]].mean()
print("=====================================================================================")
print("Average Marks and Study Hours by Branch:\n", branch_stats)

highest_avg_branch = branch_stats["Marks"].idxmax()
print(f"\nBranch with the highest average marks: {highest_avg_branch}")

top_5_students = df.sort_values(by="Marks", ascending=False).head(5)
print("\nTop 5 students by marks:\n", top_5_students)

#====================== Task 6 ======================

marks_arr = df["Marks"].to_numpy()

mean_marks = np.mean(marks_arr)
std_marks = np.std(marks_arr, ddof=0) 
z_scores = (marks_arr - mean_marks) / std_marks
df["Z_Score"] = z_scores

z_gt_1_count = np.sum(z_scores > 1)
print("=====================================================================================")
print(f"Number of students with a z-score greater than 1: {z_gt_1_count}")

#====================== Task 7 ======================

mean_val = df["Marks"].mean()
median_val = df["Marks"].median()
mode_val = df["Marks"].mode()[0]
variance_val = df["Marks"].var()
std_val = df["Marks"].std()
min_val = df["Marks"].min()
max_val = df["Marks"].max()

print("=====================================================================================")
print(f"Mean: {mean_val:.2f}")
print(f"Median: {median_val}")
print(f"Mode: {mode_val}")
print(f"Variance: {variance_val:.2f}")
print(f"Standard Deviation: {std_val:.2f}")
print(f"Min: {min_val}, Max: {max_val}")

q1 = df["Marks"].quantile(0.25)
q3 = df["Marks"].quantile(0.75)
iqr = q3 - q1
lower_limit = q1 - 1.5 * iqr
upper_limit = q3 + 1.5 * iqr

outliers = df[(df["Marks"] < lower_limit) | (df["Marks"] > upper_limit)]["Marks"].tolist()

print("=====================================================================================")
print(f"\nQ1: {q1:.2f}, Q3: {q3:.2f}, IQR: {iqr:.2f}")
print(f"Lower Limit: {lower_limit:.2f}, Upper Limit: {upper_limit:.2f}")
print(f"Outliers found: {outliers if outliers else 'None'}")

print("\nExplanation (Mean, Median, Standard Deviation):")
print(
    f"The mean ({mean_val:.2f}) and median ({median_val}) provide central reference points showing "
    f"where the typical student's marks lie in the class. The standard deviation ({std_val:.2f}) indicates "
    f"the spread or variability of student performance around the average score."
)

#====================== Task 8 ======================

corr_study = df["Marks"].corr(df["Study_Hours"])
corr_attendance = df["Marks"].corr(df["Attendance"])

print("=====================================================================================")
print(f"Correlation between Marks and Study Hours: {corr_study:.4f}")
print(f"Correlation between Marks and Attendance: {corr_attendance:.4f}")

stronger_rel = "Study Hours" if abs(corr_study) > abs(corr_attendance) else "Attendance"
print(f"\nWhich relationship is stronger? {stronger_rel}")
print(
    "Explanation: The correlation with Study Hours is stronger and positive, "
    "meaning that students who study for more hours tend to score noticeably higher marks."
)
print(
    "Causation Note: High correlation shows a strong statistical relationship between two variables, "
    "but it does not prove causation because an unmeasured third factor (like prior capability or effort) "
    "could be driving both."
)

#====================== Task 9 ======================

ci_95 = stats.t.interval(
    confidence=0.95,
    df=len(df["Marks"]) - 1,
    loc=np.mean(df["Marks"]),
    scale=stats.sem(df["Marks"])
)

print("=====================================================================================")
print(f"95% Confidence Interval for average marks: ({ci_95[0]:.2f}, {ci_95[1]:.2f})")
print(
    f"Sentence Explanation: We are 95% confident that the true population mean of student marks "
    f"lies between {ci_95[0]:.2f} and {ci_95[1]:.2f}."
)

#====================== Task 10 ======================

t_stat_1, p_val_1 = stats.ttest_1samp(df["Marks"], 60)
print("=====================================================================================")
print(f"t-statistic: {t_stat_1:.4f}, p-value: {p_val_1:.4f}")

alpha = 0.05
if p_val_1 < alpha:
    print(f"Conclusion: Reject H0 (p-value = {p_val_1:.4f} < {alpha}). The claim that the average mark is 60 is not supported.")
else:
    print(f"Conclusion: Fail to reject H0 (p-value = {p_val_1:.4f} >= {alpha}). There is insufficient evidence to dispute the claim that the average mark is 60.")

#====================== Task 11 ======================

cse_marks = df[df["Branch"] == "CSE"]["Marks"]
ece_marks = df[df["Branch"] == "ECE"]["Marks"]

t_stat_2, p_val_2 = stats.ttest_ind(cse_marks, ece_marks)
print("=====================================================================================")
print(f"t-statistic: {t_stat_2:.4f}, p-value: {p_val_2:.4f}")

if p_val_2 < alpha:
    print(f"Conclusion: Reject H0 (p-value = {p_val_2:.4f} < {alpha}). There is a statistically significant difference between the average marks of CSE and ECE students.")
else:
    print(f"Conclusion: Fail to reject H0 (p-value = {p_val_2:.4f} >= {alpha}). There is no statistically significant difference between the average marks of CSE and ECE students at the 0.05 level.")

#====================== Task 12 ======================

summary_text = (
    "Summary:\n"
    "The statistical analysis reveals that student marks show moderate variability across branches with no extreme outliers detected.\n"
    "Both study hours and attendance share a positive linear relationship with overall performance.\n"
    "However, Study Hours demonstrates a considerably stronger positive correlation with marks compared to Attendance.\n"
    "Furthermore, hypothesis tests indicate no significant performance disparity between CSE and ECE branches.\n"
    "Overall, Study Hours appears to be the single most influential factor in determining student marks."
)
print("=====================================================================================")
print(summary_text,"\n")