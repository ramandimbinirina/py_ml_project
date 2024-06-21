import pandas as pd

# Read the CSV file
csv_file_path = './files/e.csv'
df = pd.read_csv(csv_file_path)

# Save as XLS file
xls_file_path = './e.xlsx'
df.to_excel(xls_file_path, index=False)
