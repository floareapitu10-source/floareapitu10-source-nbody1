import os

# Calea catre fisierul tau de log descarcat din PuTTY
base_dir = os.path.dirname(__file__) if '__file__' in locals() else '.'
cale_fisier = os.path.join(base_dir, 'data', 'mpi_1k.txt')

if not os.path.exists(cale_fisier):
    print(f"❌ Eroare: Nu s-a gasit fisierul la calea: {cale_fisier}")
    print("Asigura-te ca ai copiat 'mpi_1k.txt' in folderul 'data'.")
else:
    linii_tabel = []
    e0 = None
    
    with open(cale_fisier, 'r') as f:
        for linie in f:
            linie_curata = linie.strip().lower()
            if "pas" in linie_curata and "energie" in linie_curata:
                # Spargem linia pentru a extrage valorile numerice
                parti = linie_curata.replace("=", " ").split()
                try:
                    pas = int(parti[1])
                    energie = float(parti[3])
                    
                    # Salvam energia initiala de la Pasul 0 ca referinta
                    if pas == 0:
                        e0 = len(parti) # siguranta in caz de parsare, dar o setam corect dedesubt
                        e0 = energie
                    
                    # Calculam driftul relativ conform formulei matematice
                    if e0 is not None and e0 != 0:
                        drift_relativ = abs((energie - e0) / e0)
                    else:
                        drift_relativ = 0.0
                        
                    linii_tabel.append((pas, linie_curata.split()[2], drift_relativ))
                except (ValueError, IndexError):
                    continue

    # --- AFISAREA TABELULUI IN FORMAT WORD / MARKDOWN ---
    print("\n" + "="*70)
    print(" TABEL DRIFT ENERGIE (PENTRU REFERAT SI SLIDE-UL 9)")
    print("="*70)
    print(f"{'Pas Timp':<12} | {'Energie Totala (E)':<22} | {'Drift Relativ (|dE/E0|)':<25} | {'Status':<8}")
    print("-"*70)
    
    for pas, en_text, drift in linii_tabel:
        # Verificam daca driftul se incadreaza sub pragul de 10^-4 (0.0001) impus la master
        status = "✅ VALID" if drift < 0.0001 else "⚠️ TIMP DT PREA MARE"
        print(f"{pas:<12} | {float(en_text):<22.6e} | {drift:<25.6e} | {status}")
    print("="*70)
