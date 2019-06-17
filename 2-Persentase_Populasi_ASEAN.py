# 2. Persentase Populasi ASEAN

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

plt.figure('ASEAN Figures', figsize = (13,9))
plt.pie(df['Populasi_Negara'], labels = df['Negara_ASEAN'], autopct='%1.1f%%', textprops={'color': 'black'})
plt.title('Persentase Penduduk ASEAN')

plt.show()