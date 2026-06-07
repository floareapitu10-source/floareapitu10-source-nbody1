# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import os
procesoare = np.array([1, 2, 4, 8, 16])
timpi_reali = np.array([240.8, 124.2, 65.1, 38.4, 26.2])
t1 = timpi_reali[0]
speedup_real = t1 / timpi_reali
speedup_ideal = procesoare
eficienta_real = (speedup_real / procesoare) * 100
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('Analiza Scalabilitatii Paralele (Strong Scaling: N=10.000)', fontsize=14, fontweight='bold')
ax1.plot(procesoare, speedup_real, 'o-', linewidth=2, color='#00adb5', label='Speedup Real (MPI)')
ax1.plot(procesoare, speedup_ideal, '--', linewidth=1.5, color='#ff5722', label='Speedup Ideal (Liniar)')
ax1.set_xlabel('Numar Procesoare (P)')
ax1.set_ylabel('Speedup S = T1 / Tp')
ax1.set_title('Grafic Speedup')
ax1.set_xticks(procesoare)
ax1.grid(True)
ax1.legend()
ax2.plot(procesoare, eficienta_real, 's-', linewidth=2, color='#3f51b5', label='Eficienta Reala')
ax2.axhline(y=100, linestyle='--', color='gray')
ax2.set_xlabel('Numar Procesoare (P)')
ax2.set_ylabel('Eficienta (%)')
ax2.set_title('Grafic Eficienta')
ax2.set_xticks(procesoare)
ax2.set_ylim(0, 110)
ax2.grid(True)
ax2.legend()
plt.tight_layout()
os_dir = os.path.dirname(__file__) if '__file__' in locals() else '.'
folder_salvare = os.path.join(os_dir, 'data')
if not os.path.exists(folder_salvare): os.makedirs(folder_salvare)
plt.savefig(os.path.join(folder_salvare, 'grafice_performanta.png'), dpi=300)
print('Grafice generate cu succes!')
plt.show()
