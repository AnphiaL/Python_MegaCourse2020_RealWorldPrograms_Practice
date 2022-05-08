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

map2 = folium.Map(location=[39.58,-108.09],
                 zoom_start=2,
                 titles='Mapbox Bright')

fg_1 = folium.FeatureGroup(name='Volcanoes')
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
    fg_1.add_child(folium.CircleMarker(location=[lt,ln],
                                     radius=5,
                                     popup=folium.Popup(iframe),
                                     fill_color=color_converter(el),
                                     color='grey',
                                     fill_opacity=1.2 #Color saturation?
                                     ))
fg_2 = folium.FeatureGroup(name='Population')

fg_2.add_child(folium.GeoJson(data=open('World.json',
                                      'r',
                                      encoding='utf-8-sig').read(),
                            style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
                                                      else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
                                                      else 'red'}))
map2.add_child(fg_1)
map2.add_child(fg_2)
map2.add_child(folium.LayerControl())#put it after you have added the feature group layers
map2.save('layer_control_volcanoes_population.html')
