import numpy as np
import matplotlib.pyplot as plt

# Definimos valores simbólicos y parámetros numéricos
tau_val = 0.01  # Constante de tiempo
t0_val = 0.001  # Tiempo inicial del pulso
t1_val = 0.005  # Tiempo final del pulso
Vs_val = 1      # Amplitud del pulso cuadrado

# Frecuencia angular para el diagrama de Bode
frequencies = np.logspace(1, 6, 500)  # Rango de frecuencias (10^1 a 10^6 rad/s)
s_vals = 1j * 2 * np.pi * frequencies  # s = jω

# Expresión de la función de transferencia con los valores numéricos
numerator = (-s_vals * (-s_vals * tau_val * np.exp(t0_val / tau_val) +
                        s_vals * tau_val * np.exp(t1_val / tau_val) +
                        s_vals * tau_val + 1) * 
             np.exp(s_vals * (t0_val + t1_val)))

denominator = ((s_vals * tau_val + 1) * 
               (np.exp(s_vals * t0_val) - np.exp(s_vals * t1_val)))

H_s_vals = numerator / denominator

# Magnitud y fase
magnitude = 20 * np.log10(np.abs(H_s_vals))
phase = np.angle(H_s_vals, deg=True)

# Gráficas del diagrama de Bode
plt.figure(figsize=(12, 8))

# Magnitud
plt.subplot(2, 1, 1)
plt.semilogx(frequencies, magnitude, label='Magnitud')
plt.grid(which="both", linestyle="--", linewidth=0.5)
plt.ylabel("Magnitud (dB)")
plt.title("Diagrama de Bode")

# Fase
plt.subplot(2, 1, 2)
plt.semilogx(frequencies, phase, label='Fase', color='orange')
plt.grid(which="both", linestyle="--", linewidth=0.5)
plt.xlabel("Frecuencia (rad/s)")
plt.ylabel("Fase (°)")

plt.tight_layout()
plt.show()