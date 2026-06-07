# Simulator Gravitațional N-Body: Implementare Hibridă C/MPI și Python/Streamlit

---

## 🌌 1. Prezentare Generală
Acest proiect reprezintă o soluție software decuplată de înaltă performanță (HPC) concepută pentru modelarea și vizualizarea interacțiunilor gravitaționale de tip *N-Body*. Sistemul este împărțit în două componente majore:
1. **Backend-ul Computațional (C / MPI):** Execută calculul masiv al forțelor gravitaționale \(\mathcal{O}(N^2)\) utilizând schema numerică simplectică *Leapfrog* cu factor de înmuiere (\(\epsilon\)), optimizat pe un cluster distribuit prin Message Passing Interface.
2. **Interfața Web Analitică (Python / Streamlit):** Randează traiectoriile 3D în timp real utilizând accelerare grafică (Plotly), monitorizează deviația energetică (driftul relativ) și expune rapoarte automate de performanță (Speedup și Eficiență) bazate pe Legea lui Amdahl.

---

## 📁 2. Structura Directorului de Proiect
Proiectul local trebuie organizat după următoarea structură de directoare pentru a asigura maparea automată a datelor:

```text
NBody_Streamlit/
│
├── app.py                      # Aplicația web interactivă (Streamlit)
├── grafice.py                  # Script automatizare rapoarte performanță (Matplotlib)
├── README.md                   # Documentația tehnică curentă
│
└── data/                       # Director pentru stocarea seturilor de date din cluster
    ├── mpi_1k.txt              # Logul text cu metricile energetice pas-cu-pas
    ├── grafice_performanta.png # Graficul generat automat pentru Speedup/Eficiență
    └── snap_*.xyz              # Fişierele de traiectorie 3D (ex: snap_0.xyz, snap_100.xyz)
```

---

## 🚀 3. Ghid de Rulare: Backend Computațional (Server HPC via PuTTY)

### Pasul 3.1: Compilarea Codului Sursă
Conectați-vă la clusterul HPC prin SSH utilizând clientul **PuTTY**. Navigați în directorul de lucru și compilați scriptul în C folosind compilatorul MPI și legătura către biblioteca matematică (`-lm`):
```bash
172.20.21.252
mpicc nbody_mpi.c -o nbody_mpi -lm
```

### Pasul 3.2: Lansarea Simulării în Paralel
Rulați executabilul pe cluster utilizând topologia distribuită. Comanda acceptă următorii parametri de intrare: `[Număr_Particule] [Număr_Pași] [Pas_Timp_dt] [Factor_Înmuiere_Epsilon]`.

Exemplu de rulare pe **4 nuclee fizice** pentru **10.000 de corpuri**:
```bash
mpirun -np 4 ./nbody_mpi 10000 1000 0.01 0.01
```
*În urma execuției, backend-ul va exporta periodic fișierele de log în directorul local de pe cluster.*

### Pasul 3.3: Transferul Datelor pe Mașina Locală
Deschideți clientul **WinSCP** (sau orice client SFTP securizat), conectați-vă la server și transferați fișierele rezultate (`mpi_1k.txt` și snapshot-urile `snap_*.xyz`) din cluster direct în folderul local `data/` al aplicației.

---

## 🖥️ 4. Ghid de Rulare: Interfața Vizuală Locală (Python)

### Pasul 4.1: Instalarea Dependențelor
Asigurați-vă că aveți instalat Python 3.9+. Deschideți o consolă (Terminal / Command Prompt) în folderul rădăcină `NBody_Simulator/` și instalați pachetele software necesare:
```bash
pip install streamlit pandas numpy plotly matplotlib
```

### Pasul 4.2: Generarea Graficelor de Performanță HPC
Înainte de a lansa interfața web, executați scriptul de automatizare pentru a genera hărțile de scalabilitate din timpii măsurați experimental prin `MPI_Wtime()`:
```bash
python grafice.py
```
*Acest pas va genera fișierul `data/grafice_performanta.png`.*

### Pasul 4.3: Lansarea Interfeței Streamlit
Porniți serverul web local dedicat vizualizării analitice prin comanda standard:
```bash
python -m streamlit run app.py
```
Aplicația se va deschide automat în browserul dumneavoastră la adresa implicită `http://localhost:8501`.

Network URL: http://172.20.51.8:8501

## 📊 5. Structura și Funcționalitățile Aplicației Web

Aplicația este structurată pe trei module independente accesibile din meniul central:

1. **🌌 Vizualizare Spațială 3D (Tab-ul 1):**
   * Încarcă fișierele structurate `.xyz` mapate într-un spațiu tridimensional interactiv cu fundal cosmic.
   * Panou cinematic cu butoane automate (`▶️ Start`, `⏸️ Pauză`, `🔄 Reset`) și slider de timp bazat pe starea sesiunii (`st.session_state`).
   * **Optimizare UX:** Include un slider în Sidebar pentru sub-eșantionarea particulelor randate simultan, prevenind blocarea browserului la scenarii de $N=10.000$.

2. **📈 Monitorizare Energie & Performanță (Tab-ul 2):**
   * Parsează automat logul `mpi_1k.txt` și calculează dinamic deviația relativă a energiei raportată la Pasul 0.
   * Afișează un tabel academic prevăzut cu statusuri binare inteligente și alertă vizuală prin coduri de culori (CSS Styler) pentru instabilitățile critice cauzate de efectele de praștie gravitațională.
   * Încarcă direct raportul grafic de Speedup și Eficiență generat de `grafice.py`.

3. **📊 Inspecție Date Brute (Tab-ul 3):**
   * Afișează matricea curentă de coordonate carteziene și mase sub forma unui tabel dinamic optimizat (paginat la 500 de rânduri pentru protecția memoriei RAM).
   * Oferă un buton nativ de descărcare (`st.download_button`) care exportă instantaneu setul complet în format `.csv` pentru audit sau analiză externă (MATLAB/Excel).

---

## 📝 6. Autori și Licență
* **Autor:** Pîțu Floarea, Student Master SIC (Stiinta si Ingineria Calculatoarelor)
* **Destinație:** Proiect de Cercetare Aplicată în cadrul disciplinelor HPC / Calcul Numeric Distribuit.
