import pandas as pd
import numpy  as np
from matplotlib import pyplot as plt

election_list = []

for line in open("ELECTION-ID"):
    a = line.split()
    year = a[0]+".csv"

    header = pd.read_csv(year, nrows = 1).dropna(axis = 1)
    d = header.iloc[0].to_dict()

    df = pd.read_csv(year, index_col = 0, thousands = ",", skiprows = [1])

    df.dropna(inplace = True, axis = 1)
    df.rename(inplace = True, columns = d)
    df["Year"] = a[0]
    election_list.append(df[["Democratic", "Republican", "Total Votes Cast", "Year"]])

merged = pd.concat(election_list)
merged["Republican Share"] = merged["Republican"]/merged["Total Votes Cast"]
only_accomack = merged.loc['Accomack County'].sort_values(by = 'Year', ascending = True)

final = only_accomack.plot(kind = "line", x = "Year", y = "Republican Share")
final.get_figure().savefig('accomack.png', bbox_inches='tight')
