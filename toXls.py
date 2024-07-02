import pandas as pd

# Read the CSV file
csv_file_path = './files/star_classification.csv'
df = pd.read_csv(csv_file_path)

# Save as XLS file
xls_file_path = './star_classification.xlsx'
df.to_excel(xls_file_path, index=False)
