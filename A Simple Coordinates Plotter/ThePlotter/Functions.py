import csv
import webbrowser as wb
from Geo import Geopoint
from folium import Map

def display_menu():
    print("This Python app will plot longitude and latitude coordinates and display those coordinates on a browser "
          "based map. "
          "Please input your longitude and latitude coordinates into the provided coordinates.csv file."
          "\n"
          "Please select one of the following options below"
          "\n"
          "1. Use the included coordinates.csv file"
          "\n"
          "2. Input the full path for a .csv file at another location"
          "\n"
          "Press any other key to exit the application.")

def process_file(csvfile, coordList):
    with open(csvfile, "r") as thePlotter:
        # Set up CSV reader and process the header
        csvReader = csv.reader(thePlotter)
        header = next(csvReader)
        latIndex = header.index("latitude")
        longIndex = header.index("longitude")

        for row in csvReader:
            lat = row[latIndex]
            lon = row[longIndex]
            coordList.append([lat, lon])

def generate_map(coordList):
    midpoint = int(len(coordList) / 2)
    mymap = Map(coordList[midpoint])

    for lat,long in coordList:
        geomarker = Geopoint(latitude=lat, longitude=long)
        geomarker.add_to(mymap)

    mymap.save(str("map.html"))
    wb.open(str("map.html"))