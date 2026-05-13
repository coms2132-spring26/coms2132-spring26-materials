import requests
import time
from datetime import datetime
from kbest import KBestCounter

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

  def __hash__(self): # for part a 
    return hash(self.time) * 5 + \
           hash(self.mag) * 7 + \
           hash(self.place) * 11 + \
           hash(self.longitude) * 13 + \
           hash(self.latitude) * 17 + \
           hash(self.depth) * 23
  
  def __eq__(self, other): # for part a
    if not isinstance(other, Earthquake):
      return False
    return self.time == other.time \
      and self.mag == other.mag \
      and self.place == other.place \
      and self.latitude == other.latitude \
      and self.longitude == other.longitude \
      and self.depth == other.depth

  def __lt__(self, other): 
    return self.mag < other.mag

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
  
  quake_set = set()
  while True: 
    earthquakes = fetch_earthquake_data()
    #quake_set.update(earthquakes) # only add new earthquakes 

    # or step by step as follows
    for q in earthquakes: 
      if not q in quake_set: 
        quake_set.add(q)
        print(q)    
    time.sleep(60)


def print_k_largest(k=3):

  largest_quakes = KBestCounter(3) 
  seen = set() 
  while True: 
    earthquakes = fetch_earthquake_data()
    #quake_set.update(earthquakes) # only add new earthquakes 

    # or step by step as follows
    for q in earthquakes: 
      if not q in seen: 
        seen.add(q)
        largest_quakes.count(q)

    print(" ")
    for q in largest_quakes.kbest():
      print(q)
    print("--- ") 
    
    time.sleep(60)


if __name__ == "__main__":

    # only one of the following three functions shoudl be called at a time
    #print_data()
    #print_new_quakes() # for part a) 
    print_k_largest(3) # for part b)
