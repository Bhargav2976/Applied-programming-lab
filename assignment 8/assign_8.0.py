from sympy import *
from pylab import *

# Declaring the necessary variables and calculating the DFT of sin(5t)
N1 = 128
t1 = linspace(0,2*pi,N1+1); t1 = t1[:-1]
y1 = sin(5*t1)
Y1 = fftshift(fft(y1))/N1
w1 = linspace(-64,63,N1)

# Magnitude plot for the DFT of sin(5t)
figure(0)
plot(w1,abs(Y1))
title(r"Spectrum of $\sin(5t)$")
ylabel(r"$|Y(\omega)|\rightarrow$")
xlabel(r"$\omega\rightarrow$")
xlim([-10,10])
grid(True)

# Phase plot for the DFT of sin(5t)
figure(1)
plot(w1,angle(Y1),'ro')
ii = where(abs(Y1)>1e-3)
plot(w1[ii],angle(Y1[ii]),'go')
title(r"Phase of $\sin(5t)$")
ylabel(r"$\angle Y(\omega)\rightarrow$")
xlabel(r"$\omega\rightarrow$")
xlim([-10,10])
grid(True)

# Declaring the necessary variables and calculating the DFT of (1 + 0.1cos(t))cos(10t)
N2 = 512
t2 = linspace(-4*pi,4*pi,N2+1); t2 = t2[:-1]
y2 = (1 + 0.1*cos(t2))*cos(10*t2)
Y2 = fftshift(fft(y2))/N2
w2 = linspace(-64,64,N2+1); w2 = w2[:-1]

# Magnitude plot for the DFT of (1 + 0.1cos(t))cos(10t)
figure(2)
plot(w2,abs(Y2))
title(r"Spectrum of $(1 + 0.1*cos(t))*cos(10*t)$")
ylabel(r"$|Y(\omega)|\rightarrow$")
xlabel(r"$\omega\rightarrow$")
xlim([-15,15])
grid(True)

# Phase plot for the DFT of (1 + 0.1cos(t))cos(10t)
figure(3)
plot(w2,angle(Y2),'ro')
title(r"Phase of $(1 + 0.1*cos(t))*cos(10*t)$")
ylabel(r"$\angle Y(\omega)\rightarrow$")
xlabel(r"$\omega\rightarrow$")
xlim([-15,15])
grid(True)

# Declaring the necessary variables and calculating the DFT of sin^3(t)
N3 = 512
t3 = linspace(-4*pi,4*pi,N3+1); t3 = t3[:-1]
y3 = (3*sin(t3) - sin(3*t3))/4
Y3 = fftshift(fft(y3))/N3
w3 = linspace(-64,64,N3+1); w3 = w3[:-1]

# Magnitude plot for the DFT of sin^3(t)
figure(4)
plot(w3,abs(Y3))
title(r"Spectrum of $sin^{3}(t)$")
ylabel(r"$|Y(\omega)|\rightarrow$")
xlabel(r"$\omega\rightarrow$")
xlim([-15,15])
grid(True)

# Calculating the DFT of cos^3(t)
y4 = (3*cos(t3) + cos(3*t3))/4
Y4 = fftshift(fft(y4))/N3

# Magnitude plot for the DFT of cos^3(t)
figure(5)
plot(w3,abs(Y4))
title(r"Spectrum of $cos^{3}(t)$")
ylabel(r"$|Y(\omega)|\rightarrow$")
xlabel(r"$\omega\rightarrow$")
xlim([-15,15])
grid(True)

# Calculating the DFT of cos(20t + 5cos(t))
y5 = cos(20*t3 + 5*cos(t3))
Y5 = fftshift(fft(y5))/N3

# Magnitude plot for the DFT of cos(20t + 5cos(t))
figure(6)
plot(w3,abs(Y5))
title(r"Spectrum of $cos(20t + 5cos(t))$")
ylabel(r"$|Y(\omega)|\rightarrow$")
xlabel(r"$\omega\rightarrow$")
xlim([-40,40])
grid(True)

# Phase plot for the DFT of cos(20t + 5cos(t)) where magnitude is greater than 1e-3
figure(7)
ii = where(abs(Y5)>=1e-3)
plot(w3[ii],angle(Y5[ii]),'go')
title(r"Phase of $cos(20t + 5cos(t))$")
ylabel(r"$\angle Y(\omega)\rightarrow$")
xlabel(r"$\omega\rightarrow$")
xlim([-40,40])
grid(True)

# The below piece piece of code is to find out the most accurate DFT of a Gaussian
# exp(-0.5t^2) when compared to its CTFT.
# Declaring all the necessary variables.
T = 2*pi
N = 128
iter = 0
tolerance = 1e-15
error = tolerance + 1

# This loop will calculate the DFT and also the error between the calculated and actual value.
# Only when the error is less than a tolerance value will the loop be terminated.
while True:

	t = linspace(-T/2,T/2,N+1)[:-1]
	w = N/T * linspace(-pi,pi,N+1)[:-1] 
	y = exp(-0.5*t**2)
	iter = iter + 1

	Y = fftshift(fft(y))*T/(2*pi*N)
	Y_actual = (1/sqrt(2*pi))*exp(-0.5*w**2)
	error = mean(abs(abs(Y)-Y_actual))

	if error < tolerance:
		break
	
	T = T*2
	N = N*2

print(" Error: %g \n Interation: %g" % (error,iter))
print(" Best value for T: %g*pi \n Best value for N: %g"%(T/pi,N))

# Magnitude plot for the most accurate DFT of the Gaussian. 
figure(8)
plot(w,abs(Y))
title(r"Spectrum of a Gaussian function")
ylabel(r"$|Y(\omega)|\rightarrow$")
xlabel(r"$\omega\rightarrow$")
grid(True)
xlim([-10,10])

show()