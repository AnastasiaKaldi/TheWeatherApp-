from tkinter import *
from tkinter import messagebox
import requests
from PIL import ImageTk, Image
from time import strftime
from datetime import datetime

w = Tk()
w.geometry('800x400')
w.title("Weather app")
w.resizable(0, 0)

try:

    def weather_data(query):
        res = requests.get(
            'http://api.openweathermap.org/data/2.5/weather?' + query +
            '&units=metric&appid=be112a76a7d7af5b6573ee9c46b1643c')
        return res.json()

    Frame(w, width=800, height=50, bg='#353535').place(x=0, y=0)

    #search bar
    imgSearch = ImageTk.PhotoImage(Image.open("searchtool.png"))

    def on_entry(e):
        e1.delete(0, 'end')

    def on_leave(e):
        if e1.get() == '':
            e1.insert(0, 'Search city')

    e1 = Entry(w, width=21, fg='white', bg='#353536', border=0)
    e1.config(font=('Times New Roman', 12))
    e1.bind("<FocusIn>", on_entry)
    e1.bind("<FocusOut>", on_leave)
    e1.insert(0, 'Search City')
    e1.place(x=620, y=15)

    # Date time format
    a = datetime.today().strftime('%B')
    b = (a.upper())
    q = datetime.now().month

    now = datetime.now()
    c = now.strftime('%B')
    month = c[0:3]

    today = datetime.today()
    date = today.strftime("%d")

    def label(a):
        Frame(width=500, height=50, bg='#353535').place(x=0, y=0)

        l1 = Label(w, text=str(a), bg="#353535", fg="white")
        l1.config(font=("Times New Roman", 18))
        l1.place(x=20, y=8)

        city = a

        query = 'q=' + city
        w_data = weather_data(query)
        result = w_data

        try:
            check = '{}'.format(result['main']['temp'])
            print(check)
        except:
            pass
            messagebox.showinfo("", "City not Found :(")

        c = (int(float(check)))
        description = ("{}".format(result['weather'][0]['description']))
        weather = ("{}".format(result['weather'][0]['main']))

        global imgWeather

        if c > 10 and weather == "Haze" or weather == "Clear":
            Frame(w, width=800, height=350, bg="#ffbf80").place(x=0, y=50)
            imgWeather = ImageTk.PhotoImage(Image.open("sun.png"))
            Label(w, image=imgWeather, border=0).place(x=170, y=130)
            bcolor = "#ffbf80"
            fcolor = "white"

        elif c > 10 and weather == "Clouds":
            Frame(w, width=800, height=350, bg="#bfbfbf").place(x=0, y=50)
            imgWeather = ImageTk.PhotoImage(Image.open("cloud.png"))
            Label(w, image=imgWeather, border=0).place(x=170, y=130)
            bcolor = "#bfbfbf"
            fcolor = "white"

        elif c <= 10 and weather == "Partly Cloudy":
            Frame(w, width=800, height=350, bg="#b3b3cb").place(x=0, y=50)
            imgWeather = ImageTk.PhotoImage(Image.open("partlycloudy.png"))
            Label(w, image=imgWeather, border=0).place(x=170, y=130)
            bcolor = "#b3b3cb"
            fcolor = "white"

        elif c > 10 and weather == "Rain":
            Frame(w, width=800, height=350, bg="#4080bf").place(x=0, y=50)
            imgWeather = ImageTk.PhotoImage(Image.open("rain.png"))
            Label(w, image=imgWeather, border=0).place(x=170, y=130)
            bcolor = "#4080bf"
            fcolor = "white"

        elif c <= 10 and weather == "Fog" or weather == "Clear":
            Frame(w, width=800, height=350, bg="#9494b8").place(x=0, y=50)
            imgWeather = ImageTk.PhotoImage(Image.open("fog.png"))
            Label(w, image=imgWeather, border=0).place(x=170, y=130)
            bcolor = "#9494b8"
            fcolor = "black"

        else:
            Frame(w, width=800, height=350, bg="#e6b3cc").place(x=0, y=50)
            label = Label(w, text=weather, border=0, bg='white')
            label.configure(font=(("Times New Roman", 18)))
            label.place(x=160, y=130)
            bcolor = "#e6b3cc"
            fcolor = "black"

        w_data = weather_data(query)
        result = w_data

        h = ("Humidity: {}".format(result['main']['humidity']))
        p = ("Pressure: {}".format(result['main']['pressure']))
        tempMax = ("MAX Temp: {}".format(result['main']['temp_max']))
        tempMin = ("MIN Temp: {}".format(result['main']['temp_min']))
        wSpeed = ("Wind Speed: {} m/s".format(result['wind']['speed']))

        l2 = Label(w, text=str(month + " " + date), bg=bcolor, fg=fcolor)
        l2.config(font=("Times New Roman", 25))
        l2.place(x=330, y=335)

        l3 = Label(w, text=str(h + "%"), bg=bcolor, fg=fcolor)
        l3.config(font=("Times New Roman", 12))
        l3.place(x=510, y=95)

        l3 = Label(w, text=str(p + "hPa"), bg=bcolor, fg=fcolor)
        l3.config(font=("Times New Roman", 12))
        l3.place(x=510, y=135)

        l3 = Label(w, text=str(tempMin) + "°C", bg=bcolor, fg=fcolor)
        l3.config(font=("Times New Roman", 12))
        l3.place(x=510, y=175)

        l3 = Label(w, text=str(tempMax) + "°C", bg=bcolor, fg=fcolor)
        l3.config(font=("Times New Roman", 12))
        l3.place(x=510, y=215)

        l3 = Label(w, text=str(wSpeed), bg=bcolor, fg=fcolor)
        l3.config(font=("Times New Roman", 12))
        l3.place(x=510, y=255)

        l3 = Label(w, text=str(c) + "°C", bg=bcolor, fg=fcolor)
        l3.config(font=("Times New Roman", 42))
        l3.place(x=330, y=150)

    label(a="Los angeles")

    def cmd1():
        b = str(e1.get())
        label(str(b))

    Button(w, image=imgSearch, command=cmd1, border=0).place(x=750, y=10)

except:

    Frame(w, width=800, height=400, bg='white').place(x=0, y=0)
    global imgNoInternet
    imgNoInternet = ImageTk.PhotoImage(Image.open("nointernet.png"))

    Label(w, image=imgNoInternet, border=0).pack(expand=True)

w.mainloop()
