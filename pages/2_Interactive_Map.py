import streamlit as st
import pydeck as pdk
import pandas as pd
import numpy as np

st.title("🌍 Interactive Map Tools")

# Generate random data for visualization
data = pd.DataFrame(
    np.random.randn(500, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)

# Sidebar for selecting map tools
map_tool = st.sidebar.radio(
    "Select a Map Visualization Tool",
    ("Scatterplot", "Heatmap", "3D Terrain", "Cluster Layer")
)

if map_tool == "Scatterplot":
    st.header("Scatterplot Layer")
    st.write("Displays points on the map with hover tooltips.")

    # Scatterplot Layer
    scatter_layer = pdk.Layer(
        "ScatterplotLayer",
        data=data,
        get_position='[lon, lat]',
        get_color='[200, 30, 0, 160]',
        get_radius=200,
        pickable=True,
    )

    view_state = pdk.ViewState(
        latitude=data['lat'].mean(),
        longitude=data['lon'].mean(),
        zoom=12,
        pitch=45,
    )

    scatter_deck = pdk.Deck(
        layers=[scatter_layer],
        initial_view_state=view_state,
        tooltip={"text": "Latitude: {lat}\nLongitude: {lon}"}
    )

    st.pydeck_chart(scatter_deck)

elif map_tool == "Heatmap":
    st.header("Heatmap Layer")
    st.write("Visualizes density using a heatmap.")

    # Heatmap Layer
    heatmap_layer = pdk.Layer(
        "HeatmapLayer",
        data=data,
        get_position='[lon, lat]',
        aggregation=pdk.types.String("MEAN"),
        intensity=1,
        radius_pixels=30,
    )

    view_state = pdk.ViewState(
        latitude=data['lat'].mean(),
        longitude=data['lon'].mean(),
        zoom=12,
        pitch=0,
    )

    heatmap_deck = pdk.Deck(
        layers=[heatmap_layer],
        initial_view_state=view_state,
    )

    st.pydeck_chart(heatmap_deck)

elif map_tool == "3D Terrain":
    st.header("3D Terrain Layer")
    st.write("Adds elevation to the map for a 3D effect.")

    # 3D Terrain Data
    terrain_data = pd.DataFrame(
        np.random.randn(500, 3) / [50, 50, 5] + [37.76, -122.4, 10],
        columns=['lat', 'lon', 'elevation']
    )

    terrain_layer = pdk.Layer(
        "ColumnLayer",
        data=terrain_data,
        get_position='[lon, lat]',
        get_elevation='elevation',
        elevation_scale=50,
        radius=100,
        get_fill_color='[200, elevation * 20, 160]',
        pickable=True,
        auto_highlight=True,
    )

    view_state = pdk.ViewState(
        latitude=terrain_data['lat'].mean(),
        longitude=terrain_data['lon'].mean(),
        zoom=12,
        pitch=45,
    )

    terrain_deck = pdk.Deck(
        layers=[terrain_layer],
        initial_view_state=view_state,
        tooltip={"text": "Latitude: {lat}\nLongitude: {lon}\nElevation: {elevation}"}
    )

    st.pydeck_chart(terrain_deck)

elif map_tool == "Cluster Layer":
    st.header("Cluster Layer")
    st.write("Groups nearby points into clusters.")

    # Cluster Layer
    cluster_layer = pdk.Layer(
        "ClusterLayer",
        data=data,
        get_position='[lon, lat]',
        cluster_radius=100,
        get_fill_color='[200, 150, 0]',
        pickable=True,
    )

    view_state = pdk.ViewState(
        latitude=data['lat'].mean(),
        longitude=data['lon'].mean(),
        zoom=12,
        pitch=0,
    )

    cluster_deck = pdk.Deck(
        layers=[cluster_layer],
        initial_view_state=view_state,
        tooltip={"text": "Clustered Points"}
    )

    st.pydeck_chart(cluster_deck)
