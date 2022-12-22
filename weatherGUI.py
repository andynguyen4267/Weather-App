import tkinter as tk
from tkinter import messagebox
import requests, json

class WeatherGUI:

    def __init__(self):
        self.api_key = "8c34baaea73542a67c5720f6a4796ce7"
        self.api_url = "http://api.openweathermap.org/data/2.5/weather"
        self.temp = self.temp_min = self.temp_max = self.weather = self.all = None
        self.zipcode = None

        self.root = tk.Tk()
        self.root.geometry("200x200")

        # title of applications
        self.title = tk.Label(text="Weather App", bg="blue", fg="white", font=("Helvetica", 16, "bold"))
        self.title.grid(row=0, column=0)
        
        # enter zipcode label
        self.zipcode_label = tk.Label(text="Enter zipcode:")
        self.zipcode_label.grid(row=2, column=0)
        
        # user entry field
        self.user_entry = tk.Entry()
        self.user_entry.grid(row=4, column=0)

        # confirm user entry button
        self.ok_entry_button = tk.Button(text="OK", command=self.on_button_click)
        self.ok_entry_button.grid(row=6, column=0)

        # exit application button
        self.exit_button = tk.Button(text="Close", command=self.root.quit)
        self.exit_button.grid(row=16, column=0)


    def on_button_click(self):
        self.zipcode = self.user_entry.get()

        try:
            self.getWeather()
            
            self.user_entry.destroy()
            self.zipcode_label.destroy()
            
            self.temp_label = tk.Label(self.root, text="Temperature: {:0.0f}".format(self.temp) + u'\N{DEGREE SIGN}' + "F")
            self.temp_label.grid(row=1, column=0)
            

            self.weather_label = tk.Label(self.root, text="Weather: {}".format(self.weather))
            self.weather_label.grid(row=2, column=0)
        except:
            messagebox.showerror("Invalid Zipcode", "Please Enter a Valid Zipcode.")

        
    def start(self):
        self.root.mainloop()

    def getWeather(self):
        URL = self.api_url + "?zip=" + self.zipcode + ",us&appid=" + self.api_key
        response = requests.get(URL)
        json_data = response.json()
        
        self.all = json_data
        self.weather = json_data["weather"][0]["main"]
        
        main_data = json_data["main"]
        self.temp = main_data["temp"]
        self.temp = (((self.temp - 273.15) * 9) / 5) + 32

gui = WeatherGUI()
gui.start()