
import  requests
from datetime import *



# For acquiring the temperature, the time of day is required.
# So from the DateTime library, the time of day
# can be achieved. But, specify just the hour is enough.
#By the two various approaches the time of day is gained.

# dataTime = datetime.now()
# print(dataTime)
# dataTimeS= str(dataTime)
# split1 = dataTimeS.split(' ')
# print(split1[1])
# split2 = split1[1].split(':')
# print(split2[0])

def request(hour):
    Url = "https://api.open-meteo.com/v1/forecast?latitude=-37.814&longitude=144.9633&hourly=temperature_2m&timezone=Australia%2FSydney&forecast_days=1"
    info = requests.get(Url)
    data = info.json()
    temps = data["hourly"]["temperature_2m"]
    return temps[hour]

def timeNow():
    dataTime = datetime.now()
    hourNow = dataTime.hour
    return hourNow

def liveWeather():
    hourNNow = timeNow()
    print(hourNNow)
    Url = "https://api.open-meteo.com/v1/forecast?latitude=-37.814&longitude=144.9633&hourly=temperature_2m&timezone=Australia%2FSydney&forecast_days=1"
    info = requests.get(Url)
    data = info.json()
    temps = data["hourly"]["temperature_2m"]
    tempNow = temps[hourNNow]
    # print(tempNow)
    return tempNow


