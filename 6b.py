import pandas as pd

# Reading the CSV file
df_csv = pd.read_csv("ODI data.csv")
print("CSV DataFrame:")
print(df_csv)

# Reading the Excel file
df_excel = pd.read_excel("Cars.xlsx")
print("\nExcel DataFrame:")
print(df_excel)
