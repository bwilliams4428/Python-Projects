# This script reads a GPS track in CSV format and
#  prints a list of coordinate pairs
import csv

# Open the input file
with open("sample.csv", "r") as gpsTrack:
    # Set up CSV reader and process the header
    csvReader = csv.reader(gpsTrack)
    header = next(csvReader)
    latIndex = header.index("latitude")
    lonIndex = header.index("longitude")

    # Make an empty list
    coordList = []

    # Loop through the lines in the file and get each coordinate
    for row in csvReader:
        lat = row[latIndex]
        lon = row[lonIndex]
        coordList.append([lat, lon])

    # Print the coordinate list
    print(coordList)