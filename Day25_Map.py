import folium

# Create a map centered over India
india_map = folium.Map(location=[20.0, 75.0], zoom_start=4)

# Create a FeatureGroup to hold the GeoJson layer
feature_group = folium.FeatureGroup(name="Indian States")

# Read the GeoJSON data from file
with open("india_states.json", "r", encoding="utf-8-sig") as file:
    geojson_data = file.read()

# Add the GeoJSON layer with basic styling and optional tooltip
feature_group.add_child(folium.GeoJson(
    data=geojson_data,
    name="GeoJSON",
    style_function=lambda feature: {
        'fillColor': '#228B22',
        'color': 'black',
        'weight': 1,
        'fillOpacity': 0.5
    },
    tooltip=folium.GeoJsonTooltip(
        fields=['state'],    # Replace 'state' with the actual property name in your GeoJSON
        aliases=['State:'],
        localize=True
    )
))

# Add the feature group to the map
india_map.add_child(feature_group)

# Add layer control (optional if you plan to add more layers)
india_map.add_child(folium.LayerControl())

# Save the map to an HTML file
india_map.save("final.html")
