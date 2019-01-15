import folium
import pandas

data=pandas.read_csv("./material/volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])

def color_produce(elevation):
  if elevation < 1000:
    return "green"
  elif 1000<=elevation<3000:
    return "orange" 
  else:
    return "red"

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles = "Mapbox Bright")
fg=folium.FeatureGroup(name="My Map")
for lt, lo, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location=[lt, lo], popup=str(el), 
    color=color_produce(el), fill=True, fill_opacity=100))
fg.add_child(folium.GeoJson(data=open('./material/world.json', 'r', encoding='utf-8-sig').read()))
map.add_child(fg)
map.save("Map.html")