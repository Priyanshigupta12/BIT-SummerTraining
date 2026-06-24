import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



### Question 1: Set a Theme
sns.set_theme(style="whitegrid")

student_data = {
    "name": ["Aman", "Priya", "Shalu", "Raj", "Ansh", "Neha", "Vivek", "Riya"],
    "course": ["Python", "Python", "Data Analytics", "Data Analytics", "AI", "AI", "Python", "Data Analytics"],
    "study_hours": [2, 4, 3, 5, 6, 4, 3, 5],
    "marks": [55, 78, 68, 88, 92, 82, 70, 90],
    "attendance": [72, 85, 80, 92, 95, 88, 78, 90]
}

df = pd.DataFrame(student_data)


### Question 2: Count Plot
sns.set_theme(style="whitegrid")
sns.countplot(data=df,x="course")
plt.title("Students by Course")
plt.savefig("course_count.png")
plt.show()


## Question 3: Bar Plot
sns.set_theme(style="whitegrid")
avg=df.groupby("course")["marks"].mean().reset_index()
sns.barplot(data=avg ,x="course",y="marks")
plt.title("Average Marks by Course")
plt.savefig("average_marks_bar.png")
plt.show()


## Question 4: Scatter Plot
sns.set_theme(style="whitegrid")
sns.scatterplot(data=df,x="study_hours",y="marks",hue="course")
plt.title("Study Hours vs Marks")
plt.savefig("study_hours_marks_scatter.png")
plt.show()



## Question 5: Box Plot
sns.set_theme(style="whitegrid")
sns.boxplot(data=df,x="course",y="marks")
plt.title("Marks Distribution by Course")
plt.savefig("marks_boxplot.png")
plt.show()




## Question 6: Histogram
sns.set_theme(style="whitegrid")
sns.histplot(
    data=df,
    x="marks",
    kde=True
)
plt.title("Marks Distribution")
plt.savefig("marks_histogram.png")
plt.show()


## Question 7: Correlation Heatmap
sns.set_theme(style="whitegrid")
corr_matrix = df[["study_hours", "marks", "attendance"]].corr()
sns.heatmap(corr_matrix,annot=True)
plt.title("Student Metrics Correlation")
plt.savefig("student_correlation_heatmap.png")
plt.show()


### Question 8: Best Performing Course
best=df.groupby("course")["marks"].mean().idxmax()
print("Best performing course:", best)