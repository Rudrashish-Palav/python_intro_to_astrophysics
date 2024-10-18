import numpy,IPython
import matplotlib.pyplot as plt
import matplotlib
#Matplotlib stuff
cmap = matplotlib.cm.get_cmap('rainbow')

####################################
####### Initial conditions #########
####################################

#We will work in cgs units, where the gravitational constant is
G = 6.67430e-8#cgs

#The sun is centered at x,y,z = 0.0,0.0,0.0. It has a mass of
Msun = 1.9891e33#gram

#The earth is 1.5e6 km away from the Sun. We define its initial position as being along the x-axis. We will work in cgs units here:
x = 14959787070000.0#cm
y = 0.0#cm
z = 0.0#cm
r = numpy.sqrt(x**2+y**2+z**2)

Mearth = 5.972E27# gram

#We set the y-coordinate equal to the circular orbit velocity:
vcirc = numpy.sqrt(G*Msun / r)
vx = 0.0
vy = vcirc
vz = 0.0

####################################
##### Running the simulations ######
####################################
torbit = 2*numpy.pi*r/vcirc#an  analytical value for the orbital time
dt = 0.025* torbit#we set the timestep, dt, to 2.5 percent of an orbital time
tmax = 50.0*torbit#We only run simulation for 1 orbit.

t = 0.0# we start at t=0.0

while t<tmax:
    #Calculate coordinates at t+dt
    x += vx*dt
    y += vy*dt
    z += vz*dt

    #Calculate Earths acceleration for the new coordinates
    r = numpy.sqrt(x**2+y**2+z**2)
    F = - G * Msun * Mearth / r**2
    ax = F/Mearth * x/r
    ay = F/Mearth * y/r
    az = F/Mearth * z/r

    #Calculate velocity at new coordinates
    vx += ax*dt
    vy += ay*dt
    vz += az*dt

    plt.plot(x,y,'.',color=cmap(t/tmax))

    #we are now dt further than before
    t += dt

plt.plot(0.0,0.0,'o',color='yellow',ms=20)

plt.xlabel('$x$ [cm]')
plt.ylabel('$y$ [cm]')
plt.axis('equal')
plt.show()
