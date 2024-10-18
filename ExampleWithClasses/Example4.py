import matplotlib.pyplot as plt
import numpy
from astropy.io import fits

from ClassSpectrum import FitsSpectrum

Spectrum = FitsSpectrum('MS_UVB_1D.fits')
Spectrum.Rebin(5)#This modifies Spectrum.Wavelength and Spectrum.Flux

SelectedWavelengths = numpy.where((Spectrum.Wavelength>370)*(Spectrum.Wavelength<560))
plt.plot(Spectrum.Wavelength[SelectedWavelengths],Spectrum.Flux[SelectedWavelengths],'--',lw=2,label = 'UV blue',color='blue')

Spectrum = FitsSpectrum('MS_VIS_1D.fits')
Spectrum.Rebin(5)#This modifies Spectrum.Wavelength and Spectrum.Flux
SelectedWavelengths = numpy.where((Spectrum.Wavelength>560)*(Spectrum.Wavelength<900))
plt.plot(Spectrum.Wavelength[SelectedWavelengths],Spectrum.Flux[SelectedWavelengths],'--',lw=2,label = 'Visual',color='green')

plt.ylim((-1e-17,3e-17))
plt.legend()
plt.xlabel('Wavelength [nm]')
plt.ylabel('Flux')
plt.show()
