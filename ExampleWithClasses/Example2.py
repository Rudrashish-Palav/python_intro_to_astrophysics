import matplotlib.pyplot as plt
import numpy
import IPython
from astropy.io import fits

from ClassSpectrum import FitsSpectrum

Spectrum = FitsSpectrum('MS_VIS_1D.fits')

#The wavelength and flux can be obtained by writing Spectrum.Wavelength and Spectrum.Flux (Spectrum. here corresponds to self. in ClassSPectrum.py)
plt.plot(Spectrum.Wavelength,Spectrum.Flux,'-',lw=3,label = 'Original data')

Spectrum.Rebin(5)#This modifies Spectrum.Wavelength and Spectrum.Flux
plt.plot(Spectrum.Wavelength,Spectrum.Flux,'--',lw=2,label = 'Rebinned')

plt.ylim((-1e-17,3e-17))
plt.legend()
plt.xlabel('Wavelength [nm]')
plt.ylabel('Flux')
plt.show()
