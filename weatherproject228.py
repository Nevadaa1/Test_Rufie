import tkinter as tk
import requests as rq
apik="e9091c7b53e643ea41bffc394402b920"
def search():
    city = city_entry.get()
    weather = getweather(city)
    locationlabel["text"]=f"{weather[0]}, {weather[1]}"
    img["file"]=f"weather_icons/{weather[3]}.png"
    weatherlabel["text"]=f"{weather[4]}"
    templabel["text"]=f"temperature: {weather[2]:.0f}C"
def getweather(city):
    url=f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apik}'
    respons = rq.get(url)
    data = respons.json()
    city = data["name"]
    country = data["sys"]["country"]
    temp=data["main"]["temp"]-273.15
    icon=data["weather"][0]["icon"]
    weather = data["weather"][0]["main"]
    final = (city, country, temp, icon, weather)
    return final
#Hello Git
window = tk.Tk()
window.title("weather")
window.geometry("300x300")

city_entry=tk.Entry(window, font=14, width=300, justify="center")
city_entry.pack()
locationlabel=tk.Label(window, text = "город", font = ("bold", 20) )
locationlabel.pack()
img = tk.PhotoImage(file="")
weatherimage = tk.Label(window, image=img)
weatherimage.pack()
weatherlabel =tk.Label(window, text="pogoda", font = 11)
weatherlabel.pack()
templabel =tk.Label(window, text="temp", font = 11)
templabel.pack()
searchbutton=tk.Button(window, text="поиск погоды", font = 16, command=search)
searchbutton.pack()















window.mainloop()
