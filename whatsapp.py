import pywhatkit
import csv
from datetime import datetime
time = datetime.now()
with open("Path of csv File","r") as file:
    reader = csv.reader(file)
    for row in reader:
        time = datetime.now()
        pywhatkit.sendwhatmsg(f"+91-{row[1]}","Welcome to TheMentorLive ",time.hour,time.minute+1,5)
