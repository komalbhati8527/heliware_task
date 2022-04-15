from django.shortcuts import render
from heligeo import heliGeoprocessingService, heliRouteService
from folium import folium
from folium.features import GeoJson
import os


# Create your views here.
def index(request):
    return render(request, "form.html")


def createPolygon(request):
    geojson = request.POST.get("geojson") # request requirement is not clear; I have taken hardcore polygon's and geojson data
    apikey = 'jhyterfvdrwesuyt'
    polygon1 = {"type": "FeatureCollection", "features": [{"type": "Feature", "properties": {},
                                                           "geometry": {"type": "Polygon", "coordinates": [
                                                               [[77.17037200927734, 28.507013881018153],
                                                                [77.22169876098633, 28.507013881018153],
                                                                [77.22169876098633, 28.57879352089678],
                                                                [77.17037200927734, 28.57879352089678],
                                                                [77.17037200927734, 28.507013881018153]]]}}]}
    polygon2 = {"type": "FeatureCollection", "features": [{"type": "Feature", "properties": {},
                                                           "geometry": {"type": "Polygon", "coordinates": [
                                                               [[77.18891143798828, 28.52737652035115],
                                                                [77.28229522705078, 28.52737652035115],
                                                                [77.28229522705078, 28.56341628776094],
                                                                [77.18891143798828, 28.56341628776094],
                                                                [77.18891143798828, 28.52737652035115]]]}}]}
    polygon_list = [polygon1, polygon2]
    union_data = heliGeoprocessingService.Union(apikey, polygon_list)
    map = folium.Map(location=[22.5726, 88.3639], zoom_start=5)
    GeoJson(union_data).add_to(map)
    directory = os.getcwd()+"/heliware/heliwareApp/templates/"
    map.save(directory+"index.html")
    return render(request, "index.html")


