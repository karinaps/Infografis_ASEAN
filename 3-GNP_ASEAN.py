# 3. GNP ASEAN

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

plt.figure('ASEAN Figures', figsize = (12,8))
plt.bar(df['Negara_ASEAN'], df['GNP'], color = colors)
plt.title('Pendapatan Bruto Nasional Negara ASEAN')
plt.xlabel('Negara')
plt.ylabel('Gross National Product (US$)')
plt.grid(True)

for i in range(len(df)):
    plt.text(df['Negara_ASEAN'][i], df['GNP'][i] + 1000, df['GNP'][i])

plt.show()

