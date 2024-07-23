import pandas as pd

link = str(input("Enter Your Link : "))
csv_data = pd.read_csv(link)
print(f"{csv_data}")
