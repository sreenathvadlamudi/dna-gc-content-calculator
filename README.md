# dna-gc-content-calculator

# 🧬 DNA GC Content Calculator (FASTA-Based)

An interactive **bioinformatics web application** built with **Streamlit** and **Biopython**, designed to analyze **FASTA sequences** and calculate **GC content**, **base composition**, and **GC classification**.

---

## 🧫 Project Overview
This tool allows users to upload DNA sequences in **FASTA format** and visualize the following:

- **GC Content (%)** of each sequence  
- **Nucleotide composition (A/T/G/C%)**  
- **GC level classification** (Low, Moderate, or High GC)  
- **Interactive bar and pie charts**  
- **Downloadable CSV summary of results**

---

## 🧬 Example: TP53 Gene (Homo sapiens)
The included example file `TP53_gene.fasta` represents the **tumor suppressor gene TP53**, known for its role in preventing cancer.

**Reference:**  
- *Official Symbol:* TP53  
- *Organism:* Homo sapiens  
- *RefSeq:* NC_000017.11 (Chromosome 17, GRCh38.p14 Primary Assembly)  

Use it to test the app and visualize GC content from a real human gene sequence.

---

## ⚙️ Installation

```bash
git clone https://github.com/<your-username>/dnagccalculator.git
cd dnagccalculator
pip install -r requirements.txt
