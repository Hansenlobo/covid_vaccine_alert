import time
import requests
import winsound
from datetime import date
today = date.today()
frequency = 2500 #Sound Frequency and Duration
duration = 1000

while True:
    d_id='286'  #Set district ID 286 for Udupi
    date = today.strftime("%d-%m-%Y")
    url = 'https://www.cowin.gov.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id='+d_id+'&date='+date   # API URL link
    # print(url)
    response = requests.get(url)
    print(f"URL Status={response.status_code}")     # check Response Status  if 200 Everything is fine
    data = response.json()
    total_centers = len(data["centers"])
    print(f"Total centers in your district = {total_centers}")     # print total centers in your District
    status = False
    for loop in range(total_centers):
        age = data["centers"][loop]["sessions"][0]["min_age_limit"]
        if age < 18:    #check for age below 18
            print("yayy u got it!")
            status = True
            print(data["centers"][loop]["name"])
        else:
            print("Better Luck Next time..")

    if status == True:
        print("got it")
        winsound.Beep(frequency, duration) #Beep sound when the condition matches!!
        time.sleep(2)
        winsound.Beep(frequency, duration)  
    time.sleep(90)   #Run Script every 90 seconds
