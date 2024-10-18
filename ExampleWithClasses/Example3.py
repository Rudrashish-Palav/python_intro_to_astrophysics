import matplotlib.pyplot as plt
import numpy
from astropy.io import fits

from ClassSpectrum import FitsSpectrum

Spectrum = FitsSpectrum('MS_UVB_1D.fits')
Spectrum.Rebin(5)#This modifies Spectrum.Wavelength and Spectrum.Flux
plt.plot(Spectrum.Wavelength,Spectrum.Flux,'--',lw=2,label = 'Rebinned',color='blue')

Spectrum = FitsSpectrum('MS_VIS_1D.fits')
Spectrum.Rebin(5)#This modifies Spectrum.Wavelength and Spectrum.Flux
plt.plot(Spectrum.Wavelength,Spectrum.Flux,'--',lw=2,label = 'Rebinned',color='green')

plt.ylim((-1e-17,3e-17))
plt.legend()
plt.xlabel('Wavelength [nm]')
plt.ylabel('Flux')
plt.show()
