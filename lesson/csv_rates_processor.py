import pandas as pd


# DataFrame object
data = pd.read_csv("Official_exchange.csv", sep=';', skiprows=2, skipfooter=3, engine='python')


def fixComma(value):
    return float(value.replace(',', '.'))


data['Cursul'] = data["Cursul"].map(fixComma)
for i, r in data.iterrows():
    data['Cursul'][i] = r['Cursul'] / r['Rata']
    data['Rata'][i] = 1


data = data.sort_values('Cursul', ascending=False)
print(data[0:4])
data[0:4].to_csv("./processed.csv", sep=';')