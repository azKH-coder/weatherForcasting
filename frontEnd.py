
import backEnd
from tkinter import *



root = Tk()
root.geometry("400x450")
root.resizable(width=False, height=False)
root.title("Live Weather")
root.configure(background="#CCE5FF")

liveWeatherText = StringVar()
lblTemperatureText = StringVar()
# **************************
def liveWeatherFront():
    lWeather = backEnd.liveWeather()
    liveWeatherText.set(lWeather)

def hourlyWeatherFront(hour):
    lTemp = backEnd.request(hour)
    lblTemperatureText.set(lTemp)

# **************************
#fistFrame: showing the numbers:0 ... 24
frm1 = Frame(root, bg= "#CCE5FF", height=200, width=450)
frm1.pack(side=TOP)

#secondFrame
frm2 = Frame(root, bg='#99CCFF', height=200, width=450)
frm2.pack(side=TOP)


#firstFrame: Buttons: using grid systems to put buttons on it

btn01 = Button(frm1, command= lambda: hourlyWeatherFront(1) ,text='01', bg='#FFFFFF', width=5, height=2)
btn01.grid(row = 0 , column = 0, padx=5, pady=8)

btn02 = Button(frm1, command= lambda: hourlyWeatherFront(2), text='02', bg='#FFFFFF', width=5, height=2)
btn02.grid(row = 0 , column = 1, padx=5, pady=8)

btn03 = Button(frm1, command= lambda: hourlyWeatherFront(3), text='03', bg='#FFFFFF', width=5, height=2)
btn03.grid(row = 0 , column = 2, padx=5, pady=8)

btn04 = Button(frm1, command= lambda: hourlyWeatherFront(4), text='04', bg='#FFFFFF', width=5, height=2)
btn04.grid(row = 0 , column = 3, padx=5, pady=8)

btn05 = Button(frm1, command= lambda: hourlyWeatherFront(5), text='05', bg='#FFFFFF', width=5, height=2)
btn05.grid(row = 0 , column = 4, padx=5, pady=8)

btn06 = Button(frm1, command= lambda: hourlyWeatherFront(6), text='06', bg='#FFFFFF', width=5, height=2)
btn06.grid(row = 0 , column = 5, padx=5, pady=8)

# *************************************************************

btn07 = Button(frm1, command= lambda: hourlyWeatherFront(7), text='07', bg='#FFFFFF', width=5, height=2)
btn07.grid(row = 1 , column = 0, padx=5, pady=8)

btn08 = Button(frm1, command= lambda: hourlyWeatherFront(8), text='08', bg='#FFFFFF', width=5, height=2)
btn08.grid(row = 1 , column = 1, padx=5, pady=8)

btn09 = Button(frm1, command= lambda: hourlyWeatherFront(9), text='09', bg='#FFFFFF', width=5, height=2)
btn09.grid(row = 1 , column = 2, padx=5, pady=8)

btn10 = Button(frm1, command= lambda: hourlyWeatherFront(10), text='10', bg='#FFFFFF', width=5, height=2)
btn10.grid(row = 1 , column = 3, padx=5, pady=8)

btn11 = Button(frm1, command= lambda: hourlyWeatherFront(11), text='11', bg='#FFFFFF', width=5, height=2)
btn11.grid(row = 1 , column = 4, padx=5, pady=8)

btn12 = Button(frm1,command= lambda: hourlyWeatherFront(12), text='12', bg='#FFFFFF', width=5, height=2)
btn12.grid(row = 1 , column = 5, padx=5, pady=8)

# ************************************************************

btn13 = Button(frm1, command= lambda: hourlyWeatherFront(13), text='13', bg='#FFFFFF', width=5, height=2)
btn13.grid(row = 2 , column = 0, padx=5, pady=8)

btn14 = Button(frm1, command= lambda: hourlyWeatherFront(14), text='14', bg='#FFFFFF', width=5, height=2)
btn14.grid(row = 2 , column = 1, padx=5, pady=8)

btn15 = Button(frm1,command= lambda: hourlyWeatherFront(15), text='15', bg='#FFFFFF', width=5, height=2)
btn15.grid(row = 2 , column = 2, padx=5, pady=8)

btn16 = Button(frm1, command= lambda: hourlyWeatherFront(16), text='16', bg='#FFFFFF', width=5, height=2)
btn16.grid(row = 2 , column = 3, padx=5, pady=8)

btn17 = Button(frm1,command= lambda: hourlyWeatherFront(17), text='17', bg='#FFFFFF', width=5, height=2)
btn17.grid(row = 2 , column = 4, padx=5, pady=8)

btn18 = Button(frm1, command= lambda: hourlyWeatherFront(18), text='18', bg='#FFFFFF', width=5, height=2)
btn18.grid(row = 2 , column = 5, padx=5, pady=8)

# **************************************************************

btn19 = Button(frm1, command= lambda: hourlyWeatherFront(19), text='19', bg='#FFFFFF', width=5, height=2)
btn19.grid(row = 3 , column = 0, padx=5, pady=8)

btn20 = Button(frm1, command= lambda: hourlyWeatherFront(20), text='20', bg='#FFFFFF', width=5, height=2)
btn20.grid(row = 3 , column = 1, padx=5, pady=8)

btn21 = Button(frm1, command= lambda: hourlyWeatherFront(21), text='21', bg='#FFFFFF', width=5, height=2)
btn21.grid(row = 3 , column = 2, padx=5, pady=8)

btn22 = Button(frm1, command= lambda: hourlyWeatherFront(22), text='22', bg='#FFFFFF', width=5, height=2)
btn22.grid(row = 3 , column = 3, padx=5, pady=8)

btn23 = Button(frm1, command= lambda: hourlyWeatherFront(23), text='23', bg='#FFFFFF', width=5, height=2)
btn23.grid(row = 3 , column = 4, padx=5, pady=8)

btn24 = Button(frm1,command= lambda: hourlyWeatherFront(00), text='24', bg='#FFFFFF', width=5, height=2)
btn24.grid(row = 3 , column = 5, padx=5, pady=8)

# second Frame
btn2 = Button(frm2, text=" Click the above buttons to Know the hourly temperature:", bg='#FFFFFF', width=80, height=2)
btn2.pack(side = TOP, padx=5, pady=16)

lblTemperature = Label(frm2,width=20, height=2, textvariable= lblTemperatureText )
lblTemperature.pack(side = TOP, padx=5, pady=6)

btn3 = Button(frm2, command= lambda: liveWeatherFront() ,text=" Click Me to Know the live weather:", bg='#FFFFFF', width=80, height=2)
btn3.pack(side = TOP, padx=5, pady=6)

lblLiveWeather = Label(frm2 ,width=20, height=2, textvariable= liveWeatherText )
lblLiveWeather.pack(side = TOP, padx=5, pady=6)
# lb3.configure(text=f"the Live Weather of {hourNow} is {tempp} c")
root.mainloop()