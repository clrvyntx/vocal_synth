import numpy as np
import scipy.fft as fft

def calcular_fft_tramo(t0, tf, fs, audio):
    n0, nf = int(t0*fs), int(tf*fs)+1
    x = audio[n0:nf]
    if len(x) < 4096:
        x = np.append(x, np.zeros(4096 - len(x)))
    return fft.fftshift(fft.fft(x)), fft.fftshift(fft.fftfreq(len(x), 1/fs))

def calcular_fft_pulsos(fs, x):
    return fft.fftshift(fft.fft(x)), fft.fftshift(fft.fftfreq(len(x), 1/fs))
