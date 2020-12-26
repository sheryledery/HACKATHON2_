import tkinter as tk
from tkinter import *
from tkinter import ttk
import requests
# HEIGHT = 700	
# WIDTH = 800
# def test_function(entry):
# 	print('this is the entry:', entry)
def format_response(weather): 	
	name = weather['name']
	desc = weather['weather'][0]['description']
	temp = weather['main']['temp']
	feels_like = weather['main']['feels_like']
	return  'City: %s \nConditions: %s \nTemperature (°C ): %s \nFeels Like (°C ): %s' % (name, desc, temp, feels_like)
def get_weather(city):
		weather_key = '40dec8cb79f0eab5af5e81835ddbbde0'
		url = 'https://api.openweathermap.org/data/2.5/weather'
		params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
		response = requests.get(url, params=params)
		weather = response.json()
		label['text']= format_response(weather)
	# PRINT IN TERMINAL TO TEST
	
		# print(weather['name'])
		# print(weather['weather'][0]['description'])
		# print(weather['main']['temp'])
		# print(weather['main']['feels_like'])
main = tk.Tk()
main.title("Weather App")
main.geometry("510x200")
main.resizable(width=True, height=True)
main.configure(bg="#898C8A")
# API 40dec8cb79f0eab5af5e81835ddbbde0
# api.openweathermap.org/data/2.5/forecast?q={city name}&appid={API key}
# background_image = tk.PhotoImage(file='unnamed.jpg')
# background_label = tk.Label(main, image= background_image)
# background_label.place(relwidth=1, relheight=1)
frame = tk.Frame(main, bg ='#2E9CB3', bd=5)
frame.place(relx=0.5, rely= 0.1, relwidth= 0.75, relheight= 0.1, anchor='n')
entry = tk.Entry(frame, font= 50 )
entry.place(relwidth=0.65, relheight=1)
button = tk.Button(frame, text='Find Forecast', font= 60, command= lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)
lower_frame = tk.Frame(main, bg='#2E9CB3', bd=10)
lower_frame.place(relx=0.5, rely= 0.25, relwidth= 0.75, relheight= 0.6, anchor='n')
label = tk.Label(lower_frame)
label.place(relwidth= 1, relheight=1)
main.mainloop()
