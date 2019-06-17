# 4. Persentase Luas Daratan ASEAN

import pandas as pd
import sqlalchemy
import matplotlib.pyplot as plt
import seaborn as sb

sb.set(style = 'darkgrid')

mydb = sqlalchemy.create_engine(
    'mysql+pymysql://karinaps:Kimtaehyung1809@localhost:3306/world'
)
query = 'select * from country'
df = pd.read_sql(query, mydb)
df = df[df['Region'] == 'Southeast Asia'].reset_index()

plt.figure('ASEAN Figures', figsize = (13,9))
plt.pie(df['SurfaceArea'], labels = df['Name'], autopct='%1.1f%%', textprops={'color': 'black'})
plt.title('Persentase Luas Daratan ASEAN')

plt.show()