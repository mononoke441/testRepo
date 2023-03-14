import cartopy.crs as ccrs
import matplotlib.pyplot as plt
from cnmaps import get_adm_maps,draw_maps
cnmaps.
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection=ccrs.PlateCarree())

draw_maps(get_adm_maps(level='国'))

plt.show()