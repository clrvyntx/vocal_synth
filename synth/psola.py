import numpy as np

def expandir(t0, tf, audio, fs, padding, n):
    n0, nf = int(t0*fs), int(tf*fs)+1
    x = audio[n0:nf]
    x = np.append(x, np.zeros(padding))
    return np.tile(x, n)

def comprimir(t0, tf, audio, fs, overlap, n):
    n0, nf = int(t0*fs), int(tf*fs)+1
    x = audio[n0:nf]
    for i in range(overlap):
        x[i] += x[-(overlap-i)]
    x = x[:-overlap]
    return np.tile(x, n)
