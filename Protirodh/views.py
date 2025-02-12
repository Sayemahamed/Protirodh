import folium
import json
import pandas as pd
from django.shortcuts import render
from django.templatetags.static import static
from django.http import HttpResponse


def handler404(request, exception):
    print("404 handler called!")  # Debug print
    return render(request, '404.html', status=404)


def handler500(request, *args, **argv):
    print("500 handler called!")
    return render(request, '500.html', status=500)


def handler403(request, exception):
    print("403 handler called!")
    return render(request, '403.html', status=403)

def bangladesh_heatmap(request):
    # Load Bangladesh District GeoJSON
    geojson_path = "static/geojson/bangladesh_geojson_adm2_64_districts_zillas.json"
    with open(geojson_path, "r", encoding="utf-8") as f:
        bd_geojson = json.load(f)

    district_data = {
        "Dhaka": 8,
        "Chattogram": 6,
        "Khulna": 4,
        "Rajshahi": 3,
        "Sylhet": 5,
        "Bagerhat": 4,
        "Barguna": 2,
        "Barishal": 2,
        "Bhola": 3,
        "Bogra": 5,
        "Sherpur": 7,
    }

    # Create a map centered on Bangladesh
    map_bd = folium.Map(location=[23.685, 90.3563], zoom_start=7)

    # Add Choropleth Layer
    folium.Choropleth(
        geo_data=bd_geojson,
        name="Heatmap",
        data=pd.DataFrame(list(district_data.items()), columns=["District", "Value"]),
        columns=["District", "Value"],
        key_on="feature.properties.ADM2_EN",  # Use district name from GeoJSON
        fill_color="YlOrRd",
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name="Heatmap Intensity",
    ).add_to(map_bd)

    # Save the map to an HTML file inside static
    map_path = "static/maps/bangladesh_heatmap.html"
    map_bd.save(map_path)

    return render(request, "heatmap.html", {"map_path": static("maps/bangladesh_heatmap.html")})