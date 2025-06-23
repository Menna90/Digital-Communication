# BPSK Bit Error Rate Simulation over AWGN Channel

This project simulates the Bit Error Rate (BER) performance of a **Binary Phase Shift Keying (BPSK)** system over an **Additive White Gaussian Noise (AWGN)** channel using Python.
It is ideal for students and engineers interested in understanding the performance of digital modulation under noisy conditions.

## 📌 Features

- Simulates BPSK modulation and demodulation
- Adds AWGN based on varying Signal-to-Noise Ratios (SNR)
- Calculates and plots BER vs. SNR
- Easy to run and modify for educational purposes

## 📊 Output

The simulation prints BER values for each SNR in dB and generates a **BER vs. SNR plot** on a semilogarithmic scale.

Example Output:
SNR = 0 dB, BER = 7.83760e-02
SNR = 1 dB, BER = 6.64150e-02
...
SNR = 10 dB, BER = 3.34000e-07

## 🧪 How It Works

1. **Bit Generation**: Random bits (0s and 1s) are generated.
2. **BPSK Modulation**: Bits are mapped to symbols: 0 → -1, 1 → +1.
3. **AWGN Channel**: Gaussian noise is added based on SNR.
4. **Demodulation**: Symbols are decoded back to bits.
5. **BER Calculation**: The number of errors is compared to total bits.
6. **Visualization**: BER vs. SNR is plotted on a log scale.

## 🛠️ Requirements

Make sure you have the following Python packages installed:

- `numpy`
- `matplotlib`
