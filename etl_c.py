# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import datetime as datetime
import pandas as pd
#import matplotlib.pyplot as plt
from influxdb import InfluxDBClient


query = 'SELECT * FROM "val1" WHERE time >= now() - 90d ; '
query1 = 'SELECT * FROM "val2" WHERE time >= now() - 90d ; '
query2 = 'SELECT * FROM "val3" WHERE time >= now() - 90d ; '
query3 = 'SELECT * FROM "val4" WHERE time >= now() - 90d ; '
query4 = 'SELECT * FROM "val5" WHERE time >= now() - 90d ; '
query5 = 'SELECT * FROM "val6" WHERE time >= now() - 90d ; '
query6 = 'SELECT * FROM "val7" WHERE time >= now() - 90d ; '
query7 = 'SELECT * FROM "val8" WHERE time >= now() - 90d ; '
query8 = 'SELECT * FROM "val9" WHERE time >= now() - 90d ; '
query9 = 'SELECT * FROM "val10" WHERE time >= now() - 90d ; '
query10 = 'SELECT * FROM "val11" WHERE time >= now() - 90d ; '
query11 = 'SELECT * FROM "val12" WHERE time >= now() - 90d ; '

query12 = 'SELECT * FROM "val_on_1" WHERE time >= now() - 90d ; '
query13 = 'SELECT * FROM "val_on_2" WHERE time >= now() - 90d ; '
query14 = 'SELECT * FROM "val_on_3" WHERE time >= now() - 90d ; '
query15 = 'SELECT * FROM "val_on_4" WHERE time >= now() - 90d ; '
query16 = 'SELECT * FROM "val_on_5" WHERE time >= now() - 90d ; '
query17 = 'SELECT * FROM "val_on_6" WHERE time >= now() - 90d ; '
query18 = 'SELECT * FROM "val_on_7" WHERE time >= now() - 90d ; '
query19 = 'SELECT * FROM "val_on_8" WHERE time >= now() - 90d ; '
query20 = 'SELECT * FROM "val_on_9" WHERE time >= now() - 90d ; '
query21 = 'SELECT * FROM "val_on_10" WHERE time >= now() - 90d ; '
query22 = 'SELECT * FROM "val_on_11" WHERE time >= now() - 90d ; '
query23 = 'SELECT * FROM "val_on_12" WHERE time >= now() - 90d ; '

query24 = 'SELECT * FROM "mean_1" WHERE time >= now() - 90d ; '
query25 = 'SELECT * FROM "mean_2" WHERE time >= now() - 90d ; '
query26 = 'SELECT * FROM "mean_3" WHERE time >= now() - 90d ; '
query27 = 'SELECT * FROM "mean_4" WHERE time >= now() - 90d ; '
query28 = 'SELECT * FROM "cv_1" WHERE time >= now() - 90d ; '
query29 = 'SELECT * FROM "cv_2" WHERE time >= now() - 90d ; '
query30 = 'SELECT * FROM "cv_3" WHERE time >= now() - 90d ; '
query31 = 'SELECT * FROM "cv_4" WHERE time >= now() - 90d ; '

client = InfluxDBClient('localhost', 8086, database='esp_32_v3')

result = client.query(query)
result1 = client.query(query1)
result2 = client.query(query2)
result3 = client.query(query3)
result4 = client.query(query4)
result5 = client.query(query5)
result6 = client.query(query6)
result7 = client.query(query7)
result8 = client.query(query8)
result9 = client.query(query9)
result10 = client.query(query10)
result11 = client.query(query11)
result12 = client.query(query12)
result13 = client.query(query13)
result14 = client.query(query14)
result15 = client.query(query15)
result16 = client.query(query16)
result17 = client.query(query17)
result18 = client.query(query18)
result19 = client.query(query19)
result20 = client.query(query20)
result21 = client.query(query21)
result22 = client.query(query22)
result23 = client.query(query23)
result24 = client.query(query24)
result25 = client.query(query25)
result26 = client.query(query26)
result27 = client.query(query27)
result28 = client.query(query28)
result29 = client.query(query29)
result30 = client.query(query30)
result31 = client.query(query31)

#print("Result: {0}".format(result))
points = result.get_points()
points1 = result1.get_points()
points2 = result2.get_points()
points3 = result3.get_points()
points4 = result4.get_points()
points5 = result5.get_points()
points6 = result6.get_points()
points7 = result7.get_points()
points8 = result8.get_points()
points9 = result9.get_points()
points10 = result10.get_points()
points11 = result11.get_points()
points12 = result12.get_points()
points13 = result13.get_points()
points14 = result14.get_points()
points15 = result15.get_points()
points16 = result16.get_points()
points17 = result17.get_points()
points18 = result18.get_points()
points19 = result19.get_points()
points20 = result20.get_points()
points21 = result21.get_points()
points22 = result22.get_points()
points23 = result23.get_points()
points24 = result24.get_points()
points25 = result25.get_points()
points26 = result26.get_points()
points27 = result27.get_points()
points28 = result28.get_points()
points29 = result29.get_points()
points30 = result30.get_points()
points31 = result31.get_points()

