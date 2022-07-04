from pylab import *
from mpl_toolkits.mplot3d import Axes3D

# Declaring the function to plot a spectrum graph.
def spectrum_plot(fig_no,w,Y,xlimit,Title,ylabel1,ylabel2,Xlabel,Grid=True):
	figure(fig_no)
	subplot(2,1,1)
	plot(w,abs(Y),lw=2)
	xlim([-xlimit,xlimit])
	ylabel(ylabel1,size=16)
	title(Title)
	grid(grid)
	subplot(2,1,2)
	plot(w,angle(Y),'ro',lw=2)
	xlim([-xlimit,xlimit])
	ylabel(ylabel2,size=16)
	xlabel(Xlabel,size=16)
	grid(Grid)

# The below piece of code is for Question.1.
# We to plot a spectrum of sin(sqrt(2)t), in the most basic approximate way.
t = linspace(-pi,pi,65); t = t[:-1]
dt = t[1]-t[0]; fmax = 1/dt
y = sin(sqrt(2)*t)
y[0] = 0 
y = fftshift(y) 
Y = fftshift(fft(y))/64.0
w = linspace(-pi*fmax,pi*fmax,65); w = w[:-1]

spectrum_plot(0,w,Y,10,r"Spectrum of $\sin\left(\sqrt{2}t\right)$",r"$|Y|\rightarrow$",r"Phase of $Y\rightarrow$",r"$\omega\rightarrow$")

# The below piece of code is to plot a spectrum of sin(sqrt(2)t), in a better way after windowing.
t = linspace(-4*pi,4*pi,257); t = t[:-1]
dt = t[1]-t[0]; fmax = 1/dt
n = arange(256)
wnd = fftshift(0.54+0.46*cos(2*pi*n/256))
y = sin(sqrt(2)*t)*wnd
y[0] = 0 
y = fftshift(y) 
Y = fftshift(fft(y))/256.0
w = linspace(-pi*fmax,pi*fmax,257); w = w[:-1]

spectrum_plot(1,w,Y,4,r"Improved Spectrum of $\sin\left(\sqrt{2}t\right)$",r"$|Y|\rightarrow$",r"Phase of $Y\rightarrow$",r"$\omega\rightarrow$")

# The below piece of code is for Question.2.
# We to plot a spectrum of cos^3(0.86t), with and without windowing.
y = cos(0.86*t)**3
y1 = y*wnd
y[0]=0
y1[0]=0
y = fftshift(y)
y1 = fftshift(y1)
Y = fftshift(fft(y))/256.0
Y1 = fftshift(fft(y1))/256.0

spectrum_plot(2,w,Y,4,r"Spectrum of $\cos^{3}(0.86t)$ without Hamming window",r"$|Y|\rightarrow$",r"Phase of $Y\rightarrow$",r"$\omega\rightarrow$")
spectrum_plot(3,w,Y1,4,r"Spectrum of $\cos^{3}(0.86t)$ with Hamming window",r"$|Y|\rightarrow$",r"Phase of $Y\rightarrow$",r"$\omega\rightarrow$")

# The below piece of code is for Question.3. We have to find the values of w0 and delta from the spectrum of the signal.
# Let w0 = 1.5 and delta = 0.5.
w0 = 1.5
d = 0.5

t = linspace(-pi,pi,129)[:-1]
dt = t[1]-t[0]; fmax = 1/dt
n = arange(128)
wnd = fftshift(0.54+0.46*cos(2*pi*n/128))
y = cos(w0*t + d)*wnd
y[0]=0
y = fftshift(y)
Y = fftshift(fft(y))/128.0
w = linspace(-pi*fmax,pi*fmax,129); w = w[:-1]
spectrum_plot(4,w,Y,4,r"Spectrum of $\cos(w_0t+\delta)$ with Hamming window",r"$|Y|\rightarrow$",r"Phase of $Y\rightarrow$",r"$\omega\rightarrow$")

# w0 is calculated by finding the weighted average of all w>0. Delta is found by calculating the phase at w closest to w0.
ii = where(w>=0)
w_cal = sum(abs(Y[ii])**2*w[ii])/sum(abs(Y[ii])**2)
i = abs(w-w_cal).argmin()
delta = angle(Y[i])
print("Calculated value of w0 without noise: ",w_cal)
print("Calculated value of delta without noise: ",delta)

# The below piece of code is for Question.4. We have to find the same for a noisy signal.
y = (cos(w0*t + d) + 0.1*randn(128))*wnd
y[0]=0
y = fftshift(y)
Y = fftshift(fft(y))/128.0
spectrum_plot(5,w,Y,4,r"Spectrum of a noisy $\cos(w_0t+\delta)$ with Hamming window",r"$|Y|\rightarrow$",r"Phase of $Y\rightarrow$",r"$\omega\rightarrow$")

# w0 is calculated by finding the weighted average of all w>0. Delta is found by calculating the phase at w closest to w0.
ii = where(w>=0)
w_cal = sum(abs(Y[ii])**2*w[ii])/sum(abs(Y[ii])**2)
i = abs(w-w_cal).argmin()
delta = angle(Y[i])
print("Calculated value of w0 with noise: ",w_cal)
print("Calculated value of delta with noise: ",delta)

# The below piece of code is for Question.5. 
# We have to plot the spectrum of a "chirped" signal.
t = linspace(-pi,pi,1025); t = t[:-1]
dt = t[1]-t[0]; fmax = 1/dt
n = arange(1024)
wnd = fftshift(0.54+0.46*cos(2*pi*n/1024))
y = cos(16*t*(1.5 + t/(2*pi)))*wnd
y[0]=0
y = fftshift(y)
Y = fftshift(fft(y))/1024.0
w = linspace(-pi*fmax,pi*fmax,1025); w = w[:-1]
spectrum_plot(6,w,Y,100,r"Spectrum of chirped function",r"$|Y|\rightarrow$",r"Phase of $Y\rightarrow$",r"$\omega\rightarrow$")

# The below piece of code is for Question.6.
# We have to plot a surface plot with respect to t and w.
t_array = split(t,16)
Y_mag = zeros((16,64))
Y_phase = zeros((16,64))

for i in range(len(t_array)):
	n = arange(64)
	wnd = fftshift(0.54+0.46*cos(2*pi*n/64))
	y = cos(16*t_array[i]*(1.5 + t_array[i]/(2*pi)))*wnd
	y[0]=0
	y = fftshift(y)
	Y = fftshift(fft(y))/64.0
	Y_mag[i] = abs(Y)
	Y_phase[i] = angle(Y)

t = t[::64]	
w = linspace(-fmax*pi,fmax*pi,64+1); w = w[:-1]
t,w = meshgrid(t,w)

fig1 = figure(7)
ax = fig1.add_subplot(111, projection='3d')
surf=ax.plot_surface(w,t,Y_mag.T,cmap='viridis',linewidth=0, antialiased=False)
fig1.colorbar(surf, shrink=0.5, aspect=5)
ax.set_title('surface plot');
ylabel(r"$\omega\rightarrow$")
xlabel(r"$t\rightarrow$")

show()