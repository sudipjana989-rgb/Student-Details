import pandas as pd

data = {
    "Name": ["Rahul", "Priya", "Amit"],
    "Python": [85, 92, 45],
    "Math": [78, 88, 50]
}

df = pd.DataFrame(data)

df["Total"] = df["Python"] + df["Math"]
df["Average"] = df[["Python", "Math"]].mean(axis=1)

print("Student Performance Analysis")
print(df)

print("\nTopper:")
print(df.loc[df["Total"].idxmax()])