dfs = pd.DataFrame(points)
dfs['time'] = pd.to_datetime(dfs['time'], errors='coerce')
dfs.set_index('time', inplace=True)
dfs = dfs.resample('30T').mean()

dfs1 = pd.DataFrame(points1)
dfs1['time'] = pd.to_datetime(dfs1['time'], errors='coerce')
dfs1.set_index('time', inplace=True)
dfs1 = dfs1.resample('30T').mean()

dfs2 = pd.DataFrame(points2)
dfs2['time'] = pd.to_datetime(dfs2['time'], errors='coerce')
dfs2.set_index('time', inplace=True)
dfs2 = dfs2.resample('30T').mean()

dfs3 = pd.DataFrame(points3)
dfs3['time'] = pd.to_datetime(dfs3['time'], errors='coerce')
dfs3.set_index('time', inplace=True)
dfs3 = dfs3.resample('30T').mean()

dfs4 = pd.DataFrame(points4)
dfs4['time'] = pd.to_datetime(dfs4['time'], errors='coerce')
dfs4.set_index('time', inplace=True)
dfs4 = dfs4.resample('30T').mean()

dfs5 = pd.DataFrame(points5)
dfs5['time'] = pd.to_datetime(dfs5['time'], errors='coerce')
dfs5.set_index('time', inplace=True)
dfs5 = dfs5.resample('30T').mean()

dfs6 = pd.DataFrame(points6)
dfs6['time'] = pd.to_datetime(dfs6['time'], errors='coerce')
dfs6.set_index('time', inplace=True)
dfs6 = dfs6.resample('30T').mean()

dfs7 = pd.DataFrame(points7)
dfs7['time'] = pd.to_datetime(dfs7['time'], errors='coerce')
dfs7.set_index('time', inplace=True)
dfs7 = dfs7.resample('30T').mean()

dfs8 = pd.DataFrame(points8)
dfs8['time'] = pd.to_datetime(dfs8['time'], errors='coerce')
dfs8.set_index('time', inplace=True)
dfs8 = dfs3.resample('30T').mean()

dfs9 = pd.DataFrame(points9)
dfs9['time'] = pd.to_datetime(dfs9['time'], errors='coerce')
dfs9.set_index('time', inplace=True)
dfs9 = dfs9.resample('30T').mean()

dfs10 = pd.DataFrame(points10)
dfs10['time'] = pd.to_datetime(dfs10['time'], errors='coerce')
dfs10.set_index('time', inplace=True)
dfs10 = dfs10.resample('30T').mean()

dfs11 = pd.DataFrame(points11)
dfs11['time'] = pd.to_datetime(dfs11['time'], errors='coerce')
dfs11.set_index('time', inplace=True)
dfs11 = dfs11.resample('30T').mean()

dfs12 = pd.DataFrame(points12)
dfs12['time'] = pd.to_datetime(dfs12['time'], errors='coerce')
dfs12.set_index('time', inplace=True)
dfs12 = dfs12.resample('30T').mean()

dfs13 = pd.DataFrame(points13)
dfs13['time'] = pd.to_datetime(dfs13['time'], errors='coerce')
dfs13.set_index('time', inplace=True)
dfs13 = dfs13.resample('30T').mean()

dfs14 = pd.DataFrame(points14)
dfs14['time'] = pd.to_datetime(dfs14['time'], errors='coerce')
dfs14.set_index('time', inplace=True)
dfs14 = dfs14.resample('30T').mean()

dfs15 = pd.DataFrame(points15)
dfs15['time'] = pd.to_datetime(dfs15['time'], errors='coerce')
dfs15.set_index('time', inplace=True)
dfs15 = dfs15.resample('30T').mean()

dfs16 = pd.DataFrame(points16)
dfs16['time'] = pd.to_datetime(dfs16['time'], errors='coerce')
dfs16.set_index('time', inplace=True)
dfs16 = dfs16.resample('30T').mean()

dfs17 = pd.DataFrame(points17)
dfs17['time'] = pd.to_datetime(dfs17['time'], errors='coerce')
dfs17.set_index('time', inplace=True)
dfs17 = dfs17.resample('30T').mean()

dfs18 = pd.DataFrame(points18)
dfs18['time'] = pd.to_datetime(dfs18['time'], errors='coerce')
dfs18.set_index('time', inplace=True)
dfs18 = dfs18.resample('30T').mean()

dfs19 = pd.DataFrame(points19)
dfs19['time'] = pd.to_datetime(dfs19['time'], errors='coerce')
dfs19.set_index('time', inplace=True)
dfs19 = dfs19.resample('30T').mean()

dfs20 = pd.DataFrame(points20)
dfs20['time'] = pd.to_datetime(dfs20['time'], errors='coerce')
dfs20.set_index('time', inplace=True)
dfs20 = dfs20.resample('30T').mean()

