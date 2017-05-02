import time
import webbrowser

total_breaks = 3
count = 0

print("Break reminder will launch every two hours until you've had your day's total of breaks.")
while count < total_breaks:
    time.sleep(240)
    webbrowser.open("http://www.buzzfeed.com/videos")

    count += 1
