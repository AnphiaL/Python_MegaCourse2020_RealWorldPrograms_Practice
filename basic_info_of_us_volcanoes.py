import folium
import pandas
data = pandas.read_csv('Volcanoes.txt')

def color_converter(el):

    if el < 2000:
        return 'green'
    elif 2000 <= el < 3000:
        return 'orange'
    else:
        return 'red'

#creating a volcanol map with markers
map = folium.Map(location=[39.58,-108.09],
                 zoom_start=5,
                 titles='Mapbox Bright')

fg = folium.FeatureGroup(name='My Map')
lat = list(data['LAT'])
lon = list(data['LON'])
name = list(data['NAME'])
location = list(data['LOCATION'])
elev = list(data['ELEV'])
v_type = list(data['TYPE'])
html = """<h4>Volcano information:</h4>
Name: %s
Location: %s
Type: %s
Height: %s m
"""

for lt,ln,nm,loc,v_tp,el in zip(lat,lon,name,location,v_type,elev):
    iframe = folium.IFrame(html=html % (nm, loc,v_tp,el),
                           width=200,
                           height=100)
    fg.add_child(folium.Marker(location=[lt,ln],
                                     popup=folium.Popup(iframe),
                                     icon=folium.Icon(color=color_converter(el))))
map.add_child(fg)
map.save('basic_info_of_us_volcanoes_markers.html')

#creating a volcanol map with circlemarkers
map1 = folium.Map(location=[39.58,-108.09],
                 zoom_start=5,
                 titles='Mapbox Bright')

fg = folium.FeatureGroup(name='My Map')
lat = list(data['LAT'])
lon = list(data['LON'])
name = list(data['NAME'])
location = list(data['LOCATION'])
elev = list(data['ELEV'])
v_type = list(data['TYPE'])
html = """<h4>Volcano information:</h4>
Name: %s
Location: %s
Type: %s
Height: %s m
"""

for lt,ln,nm,loc,v_tp,el in zip(lat,lon,name,location,v_type,elev):
    iframe = folium.IFrame(html=html % (nm, loc,v_tp,el),
                           width=200,
                           height=100)
    fg.add_child(folium.CircleMarker(location=[lt,ln],
                                     radius=5,
                                     popup=folium.Popup(iframe),
                                     fill_color=color_converter(el),
                                     color='grey',
                                     fill_opacity=1.2 #Color saturation?
                                     ))
#map.save('basic_info_of_us_volcanoes.html')
map1.add_child(fg)
map1.save('basic_info_of_us_volcanoes_circlemarkers.html')