dfs21 = pd.DataFrame(points21)
dfs21['time'] = pd.to_datetime(dfs21['time'], errors='coerce')
dfs21.set_index('time', inplace=True)
dfs21 = dfs21.resample('30T').mean()

dfs22 = pd.DataFrame(points22)
dfs22['time'] = pd.to_datetime(dfs22['time'], errors='coerce')
dfs22.set_index('time', inplace=True)
dfs22 = dfs22.resample('30T').mean()

dfs23 = pd.DataFrame(points23)
dfs23['time'] = pd.to_datetime(dfs23['time'], errors='coerce')
dfs23.set_index('time', inplace=True)
dfs23 = dfs23.resample('30T').mean()

dfs24 = pd.DataFrame(points24)
dfs24['time'] = pd.to_datetime(dfs24['time'], errors='coerce')
dfs24.set_index('time', inplace=True)
dfs24 = dfs24.resample('30T').mean()

dfs25 = pd.DataFrame(points25)
dfs25['time'] = pd.to_datetime(dfs25['time'], errors='coerce')
dfs25.set_index('time', inplace=True)
dfs25 = dfs25.resample('30T').mean()

dfs26 = pd.DataFrame(points26)
dfs26['time'] = pd.to_datetime(dfs26['time'], errors='coerce')
dfs26.set_index('time', inplace=True)
dfs26 = dfs26.resample('30T').mean()

dfs27 = pd.DataFrame(points27)
dfs27['time'] = pd.to_datetime(dfs27['time'], errors='coerce')
dfs27.set_index('time', inplace=True)
dfs27 = dfs27.resample('30T').mean()

dfs28 = pd.DataFrame(points28)
dfs28['time'] = pd.to_datetime(dfs28['time'], errors='coerce')
dfs28.set_index('time', inplace=True)
dfs28 = dfs28.resample('30T').mean()

dfs29 = pd.DataFrame(points29)
dfs29['time'] = pd.to_datetime(dfs29['time'], errors='coerce')
dfs29.set_index('time', inplace=True)
dfs29 = dfs29.resample('30T').mean()

dfs30 = pd.DataFrame(points30)
dfs30['time'] = pd.to_datetime(dfs30['time'], errors='coerce')
dfs30.set_index('time', inplace=True)
dfs30 = dfs30.resample('30T').mean()

dfs31 = pd.DataFrame(points31)
dfs31['time'] = pd.to_datetime(dfs31['time'], errors='coerce')
dfs31.set_index('time', inplace=True)
dfs31 = dfs31.resample('30T').mean()

dfs = dfs.merge(dfs1, how='inner', on='time').merge(dfs2, how='inner', on='time').merge(dfs3, how='inner', on='time').merge(dfs4, how='inner', on='time').merge(dfs5, how='inner', on='time').merge(dfs6, how='inner', on='time').merge(dfs7, how='inner', on='time').merge(dfs8, how='inner', on='time').merge(dfs9, how='inner', on='time').merge(dfs10, how='inner', on='time').merge(dfs11, how='inner', on='time').merge(dfs12, how='inner', on='time').merge(dfs13, how='inner', on='time').merge(
    dfs14, how='inner', on='time').merge(dfs15, how='inner', on='time').merge(dfs16, how='inner', on='time').merge(dfs17, how='inner', on='time').merge(dfs18, how='inner', on='time').merge(dfs19, how='inner', on='time').merge(dfs20, how='inner', on='time').merge(dfs21, how='inner', on='time').merge(dfs22, how='inner', on='time').merge(dfs23, how='inner', on='time').merge(dfs24, how='inner', on='time').merge(dfs25, how='inner', on='time').merge(dfs26, how='inner', on='time').merge(dfs27, how='inner', on='time').merge(dfs28, how='inner', on='time').merge(dfs29, how='inner', on='time').merge(dfs30, how='inner', on='time').merge(dfs31, how='inner', on='time').merge(dfs27, how='inner', on='time')
dfs.set_axis(['Sensor(1)', 'Sensor(2)', 'Sensor(3)', 'Sensor(4)', 'Sensor(5)', 'Sensor(6)', 'Sensor(7)', 'Sensor(8)', 'Sensor(9)', 'Sensor(10)', 'Sensor(11)', 'Sensor(12)', 'water(1)',
              'water(2)', 'water(3)', 'water(4)', 'water(5)', 'water(6)', 'water(7)', 'water(8)', 'water(9)', 'water(10)', 'water(11)', 'water(12)', 'mean(1)', 'mean(2)', 'mean(3)', 'mean(4)', 'cv_1', 'cv_2', 'cv_3', 'cv_4'], axis=1)
print(dfs)

#ax=dfs['Sensor(1)'].plot()
#ax=dfs['Sensor(2)'].plot()

#plt.legend(loc='upper left')
#ax.set_ylabel("Soil moisture")

dfs.to_csv("/home/pi/Documents/proto/Csv/proto.csv")
