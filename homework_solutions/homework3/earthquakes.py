import requests
import time
from datetime import datetime

class Earthquake:

  def __init__(self, json):
    props = json['properties']
    self.time = float(props['time']) / 1000
    self.mag = float(props['mag'])
    self.place = props['place']
    coord = json['geometry']['coordinates']
    self.latitude, self.longitude, self.depth = float(coord[0]), float(coord[1]), float(coord[2])

  def __repr__(self): 
    time = str(datetime.fromtimestamp(self.time)) 
    return f"{time} -- {self.mag} {self.place}"   


def fetch_earthquake_data():
    url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        json_quake_list =  data["features"]
        return [Earthquake(json_quake) for json_quake in json_quake_list]
    else:
        print("Error fetching data:", response.status_code)
        return []


def print_data():
    while True:
        earthquakes = fetch_earthquake_data()
        for q in earthquakes: 
          print(q)
        print()
        time.sleep(60)

def print_new_quakes():
    pass # Replace for part a) 

def print_k_largest(k=3):
    pass # Replace for part b)

if __name__ == "__main__":

    # only one of the following three functions shoudl be called at a time
    print_data()
    #print_new_quakes() # for part a) 
    #print_k_largest(3) # for part b)
