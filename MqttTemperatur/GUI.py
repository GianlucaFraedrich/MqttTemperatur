import tkinter as tk
import mysql.connector
import datetime

#Matplotlib Einstellungen


#SQL Verbindung
db = mysql.connector.connect(
host="localhost",
user="test",
password="pw",
database="mqtttemperatur"
)

def db_get_rooms ():
    #Gibt eine List mit alle Namen und ID's der Räume wieder
    #Example: [(1, 'Room1'), (2, 'Room2'), (3, 'Room3')]
    cursor = db.cursor()
    cursor.execute("SELECT * FROM rooms")
    result = cursor.fetchall()
    return result

def db_get_newest_temperature(Room_ID):
    #Gibt die letzte Temperatur des Raums wieder
    cursor = db.cursor()
    cursor.execute("SELECT Temperature from temperature WHERE ROOMS_ID = %s ORDER BY time DESC", (Room_ID,))
    result = cursor.fetchall()
    return result[0][0]

def db_get_temp_time(Room_ID, time):
    #Übergibt alle Temperaturen und deren Zeit des Raumes in den letzten x(time) Stunden als List wieder
    cursor = db.cursor()
    timenow=datetime.datetime.now()
    timepast=datetime.datetime.now() - datetime.timedelta(hours=time)
    cursor.execute("SELECT Temperature, time from temperature WHERE Rooms_ID = %s AND time BETWEEN %s AND %s ORDER BY time DESC", (Room_ID, timepast, timenow))
    result = cursor.fetchall()
    temp_list = []
    for temp in result:
        temp_list.append(temp)
    return temp_list



class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        button1 = tk.Button(parent)

        
if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()