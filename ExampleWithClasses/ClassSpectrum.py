import matplotlib.pyplot as plt
import numpy
import IPython
from astropy.io import fits

class FitsSpectrum():
    def __init__(self,Filename):
        self.Filename = Filename
        self.Flux = fits.getdata(self.Filename)

        #Read in the Header
        self.Header = fits.getheader(self.Filename)

        #Generate the wavelength array based on the HEADER

        Wavelength = []
        for i in range(len(self.Flux)):
            Wavelength.append(self.Header['CRVAL1']+i*self.Header['CDELT1'])

        self.Wavelength = numpy.array(Wavelength)#convert from list to numpy array


    def Rebin(self,Factor):
        #First we rebin the wavelength array
        Split_List = numpy.array_split(self.Wavelength,self.Wavelength.size/Factor)
        Binned = []
        for i in range(len(Split_List)):
            Binned.append(numpy.median( Split_List[i]))

        self.Wavelength = numpy.array(Binned)

        #now we rebin the flux array
        Split_List = numpy.array_split(self.Flux,self.Flux.size/Factor)
        Binned = []
        for i in range(len(Split_List)):
            Binned.append(numpy.median( Split_List[i]))

        Binned = numpy.array(Binned)
        self.Flux = numpy.array(Binned)
