from plyer import notification
import requests
import time
import datetime


def notify(title,message):

    notification.notify(
        title = title,
        message = message,
        app_icon = "icon.ico", 
        timeout = 3      
    )

covidData = None

try:

    covidData = requests.get("https://corona-rest-api.herokuapp.com/Api/india")

except:

    #if the data is not fetched due to lack of internet

    print("Please! Check your internet connection")


data = covidData.json()['Success']



if __name__ == "__main__":

    while True:

        notify("COVID19 Stats on {}".format(datetime.date.today()), "Total cases : {totalcases}\nToday cases : {todaycases}\nToday deaths :{todaydeaths}\nTotal active :{active}".format(
                        totalcases = data['cases'],
                        todaycases = data['todayCases'],
                        todaydeaths = data['todayDeaths'],
                        active = data["active"]))
        time.sleep(3600)



                        
                        



    

