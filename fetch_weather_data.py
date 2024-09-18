import requests  # Library to make HTTP requests to fetch the webpage
from bs4 import BeautifulSoup  # Library to parse the HTML content
import csv # Library to save the data into a CSV file
import time # Library to get the current date and time
import schedule # Library to schedule tasks

#Function to get the weather data and save it to a CSV

def get_temperature_data():
    # The URL of the weather page (you can change the URL for a specific city)
    url = "https://www.timeanddate.com/weather/"

    # Make a request to fetch the content of the page
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the page content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the temperature using the class "h2"
        temperature_data = soup.find("span", class_="my-city__temp")

        # If we find the temperature, print it
        if temperature_data:
            temperature=temperature_data.text.strip()
            print("Temperature:", temperature)  # Remove extra spaces using .strip()

            # Define the data to save
           # data=[["Date","Temperature"]] #The first row is the header with column names
            #data.append([time.strftime("%Y-%m-%d"), temperature]) # Add the current date and temperature

            #Open a csv file to save the data


            #Save to the CSV file
            # "a" means we append data to the end of the file if it already exists
            now=datetime. now()

            with open("weather_data.csv","a",newline="") as file:
                writer = csv.writer(file) # create a writer object to write data into the file
                writer.writerow([now.strftime("%Y-%m-%d %H:%M%:%S"), temperature]) #write the data into the CSV file
            

        else:
            print("Could not find temperature data.")
    else:
        # If the connection to the website failed, print the error
        print("Failed to retrieve the webpage. Status code:", response.status_code)

# Schedule the task to run every day at a specific time (e.g 8:00 AM)

schedule.every().hour.do(get_temperature_data)

# Loop to keep the script running and checking the schedule

while True:
    schedule.run_pending() #Run any scheduled tasks that are due
    time.sleep(1) #wait for 1 second before checking again