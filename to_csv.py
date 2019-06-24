import pandas as pd

path = "data/Poisson_data_cleaned_06212019.xlsx"

data_xls = pd.read_excel(path, index_col=None)
data_xls.to_csv('Poisson_data_cleaned_06212019.csv', encoding='utf-8',header = None,index = False)
