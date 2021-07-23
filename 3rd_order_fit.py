import pmd_beamphysics
import opal
from pmd_beamphysics import ParticleGroup, particle_paths
import matplotlib
from pmd_beamphysics.plot import marginal_plot, slice_plot
from pmd_beamphysics.interfaces import opal
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scipy.stats as stats
import numpy as np
matplotlib.rcParams['figure.figsize'] = (8,6)
from h5py import File
import os
H5FILE = 'sc_inj_C1.h5'
h5 = File(H5FILE, 'r')
ph5_group = h5['Step#0']
ph5 = opal.opal_to_data(ph5_group)
P = ParticleGroup(data = ph5)


#Fitting function
def func(x, a, b, c, d):
	return a+b*x+c*x**2+d*x**3
  
xData = P.z
yData = P.pz

#Plot data
plt.plot(xData, yData, 'bo', label='experimental-data')

#Curve-fitting
popt, pcov = curve_fit(func, xData, yData)
print(popt)

#x values for the fit function
#xFit = np.arange(np.amin(xData), np.amax(xData), 1/len(xData))
xFit = np.linspace(np.amin(xData), np.amax(xData), len(xData))

#Plot the fit
plt.plot(xFit, func(xFit, *popt), 'r', label='fit params: a=%3f, b=%3f, c=%3f, d=%3f' % tuple(popt))

stats.chisquare(yData, func(xFit, *popt))

plt.xlabel('z [mm]')
plt.ylabel('pz [MeV/c]')
plt.legend()
#plt.show()
#plt.savefig('./3rd_order_fits/' + H5FILE + '.pdf')
plt.savefig('testplot.pdf')

print(yData.sum())
print(func(xFit, *popt).sum())
