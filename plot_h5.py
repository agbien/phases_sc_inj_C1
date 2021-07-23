import pmd_beamphysics
import opal
from pmd_beamphysics import ParticleGroup, particle_paths
import matplotlib
from pmd_beamphysics.plot import marginal_plot, slice_plot
from pmd_beamphysics.interfaces import opal
import matplotlib.pyplot as plt
matplotlib.rcParams['figure.figsize'] = (8,6)
from h5py import File
import os
H5FILE = 'neg30_sc_inj_C1.h5'
h5 = File(H5FILE, 'r')
ph5_group = h5['Step#0']
ph5 = opal.opal_to_data(ph5_group)
P = ParticleGroup(data = ph5)
#plt = P.H5Plotter('px', 'py')
#plt.savefig('test_h5plotter.pdf')

marginal_plot(P, 'z', 'pz', bins=250)
plt.savefig('./espreadplots/neg30_marginal_emit_sliceplot_z_vz_pz.pdf', dpi=200, bbox_inches='tight')

slice_plot(P,  stat_key = 'norm_emit_x', slice_key='z')
plt.savefig('./emitplots/neg30_emit_sliceplot.pdf', dpi=200, bbox_inches='tight')

#xy = plt.hist2d(xtapart.z*10**3, xtapart.pz*10**3, num_bins, facecolor='blue', cmin=1)#, alpha=0.5)
#xy.savefig('2dhist_test')

#import opal
#from opal.opal import load_dataset, filetype
#from opal.visualization.styles import load_style
#from opal.visualization import H5Plotter
#ds = load_dataset('/gpfs/slac/staas/fs1/g/g.beamphysics/abien/lcls-lattice-master/opal/models/sc_inj', fname = 'sc_inj.h5')
#load_style('poster')
#plt = ds.H5plotter('px', 'py')
#plt = ds.plot_phase_space('rms_px', 'rms_py')
#plt.tight_layout()
