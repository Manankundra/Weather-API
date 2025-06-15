import requests
import matplotlib.pyplot as plt
import numpy as np 

Api_key = 'd69af6d5645feb2af53d4e844cb6b15f'
cities = ["Mumbai", "Delhi", "Kolkata", "Chennai", "Goa"]

temps = []
feels_like = []
humidity = []

for city in cities:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={Api_key}&units=metric"
    data = requests.get(url).json()
    temps.append(data['main']['temp'])
    feels_like.append(data['main']['feels_like'])
    humidity.append(data['main']['humidity'])


plt.style.use('classic')

# Plot temperature comparison
plt.figure(figsize=(10, 5))
plt.bar(cities, temps, color='skyblue', label="Actual Temp")
plt.bar(cities, feels_like, color='orange', alpha=0.5, label="Feels Like")
plt.title("Temperature vs Feels Like in Cities")
plt.xlabel("Cities")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot humidity
plt.figure(figsize=(10, 5))
plt.bar(cities, humidity, color='green')
plt.title("Humidity Levels in Cities")
plt.xlabel("Cities")
plt.ylabel("Humidity (%)")
plt.grid(True)
plt.tight_layout()
plt.show()
