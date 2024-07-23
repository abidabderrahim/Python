import pandas as pd

link = str(input("Enter Website URL : "))

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

tables = pd.read_html(link)
for i, table in enumerate(tables):
    print(f"Table {i + 1}:\n{table}\n")
