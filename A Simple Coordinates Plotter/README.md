## A Simple Coordinates Plotter - Still a work in progress.........

This Python application reads a .csv file containing latitude and longitude points, saves the points to a list and displays those points on a map generated from your web browser.

A user can plot points that are inputted into the provided [coordinates.csv](https://github.com/bwilliams4428/Python-Projects/blob/main/A%20Simple%20Coordinates%20Plotter/ThePlotter/coordinates.csv) file or input the full path to a file at a different location on the user's computer.

If a user selects option 1, then the coordinates inputted into the coordinates.csv file will display on the web based map.

![Image1](https://github.com/bwilliams4428/Python-Projects/blob/main/A%20Simple%20Coordinates%20Plotter/ThePlotter/option1.PNG)

![Output](https://github.com/bwilliams4428/Python-Projects/blob/main/A%20Simple%20Coordinates%20Plotter/ThePlotter/Capture1.PNG)


If a user select option 2, then the user will be prompted to input the file path to a .csv file on the user's computers to have those coordinates displayed on a web based map.

![Image2](https://github.com/bwilliams4428/Python-Projects/blob/main/A%20Simple%20Coordinates%20Plotter/ThePlotter/option2.PNG)

![Output](https://github.com/bwilliams4428/Python-Projects/blob/main/A%20Simple%20Coordinates%20Plotter/ThePlotter/Capture1.PNG)


This application was tested using Python 3:
    
    python3 Plotter.py

Required Python libraries

* **csv**
* **webbrowser**
* **folium**

Using pip to install the required libraries typically works:

    python3 -m pip install folium

(I do have other libraries listed in my code(such as pytz,datatime and sunnyday but they are not used at this time):

This is a very simple implementation. I do plan to add more functionality and features to this application.
