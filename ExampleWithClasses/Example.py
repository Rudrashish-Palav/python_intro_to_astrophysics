import matplotlib.pyplot as plt
import numpy
import IPython
from astropy.io import fits

def Rebin(Array,Factor):
    Split_List = numpy.array_split(Array,Array.size/Factor)
    Binned = []
    for i in range(len(Split_List)):
        Binned.append(numpy.median( Split_List[i]))

    Binned = numpy.array(Binned)
    return Binned


#Read in the flux
Flux = fits.getdata('MS_VIS_1D.fits')

#Read in the Header
Header = fits.getheader('MS_VIS_1D.fits')

#Generate the wavelength array based on the HEADER
Wavelength = []
for i in range(len(Flux)):
    Wavelength.append(Header['CRVAL1']+i*Header['CDELT1'])

Wavelength = numpy.array(Wavelength)#convert from list to numpy array


plt.plot(Wavelength,Flux,'-',lw=3,label = 'Original data')

plt.plot(Rebin(Wavelength,5),Rebin(Flux,5),'--',lw=2,label = 'Rebinned')

plt.legend()
plt.xlabel('Wavelength [nm]')
plt.ylabel('Flux')
plt.ylim((-1e-17,3e-17))
plt.show()
