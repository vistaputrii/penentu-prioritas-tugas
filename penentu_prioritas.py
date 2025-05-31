import streamlit as st
import pandas as pd

st.title("Penentu Urutan Tugas Berdasarkan Prioritas")

# Skor jenis tugas
jenis_tugas_dict = {
    "Skripsi": 7,
    "Artikel / Laporan penting": 7,
    "Harian": 6,
    "Presentasi pribadi": 6,
    "Kelompok": 5,
    "Belajar mandiri": 5,
    "Hobi": 3,
    "Nongkrong": 2,
    "Rapat": 2
}

# Skor deadline
deadline_dict = {
    "0 - 2 hari": 2,
    "3 - 4 hari": 1,
    "5 - 7 hari": 0
}

# Input jumlah tugas
jumlah_tugas = st.number_input("Masukkan jumlah tugas yang ingin dinilai:", min_value=1, step=1)

# Tempat menyimpan data
data_tugas = []

for i in range(jumlah_tugas):
    st.subheader(f"Tugas {i + 1}")
    nama = st.text_input(f"Nama Tugas {i + 1}", key=f"nama_{i}")
    jenis = st.selectbox(f"Jenis Tugas {i + 1}", list(jenis_tugas_dict.keys()), key=f"jenis_{i}")
    deadline = st.selectbox(f"Deadline Tugas {i + 1}", list(deadline_dict.keys()), key=f"deadline_{i}")

    if nama:
        jenis_score = jenis_tugas_dict[jenis]
        deadline_score = deadline_dict[deadline]
        total_score = jenis_score + deadline_score

        # Klasifikasi berdasarkan total score
        if total_score >= 8:
            kategori = "Penting - Mendesak"
        elif total_score >= 4:
            kategori = "Penting - Tidak Mendesak"
        elif total_score >= 2:
            kategori = "Tidak Penting - Mendesak"
        else:
            kategori = "Tidak Penting - Tidak Mendesak"

        data_tugas.append({
            "Nama Tugas": nama,
            "Jenis": jenis,
            "Deadline": deadline,
            "Skor Total": total_score,
            "Kategori": kategori
        })

# Tampilkan tabel
if data_tugas:
    df = pd.DataFrame(data_tugas)
    df_sorted = df.sort_values(by="Skor Total", ascending=False).reset_index(drop=True)
    st.subheader("Tabel Urutan Prioritas Tugas")
    st.dataframe(df_sorted)


