#!/usr/bin/env python3

import urllib.request
import json




def main():
    print("jsondata_start")
    urlData = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    webUrl = urllib.request.urlopen(urlData)
    print("result code: " + str(webUrl.getcode()))

    if webUrl.getcode() == 200:
        data = webUrl.read()
        printResults(data)
    else:
        print("received errot, cannot parse results")


def printResults(data):
    theJSON = json.loads(data)

    if "title" in theJSON["metadata"]:
        print(theJSON["metadata"]["title"])



if __name__ == "__main__":
    main()
