import requests  # Library to make HTTP requests to fetch the webpage
from bs4 import BeautifulSoup  # Library to parse the HTML content
import csv # Library to save the data into a CSV file
import time # Library to get the current date and time
import schedule # Library to schedule tasks
from datetime import datetime
import os # Library to check if the file exist
from lxml import html


#Function to get the weather data and save it to a CSV

def get_temperature_data():
    # The URL of the weather page (you can change the URL for a specific city)
    url = "https://www.timeanddate.com/weather/usa/cleveland"

    # Make a request to fetch the content of the page
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the page content using BeautifulSoup
        tree=html.fromstring(response.content)
        soup = BeautifulSoup(response.text, 'html.parser')
        temperature_data = soup.find("div", class_="h2")
        feels_like=tree.xpath("//p[2]/text()[1]")

        # If we find the temperature, print it
        if temperature_data:
            temperature=temperature_data.text.strip()

            print("Temperature:", temperature)
            print("Temperature:", temperature)
            print("Feels Like:", feels_like[0] if feels_like else "N/A")
            now = datetime.now()

            #Define file path
            filepath= 'C:/Users/navee/PycharmProjects/Weather_ETL/weather_data.csv'

            #check if file exist
            file_exists=os.path.isfile(filepath)

            #if the file exists

            with open(filepath,"a", newline="") as file:
                writer = csv.writer(file) # create a writer object to write data into the file

                #check if the file is empty
                file.seek(0,2)
                if not file_exists or file.tell()==0:
                    writer.writerow(["Date","Time","Temperature","Feels Like"])

                writer.writerow([now.strftime("%Y-%m-%d"),
                             now.strftime("%H:%M:%S"),
                             temperature,
                             feels_like[0] if feels_like else "N/A",
                            ])
            #write the data into the CSV file

            

        else:
            print("Could not find temperature data.")
    else:
        # If the connection to the website failed, print the error
        print("Failed to retrieve the webpage. Status code:", response.status_code)

# Schedule the task to run every hour

schedule.every().hour.do(get_temperature_data)

#Loop to keep the script running and checking the schedule

while True:
    schedule.run_pending() #Run any scheduled tasks that are due
    time.sleep(1) #wait for 1 second before checking again