# 1. Populasi ASEAN

import pandas as pd
import sqlalchemy
import matplotlib.pyplot as plt
import seaborn as sb

sb.set(style = 'darkgrid')

mydb = sqlalchemy.create_engine(
    'mysql+pymysql://karinaps:Kimtaehyung1809@localhost:3306/world'
)
query = 'select * from asean'
df = pd.read_sql(query, mydb)

colors = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'gray', 'yellow', 'pink', 'black', 'darkblue']

plt.figure('ASEAN Figures', figsize = (13,9))
plt.bar(df['Negara_ASEAN'], df['Populasi_Negara'], color = colors)
plt.title('Populasi Negara ASEAN')
plt.xlabel('Negara')
plt.ylabel('Populasi (x100jt jiwa')
plt.grid(True)

for j in range(len(df)):
    plt.text(df['Negara_ASEAN'][j], df['Populasi_Negara'][j] + 1000000, df['Populasi_Negara'][j])

plt.show()