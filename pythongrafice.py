import matplotlib.pyplot as plt
import numpy as np
import os

# 1. Datele experimentale colectate din PuTTY
procesoare = np.array([1, 2, 4, 8, 16])
timpi_reali = np.array([240.8, 124.2, 65.1, 38.4, 26.2]) 

# 2. Calculul metricilor de performanta
t1 = timpi_reali[0]
speedup_real = t1 / timpi_reali
speedup_ideal = procesoare
eficienta_real = (speedup_real / procesoare) * 100

# 3. Generarea panoului grafic
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle("Analiza Scalabilitatii Paralele (Strong Scaling: N=10.000)", fontsize=14, fontweight='bold')

# Graficul 1: Speedup
ax1.plot(procesoare, speedup_real, 'o-', linewidth=2, color='#00adb5', label='Speedup Real (MPI)')
ax1.plot(procesoare, speedup_ideal, '--', linewidth=1.5, color='#ff5722', label='Speedup Ideal (Liniar)')
ax1.set_xlabel("Numar Procesoare (P)", fontsize=11)
ax1.set_ylabel("Speedup S = T1 / Tp", fontsize=11)
ax1.set_title("Grafic Speedup", fontsize=12, fontweight='bold')
ax1.set_xticks(procesoare)
ax1.grid(True, linestyle=':', alpha=0.6)
ax1.legend(fontsize=10)

# Graficul 2: Eficienta
ax2.plot(procesoare, eficienta_real, 's-', linewidth=2, color='#3f51b5', label='Eficienta Reala')
ax2.axhline(y=100, linestyle='--', linewidth=1.2, color='gray', label='Eficienta Ideala (100%)')
ax2.set_xlabel("Numar Procesoare (P)", fontsize=11)
ax2.set_ylabel("Eficienta (%)", fontsize=11)
ax2.set_title("Grafic Eficienta", fontsize=12, fontweight='bold')
ax2.set_xticks(procesoare)
ax2.set_ylim(0, 110)
ax2.grid(True, linestyle=':', alpha=0.6)
ax2.legend(fontsize=10)

plt.tight_layout()

# 4. Salvarea automata a imaginii pe disc
os_dir = os.path.dirname(__file__) if '__file__' in locals() else '.'
folder_salvare = os.path.join(os_dir, 'data')
if not os.path.exists(folder_salvare):
    os.makedirs(folder_salvare)

cale_imagine = os.path.join(folder_salvare, 'grafice_performanta.png')
plt.savefig(cale_imagine, dpi=300)
print(f"Grafice salvate in: {cale_imagine}")

plt.show()

