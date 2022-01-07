import os; os.system("pip install requests")
import requests
import datetime

london = "https://www.metaweather.com/api/location/44418/"
sanfrancisco = "https://www.metaweather.com/api/location/2487956/"
paris = "https://www.metaweather.com/api/location/615702/"

city_list = [london, sanfrancisco, paris]

print("\n\n\n------------------------------------------------------------\n")
print("From which city would you like to have tomorrow's weather?\n")
print("1. London")
print("2. San Francisco")
print("3. Paris\n")
print("Your answer : ",end="")
city_number=input()

response = requests.get(city_list[int(city_number) - 1]).json()


def weather_forecast(my_dict):
  my_city = my_dict.get("title")
  
  tomorrow = str(datetime.date.today() + datetime.timedelta(days=1))
    
  for consolidated_weather_dict in my_dict.get("consolidated_weather"):
    if consolidated_weather_dict.get("applicable_date") == tomorrow:
      my_forecast = consolidated_weather_dict.get("weather_state_name")

  return f"\nThe weather in {my_city} tomorow is {my_forecast}"

print(weather_forecast(response))
