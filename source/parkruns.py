import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
from shapely.geometry import Polygon, Point
import numpy as np
from pyproj import CRS, Transformer

# Load the parkrun data
parkruns_url = "http://www.rhoff.org.uk/Full_5k_parkrun_List.csv"
parkruns = pd.read_csv(parkruns_url)

# Filter for parkruns in the Netherlands
parkrun = parkruns[parkruns['Country Name'] == 'Netherlands']

# Load the shapefile of Netherlands
NLD = gpd.read_file("../data/gadm41_NLD_1.shp")

# Remove specific regions
NLD_fixed = NLD[~NLD['NAME_1'].isin(["Zeeuwse meren", "IJsselmeer"])]

# Set the correct projection for the Netherlands (EPSG:28992)
NLD_fixed = NLD_fixed.to_crs(epsg=28992)

# Transform the parkrun coordinates to the same projection
parkrun_gdf = gpd.GeoDataFrame(parkrun, geometry=gpd.points_from_xy(parkrun['Longitude'], parkrun['Latitude']))
parkrun_gdf = parkrun_gdf.set_crs(epsg=4326)  # Assuming parkrun data is in WGS84
parkrun_gdf = parkrun_gdf.to_crs(epsg=28992)

# Extract the coordinates after projection for the Voronoi plot
points = np.array([(point.x, point.y) for point in parkrun_gdf.geometry])

# Voronoi diagram setup
vor = Voronoi(points)

# Caption for the plot
open_parkruns_count = len(parkrun_gdf[parkrun_gdf['Status'] == "Open"])
caption = f"Voronoi plot of the {open_parkruns_count} parkruns in The Netherlands."

# Get the bounds of the Netherlands and parkrun data to set axis limits
nld_bounds = NLD_fixed.total_bounds  # [xmin, ymin, xmax, ymax]
parkrun_bounds = parkrun_gdf.total_bounds  # [xmin, ymin, xmax, ymax]

# Set the axis limits slightly wider than the data bounds to avoid cutting off any parts
xlim = [min(nld_bounds[0], parkrun_bounds[0]) - 10000, max(nld_bounds[2], parkrun_bounds[2]) + 10000]
ylim = [min(nld_bounds[1], parkrun_bounds[1]) - 10000, max(nld_bounds[3], parkrun_bounds[3]) + 10000]

# Plot the map with Voronoi diagram
fig, ax = plt.subplots(figsize=(10, 10))

# Plot Netherlands regions
NLD_fixed.boundary.plot(ax=ax, color="black", linewidth=1)
NLD_fixed.plot(ax=ax, color="orange", alpha=0.9)

# Plot the Voronoi diagram
voronoi_plot_2d(vor, ax=ax, show_vertices=False, line_colors='black', line_width=0.5, line_alpha=0.6)

# Plot official parkruns
official_parkruns = parkrun_gdf[parkrun_gdf['Status'] == "Open"]
ax.scatter(official_parkruns.geometry.x, official_parkruns.geometry.y, color='black', edgecolor='white', s=100, zorder=5, label="Official parkruns")
# Set axis limits
ax.set_xlim(xlim)
ax.set_ylim(ylim)
ax.axis('off')
ax.set_title(caption)

# Save the plot
plt.savefig("../images/parkruns.png", dpi=100, bbox_inches='tight')
plt.show()

# Second plot without country borders
fig, ax = plt.subplots(figsize=(10, 10))

# Plot only the parkruns and Voronoi diagram without borders
ax.scatter(parkrun_gdf.geometry.x, parkrun_gdf.geometry.y, color='black', s=100, zorder=5)
voronoi_plot_2d(vor, ax=ax, show_vertices=False, line_colors='black', line_width=0.5, line_alpha=0.6)

ax.set_aspect('equal')

# Save the plot
plt.savefig("../images/noborder.png", dpi=100, bbox_inches='tight')
plt.show()
