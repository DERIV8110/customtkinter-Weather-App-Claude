import customtkinter
from tkinter import *
import ttkbootstrap as ttk
import json                            #only for pretty printing
import requests
from datetime import datetime
from tkinter import messagebox

home = customtkinter.CTk()
home.geometry("500x300")

frame = ttk.Frame(home)
frame.grid(row=0, column=0)
home.grid_rowconfigure(0, weight=2)
home.grid_rowconfigure(1, weight=2)
home.grid_rowconfigure(2, weight=1)
home.grid_rowconfigure(3, weight=1)
home.grid_rowconfigure(4, weight=1)

home.grid_columnconfigure(0, weight=1)
home.grid_columnconfigure(1, weight=1)
home.grid_columnconfigure(2, weight=1)
home.grid_columnconfigure(3, weight=1)

now = datetime.now()

date_label = customtkinter.CTkLabel(home,text=now.strftime("%d %B %Y"))
date_label.grid(row=0,column=0)

day_label = customtkinter.CTkLabel(home,text=now.strftime("%A"))
day_label.grid(row=0,column=3)

search_label = customtkinter.CTkLabel(home,text="Enter Location")
search_label.grid(row=1,column=0)

entry = customtkinter.CTkEntry(home, placeholder_text="First letter Uppercase",width=150)
entry.grid(row=1,column=3)

def fetch_data():
       get_location = entry.get()
       if get_location == "":
              messagebox.showerror("Error","Please enter a valid region")
       else:
              url_geocoding = f"https://geocoding-api.open-meteo.com/v1/search?name={get_location}&count=10&language=en&format=json"
              response1 = requests.get(url_geocoding)
              sdata1 = response1.json()
              print("city data:",sdata1["results"][0])
              latitude = sdata1["results"][0]["latitude"]
              longitude = sdata1["results"][0]["longitude"]


              #url consists of url of website from documentation on website then symbol and token(api key)
              url_lat_lon = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m"
              response2 = requests.get(url_lat_lon)
              sdata2 = response2.json()
              print("temp data:",sdata2)

              show_loc_label = customtkinter.CTkLabel(home,text=get_location)
              show_loc_label.grid(row=2,column=0)

              temp_data = sdata2["hourly"]["temperature_2m"]
              print()
              print()

              min_temp_label = customtkinter.CTkLabel(home,text=min(temp_data))
              min_temp_label.grid(row=2,column=3)                                                # f" with {} in a continous string separates variables
                                                                                    #and string
              max_temp_label = customtkinter.CTkLabel(home,text=max(temp_data))
              max_temp_label.grid(row=3,column=3) 
                                                                                    #f"{sdata['c']}"
              
              #print("Status code:", response.status_code)     # add this
              #print("Full response:", sdata2)                 # already have this
        

search_butt = customtkinter.CTkButton(home, text="Search", command=fetch_data)
search_butt.grid(row=4,column=2)




home.mainloop()