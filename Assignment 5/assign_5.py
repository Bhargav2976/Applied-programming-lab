from pylab import *
import mpl_toolkits.mplot3d.axes3d as p3
import sys
# Initalising required parameers with default values
Nx = 25
Ny = 25
radius = 8
Niter = 1500

# Creating the Matrix
phi = zeros((Nx,Ny))
x = linspace(-0.5,0.5,Nx)
y = linspace(-0.5,0.5,Ny)
n = arange(Niter)
X,Y = meshgrid(x,-y)

# finding coordinates of points inside a given radius
A = X*X + Y*Y 
ii = where(A <= (0.35*0.35))

# setting value of phi to 1 at those points
phi[ii] = 1.0

# Iterations
errors = empty((Niter,1))
for k in range(Niter):
    oldphi = phi.copy()
    phi[1:-1,1:-1] = 0.25*(phi[1:-1,0:-2] + phi[1:-1,2:] + phi[0:-2,1:-1] + phi[2:,1:-1])

# Boundary conditions
    phi[1:-1,0] = phi[1:-1,1]
    phi[1:-1,-1] = phi[1:-1,-2]
    phi[0,1:-1] = phi[1,1:-1]
    phi[ii] = 1.0
    errors[k] = (abs(phi-oldphi)).max()

# Exponent part of the error values    
c_approx_500 = lstsq(c_[ones(Niter-500),arange(500,Niter)],log(errors[500:]),rcond =None)
a_500,b_500 = exp(c_approx_500[0][0]), c_approx_500[0][1]

print("The values of A and B for interations after 500 are:",a_500,b_500)

c_approx = lstsq(c_[ones(Niter),arange(Niter)],log(errors),rcond=None)
a,b = exp(c_approx[0][0]), c_approx[0][1]
print("The values of A and B are: ",a ,b)

# Current density vector calculations
Jx = zeros((Ny, Nx))
Jy = zeros((Ny, Nx))
Jx[1:-1, 1:-1] = 0.5*(phi[1:-1, 0:-2] - phi[1:-1, 2:])
Jy[1:-1, 1:-1] = 0.5*(phi[2:, 1:-1] - phi[0:-2, 1:-1])

# plotting vector plot of currents
figure(0)
quiver(X,Y,Jx,Jy)
plot(ii[0]/Nx - 0.48, ii[1]/Ny -0.48,'ro')
title("Vector plot of Current flow")
xlabel(r'$X\rightarrow$')
ylabel(r'$Y\rightarrow$')

#plotting initial potential contour
figure(1)
plot(ii[0]/Nx - 0.48, ii[1]/Ny - 0.48, 'ro',label = "V = 1")
title("Initial Potential Contour")
xlim(-0.5,0.5)
ylim(-0.5,0.5)
xlabel(r'$X\rightarrow$')
ylabel(r'$Y\rightarrow$')
grid(True)
legend()

# Plotting of error vs iteration in semilog
figure(2)
semilogy(n,errors)
title("Error vs iteration")
xlabel(r'$Iteration\rightarrow$', size = 15)
ylabel(r'$Error\rightarrow$', size = 15)
grid(True)

# Plotting of error vs iteration in loglog
figure(3)
loglog(n,errors)
title("Error vs iteration in loglog plot")
xlabel(r'$Iteration\rightarrow$',size = 15)
ylabel(r'$Error\rightarrow$',size=15)
grid(True)

# Plotting error vs iteration above 500 in semilog
figure(4)
semilogy(n[500:],errors[500:])
title("Error vs Iteration above 500")
xlabel(r'$Iteration\rightarrow$',size=15)
ylabel(r'$Error\rightarrow$', size = 15)
grid(True)

# Plotting actuall and expected error in semilog for above 500 iterations
figure(5)
semilogy(n[500:],errors[500:],label = "Actual")
semilogy(n[500:],a_500*exp(b_500*n[500:]),label = "Expected")
title("Expected vs Actual error(>500 iterations)")
xlabel(r'$Iteration\rightarrow$',size = 15)
ylabel(r'$Error\rightarrow$',size = 15)
grid(True)
legend()

# Plotting of actual and expected error in semilog
figure(6)
semilogy(n,errors,label = "Acyual")
semilogy(n,a*exp(b*n),label="Expected")
title("Expected versus actual error")
xlabel(r'$Iteration\rightarrow$',size=15)
ylabel(r'$Error\rightarrow$', size=15)
grid(True)

# Plotting of the contour of phi (potential).
figure(7)
contourf(X,Y,phi)
plot(ii[0]/Nx-0.48,ii[1]/Ny-0.48,'ro',label="V = 1")
title("Contour plot of potential")
xlabel(r'$X\rightarrow$')
ylabel(r'$Y\rightarrow$')
colorbar()
grid(True)
legend()

# Plotting the surface plots of phi (potential).
fig1=figure(8)
ax=p3.Axes3D(fig1) 
title("The 3-D surface plot of the potential")
xlabel(r'$X\rightarrow$')
ylabel(r'$Y\rightarrow$')
surf = ax.plot_surface(X, Y, phi, rstride=1, cstride=1, cmap=cm.jet)
fig1.colorbar(surf)

show()
exit()