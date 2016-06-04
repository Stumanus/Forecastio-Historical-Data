import json
import csv
import forecastio
import pprint
import time
import datetime
import requests


api_key = '4380a8f198376852eff141666cdc8671'

locations = ['Bullhead_City', 'Casa_Grande', 'Safford', 'Sierra_Vista', 'Tucson', 'Roseville']

lats = [35.1359386, 32.8795022, 32.8339546, 31.5455001, 32.2217429, 38.7521235]

longs = [-114.52859810000001, -111.75735209999999, -109.70758000000001, -110.27728560000003, -110.92647899999997, -121.28800590000003]

#variable for current time'''
now = datetime.datetime.now()
ForecastTime = now.strftime("[%Y]-[%m]-[%d]T[%H]:[%M]:[%S]")


#Set date range for download of historical hourly data from current day backwards'''

a = datetime.datetime.today() - datetime.timedelta(1)
numdays = 15 #number of days to pull

#Create list of dates to pass to function '''
datelist = []
time_machine_dates = []
for x in range(0, numdays):
    datelist.append(a - datetime.timedelta(days = x))
for z in datelist:
    time_machine_dates.append(z.strftime("%Y-%m-%dT%H:%M:%S"))

#loop through locations and dates, append temperatures to list '''

temps = []

for i in range(len(locations)):
    for dates in time_machine_dates:
        forecast_url = 'https://api.forecast.io/forecast/%s/%s,%s,%s' % (api_key, lats[i], longs[i], dates)
        forecast = requests.get(forecast_url)
        data = forecast.json()
        byHour = data['hourly']['data']

        for hourlydata in byHour:
            try:
                temps.append({
                    'Time':time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(hourlydata['time'])),
                    'Location': locations[i],
                    'Temp': hourlydata['temperature'],
                     })

            except:
                print("Well shit..")
                pass
print("Current Time:" + ForecastTime)
pprint.pprint(time_machine_dates)
pprint.pprint(temps)

