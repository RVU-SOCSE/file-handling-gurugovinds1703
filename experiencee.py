import pandas as pd

# Read CSV file
df = pd.read_csv("experience.csv")

# 1. Display content of the file
print("===== FILE CONTENT =====")
print(df)

# 2. Total number of rows and columns
print("\n===== SHAPE =====")
print("Rows and Columns:", df.shape)

# 3. Length of dataframe
print("\n===== LENGTH =====")
print("Number of rows:", len(df))

# 4. Display first 2 rows
print("\n===== FIRST 2 ROWS =====")
print(df.head(2))
