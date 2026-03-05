import numpy as np
import scipy.signal as sgn

def p(F, B, fs):
    return np.exp(-2*np.pi*B/fs) * np.exp(2j*np.pi*F/fs)

def polos_vocal(vocal, fs):
    polos = np.empty(8, dtype=np.clongdouble)
    for i in range(4):
        polos[2*i] = p(vocal[0][i], vocal[1][i], fs)
        polos[2*i+1] = np.conj(polos[2*i])
    return polos

def forma_sos_filtro(polos):
    sos = np.empty([4,6])
    for i in range(4):
        sos[i] = [1,0,0,1,-2*np.real(polos[2*i]), np.abs(polos[2*i])**2]
    return sos

def aplicar_filtro(sos, x):
    return sgn.sosfilt(sos, x)
