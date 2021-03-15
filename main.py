from Integral import Integral
e=1/(10**2)
space=[0,1]
n = 1
integ = Integral(e, space)
print(integ.play())
print(integ.Upp - integ.Low)
print((integ.Upp + integ.Low)/2)