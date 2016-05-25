import requests
import pprint

cor_cities = {'Los Gatos':'Castle Rock', 'Berkeley':'Mortar and Indian Rock', 'Yosemite':'Yosemite', 'Sonora,us':'Columbia Boulders', 'Bolinas':'Stinson and Mickey\'s Beach', 'San Anslemo':'Mt. Tam', 'South Lake Tahoe':'Lake Tahoe', 'Monte Rio': 'Fort Ross'}
cities = ['Los Gatos', 'Berkeley', 'Yosemite', 'Sonora,us', 'Bolinas', 'San Anselmo', 'South Lake Tahoe', 'Monte Rio']
# give:
# City names
# option: 5 day

# information object
# name, temp, percip, humidity

def getInformationForCityName(cityName):
	# ...
	response = requests.get('http://api.openweathermap.org/data/2.5/forecast/daily?q={}&mode=json&units=imperial&cnt=7'.format(cityName))
	cityObj = response.json()
	return cityObj

def dayIndex():
	days_out = int(raw_input('\nIn how many days are you planning to climb? (Choose between 1 and 7 days). '))
	days_index = days_out - 1
	return days_index
   


def getDayinfo(totalcityinfo, daysout):
	return totalcityinfo['list'][daysout]

def getTemp(citydayinfo):
	return citydayinfo['temp']['day']

def getHumidity(citydayinfo):
	return citydayinfo['humidity']

def isRaining(citydayinfo):
	if citydayinfo['weather'][0]['main'] == 'Rain':
		return True
	else:
		return False

def CreateCityInsta(name, climbday):
 	info = getInformationForCityName(name)
 	dayinfo = getDayinfo(info, climbday)
 	cityTemp = getTemp(dayinfo)
 	cityHumid = getHumidity(dayinfo)
 	cityRain = isRaining(dayinfo)
 	return CityWeather(name, cityTemp, cityHumid, cityRain)


class CityWeather:
	def __init__(self, name, Temp, Humidity, Raining):
		self.name = name
		self.Temp = Temp
		self.Humidity = Humidity
		self.Raining = Raining


def CheckPref(CW,User):
	#x input will be instances of CityWeather class
	#y will be user preferences
	if CW.Temp - User.temp <= 8.0 or CW.Temp <= User.temp:
		if CW.Humidity <= User.humid:
			if CW.Raining == False:
				return True
			else:
				return False
		else:
			return False
	else:
		return False


def MatchList(city_data_list, userPref):
	return [x.name for x in city_data_list if CheckPref(x, userPref) == True]

'''def MatchListTest(city_data_list, userPref, climbnames):
	city_matches = [x.name for x in city_data_list if CheckPref(x, userPref) == True]
	actual_matches = [climbnames[x] for x in city_matches]
	print '\n'
	for places in actual_matches:
    	print places
    print '\nThe above areas fit your criteria.  Happy Climbing!'

#LG = CreateCityInsta('Los Gatos', 3)
#for x in cities:
#pprint.pprint(getInformationForCityName('Bolinas'))'''