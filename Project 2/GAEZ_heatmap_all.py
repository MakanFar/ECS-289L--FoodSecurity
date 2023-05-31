import os
import numpy as np
import matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt
from osgeo import gdal

# files for different product prediction are downloaded manually: 
for fname in os.listdir('.'):
	os.system('gdal_translate -projwin 97.455582 20.058877 109.606461 8.888170 -of GTiff ' + fname +'  clipped.tif')
	harvest = gdal.Open('clipped.tif')
	harvest = np.array(harvest.GetRasterBand(1).ReadAsArray())

	fig, ax = plt.subplots()
	# fig.colorbar()
	im = ax.imshow(harvest)
	plt.imsave(fname[:-4] + '_heatmap.png',harvest)


# fig.tight_layout()
# plt.show()