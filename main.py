import os
import matplotlib.pyplot as plt
from synth import glottal, vocal_filter, psola, fft_utils
import scipy.io.wavfile as wav
import numpy as np

# --- CREATE AUDIO FOLDER ---
os.makedirs("./audio", exist_ok=True)

# --- PARAMETERS ---
fs = 16000
f0 = 200        # fundamental frequency
p0 = 200
tp = 0.4 / f0
tn = 0.16 / f0
audio_duration = 1.0           # desired length in seconds
n_cycles = int(f0 * audio_duration)  # number of glottal pulses for duration

# Vowels
vowels = {
    'a': [[830,1400,2890,3930],[110,160,210,230]],
    'e': [[500,2000,3130,4150],[80,156,190,220]],
    'i': [[330,2765,3740,4366],[70,130,178,200]],
    'o': [[546,934,2966,3930],[97,130,185,240]],
    'u': [[382,740,2760,3380],[74,150,210,180]]
}

# --- USER CHOICE ---
vowel_choice = input("Choose a vowel (a, e, i, o, u): ").strip().lower()
if vowel_choice not in vowels:
    print("Invalid choice! Defaulting to 'a'.")
    vowel_choice = 'a'

vocal_formants = vowels[vowel_choice]

# --- GENERATE GLOTTAL PULSES FOR FULL DURATION ---
x = glottal.muestrear_pulsos_gloticos(1/f0, p0, tp, tn, fs, n_cycles)

# --- APPLY VOCAL FILTER ---
polos = vocal_filter.polos_vocal(vocal_formants, fs)
sos = vocal_filter.forma_sos_filtro(polos)
vocal = vocal_filter.aplicar_filtro(sos, x)

# --- NORMALIZE ---
vocal = vocal / np.max(np.abs(vocal))

# --- SAVE WAV ---
wav.write(f"./audio/vocal_{vowel_choice}.wav", fs, (vocal * 32767).astype("int16"))

# --- PSOLA pitch shift ---
padding_expand = 16
padding_compress = 16

vocal_exp = psola.expandir(0, 1/f0, vocal, fs, padding_expand, n_cycles)
vocal_comp = psola.comprimir(0, 1/f0, vocal, fs, padding_compress, n_cycles)

vocal_exp = vocal_exp / np.max(np.abs(vocal_exp))
vocal_comp = vocal_comp / np.max(np.abs(vocal_comp))

wav.write(f"./audio/vocal_psola_exp_{vowel_choice}.wav", fs, (vocal_exp * 32767).astype("int16"))
wav.write(f"./audio/vocal_psola_comp_{vowel_choice}.wav", fs, (vocal_comp * 32767).astype("int16"))

# --- FFTs of full audio duration ---
X_orig = np.fft.fftshift(np.fft.fft(vocal))
f_axis_orig = np.fft.fftshift(np.fft.fftfreq(len(vocal), 1/fs))

X_exp = np.fft.fftshift(np.fft.fft(vocal_exp))
f_axis_exp = np.fft.fftshift(np.fft.fftfreq(len(vocal_exp), 1/fs))

X_comp = np.fft.fftshift(np.fft.fft(vocal_comp))
f_axis_comp = np.fft.fftshift(np.fft.fftfreq(len(vocal_comp), 1/fs))

# --- PLOT ---
plt.figure(figsize=(12,5))
plt.plot(f_axis_orig, np.abs(X_orig), label='Original')
plt.plot(f_axis_exp, np.abs(X_exp), label='Expanded')
plt.plot(f_axis_comp, np.abs(X_comp), label='Compressed')
plt.title(f"FFT over {audio_duration:.1f}s of vowel [{vowel_choice}]")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude")
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()
