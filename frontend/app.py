import streamlit as st
import requests
import folium
from streamlit_folium import folium_static, st_folium




#title
st.title("Weiterbetriebszeitrechner")


#input of coordinates of wind turbine
st.write('Bitte geben Sie die Koordinaten, der zu betrchtenden Anlage ein.')
cl1, cl2 = st.columns((1,1))
with cl1:
    long = st.number_input('Längengrad', value = 50., step = 0.0001)
with cl2:
    lat = st.number_input('Breitengrad', value =10., step = 0.0001)

#create two columns
col1, col2 = st.columns((1,1))

#column 1
with col1:
    st.write('Bitte geben Sie noch Folgendes an.')
    #user inputs
    #ibdate = st.date_input('Inbetriebnahmedatum')
    manufact = st.selectbox('Typenbezeichnung', ['E40 5.40', 'E40 6.44', 'E66 18.70', 'V80', 'V52', '1.5sl'])
    input1 = st.selectbox("Windzone", ('1', '2', '3', '4'))
    input2 = st.number_input("Jahresertrag in kWh", value=100000,)
    input3 = st.number_input("Mittlere Windgeschwindigkeit", value=5.5)

#column 2
with col2:
    #create folium map element
    mymap = folium.Map(location=[long, lat], zoom_start=15)
    mymarker = folium.Marker(location=[long, lat], popup="Mein Windrad", draggable=False)
    #add satelite pictures
    tile = folium.TileLayer(
            tiles = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
            attr = 'Esri',
            name = 'Esri Satellite',
            overlay = False,
            control = True
           ).add_to(mymap)
    #add marker
    mymarker.add_to(mymap)
    # Display the map in Streamlit using st_folium
    d2 = st_folium(mymap, width=400, height=400)


if st.button(label='Weiterbetriebszeit berechnen'):

    st.write('Ergebnis')
    #url = 'http://0.0.0.0:8123/predict'
    #
    #params = {
    #    'feature1': input1,
    #    'feature2': input2,
    #    'feature3': input3
    #}
    #response = requests.get(url, params=params).json()
    #
    #
    #st.write(f"Weiterbetriebszeit: {response['prediction']}")



#if __name__ == "__main__":
#    main()
#
