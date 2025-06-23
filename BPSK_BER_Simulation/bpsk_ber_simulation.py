# -*- coding: utf-8 -*-
"""
Created on Mon Jun 23 12:09:12 2025

@author: menna
"""

import numpy as np
import matplotlib.pyplot as plt

def simulate_ber_bpsk_awgn(num_bits=100000, snr_range_db=range(0, 11)):
    # Generate random bits (0 or 1)
    bits = np.random.randint(0, 2, size=num_bits)

    # BPSK Modulation (0 -> -1, 1 -> +1)
    symbols = 2 * bits - 1  # Convert bits to -1 or +1

    ber_list = []

    # Simulate for each SNR
    for snr_db in snr_range_db:
        snr_linear = 10**(snr_db / 10)
        noise_std = 1 / np.sqrt(2 * snr_linear)

        # Generate AWGN noise
        noise = noise_std * np.random.randn(num_bits)

        # Add noise to transmitted symbols
        received = symbols + noise

        # Demodulation
        detected_bits = (received > 0).astype(int)

        # BER Calculation
        num_errors = np.sum(bits != detected_bits)
        ber = num_errors / num_bits
        ber_list.append(ber)

        print(f"SNR = {snr_db} dB, BER = {ber:.5e}")

    # Plot BER vs. SNR (semilog scale)
    plt.figure(figsize=(8, 5))
    plt.semilogy(snr_range_db, ber_list, marker='o', linestyle='-', color='b')
    plt.title('BER vs. SNR for BPSK over AWGN Channel')
    plt.xlabel('SNR (dB)')
    plt.ylabel('Bit Error Rate (BER)')
    plt.grid(True, which='both')
    plt.tight_layout()
    plt.show()

# Run the simulation
simulate_ber_bpsk_awgn()