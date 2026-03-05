import numpy as np

def u(n):
    return np.heaviside(n,1)

def pulso_glotico(t, p0, tp, tn):
    return (0.5 * p0)*(1 - np.cos(t/tp*np.pi))*(u(t)-u(t-tp)) + \
           p0*np.cos((t-tp)/tn*np.pi/2)*(u(t-tp)-u(t-(tp+tn)))

def muestrear_pulsos_gloticos(t0, p0, tp, tn, fs, n):
    longitud_pulso = int(t0 * fs)
    x = np.array([pulso_glotico(i/fs, p0, tp, tn) for i in range(longitud_pulso)])
    return np.tile(x, n)
