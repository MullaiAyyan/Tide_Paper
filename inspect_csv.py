import pandas as pd

# Load merged CSV
df = pd.read_csv(r"C:\Users\Mulla\Downloads\MSI_Cube_Cuddalore_HLS_All.csv")

# Inspect the data
print("Shape:", df.shape)       # rows, columns
print("Columns:", df.columns)   # column names
print(df.head())                # first 5 rows
