# Vowel Synthesizer with PSOLA

This project synthesizes vowels using **glottal pulses** filtered with formant frequencies, and allows **pitch manipulation** with the **PSOLA algorithm**. You can generate any of the five main vowels, save them as WAV files, and visualize their frequency spectra.  

## Features

- Generate vowels `[a, e, i, o, u]` using glottal pulse modeling.
- Apply vocal tract filters based on formants.
- Normalize and save synthesized audio.
- Pitch shift using **PSOLA** (expand/compress pulses).
- Visualize FFTs of original and pitch-shifted vowels.

## Requirements

- Python 3.10+  
- Libraries: `numpy`, `scipy`, `matplotlib`  

Install dependencies with:

```bash
pip install numpy scipy matplotlib
```

## Usage

Run the main script:

```bash
python main.py
```

You will be prompted to choose a vowel:

```
Choose a vowel (a, e, i, o, u):
```

The script will generate:

- `vocal_<vowel>.wav` → original synthesized vowel
- `vocal_psola_exp_<vowel>.wav` → pitch-expanded vowel
- `vocal_psola_comp_<vowel>.wav` → pitch-compressed vowel

It will also plot the FFT of the original and pitch-shifted vowels.

