import requests
from pprint import pprint
import datetime

url = 'https://disease.sh/v3/covid-19/countries/mayotte?strict=true'

resp = requests.get(url=url)
data = resp.json()  # Check the JSON Response Content documentation below

updated = data.get("updated")
_updated_datetime = datetime.datetime.fromtimestamp(float(updated/1000))
nb_active = data.get("active")
nb_deaths = data.get("deaths")
nb_recovered = data.get("recovered")
nb_tests = data.get("tests")
population = data.get("population")
updated_datetime_time = _updated_datetime.strftime('%H:%M:%S')
updated_datetime_date = _updated_datetime.strftime('%d/%m/%Y')
# pprint([updated_datetime_time,
#     updated_datetime_date,
#     nb_active/population*100,
#     nb_deaths/population*100,
#     nb_recovered/population*100,
#     population])

res_string = "Bot stats COVID Mayotte\n\
Nb cas positifs : {positifs:,}.\n\
Nb décès : {deces:,}.\n\
Nb guéris : {gueris:,}.\n\
Nb tests réalisés : {testees:,}.\n\
Nb hbts : {hbts:,}.\n\n\
MAJ le {date} à {heure} (UTC+0300).\nhttps://disease.sh/\n\n\n\
#covid #coronavirus #corona #mayotte #france #mahorais\
".format(positifs=nb_active,
         p_positifs=nb_active/population,
         deces=nb_deaths,
         p_deces=nb_deaths/population,
         gueris=nb_recovered,
         p_gueris=nb_recovered/population,
         testees=nb_tests,
         hbts=population,
         date=updated_datetime_date,
         heure=updated_datetime_time).replace(',', ' ')

# print(res_string)