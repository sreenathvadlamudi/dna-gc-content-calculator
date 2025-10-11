import streamlit as st
from Bio import SeqIO
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

st.set_page_config(page_title="DNA GC Content Calculator", page_icon="🧬", layout="wide")

st.title("🧬 DNA GC Content Calculator")
st.write("""
This web application calculates the **GC content** and **nucleotide composition** of DNA sequences.  
You can either paste a DNA sequence directly or upload a FASTA/text file.
""")

# Sidebar info
with st.sidebar:
    st.header("About GC Content")
    st.write("""
    GC content measures the percentage of Guanine (G) and Cytosine (C) bases in DNA.  
    High GC regions are more thermally stable and influence gene expression.
    """)
    st.markdown("---")
    st.write("**Developed by:** Sreenath Vadlamudi")
    st.write("**Powered by:** Streamlit + BioPython")

# Input options
option = st.radio("Select Input Type:", ["Enter Sequence", "Upload File"])

sequences = []

if option == "Enter Sequence":
    seq_input = st.text_area("Enter DNA Sequence(s) (A/T/G/C only):", height=150)
    if seq_input:
        sequences.append(("User_Input_1", seq_input.replace("\n", "").strip()))

elif option == "Upload File":
    uploaded_file = st.file_uploader("Upload FASTA or Text File", type=["fasta", "fa", "txt"])
    if uploaded_file:
        file_content = uploaded_file.read().decode("utf-8")
        st.text_area("📄 File Preview (First 500 characters):", file_content[:500], height=150)
        fasta_io = io.StringIO(file_content)
        for record in SeqIO.parse(fasta_io, "fasta"):
            sequences.append((record.id, str(record.seq)))

if sequences:
    results = []
    for seq_id, seq in sequences:
        seq = seq.upper()
        total_len = len(seq)
        if total_len == 0:
            continue
        g = seq.count("G")
        c = seq.count("C")
        a = seq.count("A")
        t = seq.count("T")
        gc_content = ((g + c) / total_len) * 100

        # Classify GC Content
        if gc_content < 40:
            gc_level = "Low GC"
        elif 40 <= gc_content <= 60:
            gc_level = "Moderate GC"
        else:
            gc_level = "High GC"

        results.append({
            "Sequence_ID": seq_id,
            "Length": total_len,
            "A%": round((a / total_len) * 100, 2),
            "T%": round((t / total_len) * 100, 2),
            "G%": round((g / total_len) * 100, 2),
            "C%": round((c / total_len) * 100, 2),
            "GC_Content (%)": round(gc_content, 2),
            "GC Level": gc_level
        })

    df = pd.DataFrame(results)
    st.subheader("🧩 Sequence Analysis Results")
    st.dataframe(df, use_container_width=True)

    # Visualization
    st.subheader("📊 GC Content Distribution")
    st.bar_chart(df.set_index("Sequence_ID")["GC_Content (%)"])

    # Pie chart for first sequence composition
    st.subheader("🧬 Base Composition (First Sequence)")
    first = df.iloc[0]
    bases = ['A', 'T', 'G', 'C']
    values = [first["A%"], first["T%"], first["G%"], first["C%"]]
    fig, ax = plt.subplots()
    ax.pie(values, labels=bases, autopct='%1.1f%%', startangle=90)
    st.pyplot(fig)

    # Download button for results
    csv_data = df.to_csv(index=False)
    b64 = base64.b64encode(csv_data.encode()).decode()
    st.download_button(
        label="⬇️ Download Results as CSV",
        data=csv_data,
        file_name="gc_content_results.csv",
        mime="text/csv"
    )

else:
    st.info("Please input a sequence or upload a FASTA file to begin.")
