import streamlit as st

st.set_page_config(page_title='Informasi Atribut', page_icon='ℹ️')
st.title('Informasi Mengenai Atribut Prediksi Kanker Payudara')

st.write("""
Berikut adalah penjelasan mengenai atribut yang digunakan untuk memprediksi apakah kanker payudara bersifat jinak atau ganas:

A. Atribut Mean (Rata-rata)

1. **Radius rata-rata**: Rata-rata jarak dari pusat ke titik terluar tumor
2. **Texture rata-rata**: Rata-rata variasi intensitas permukaan tumor
3. **Perimeter rata-rata**: Rata-rata keliling tumor
4. **Area rata-rata**: Rata-rata luas permukaan tumor
5. **Smoothness rata-rata**: Rata-rata keseragaman tekstur permukaan
6. **Compactness rata-rata**: Rata-rata kekompakan (rapatnya bentuk tumor)
7. **Concavity rata-rata**: Rata-rata cekungan pada permukaan tumor
8. **Concave points rata-rata**: Rata-rata jumlah titik cekungan pada tumor
9. **Symmetry rata-rata**: Rata-rata keseragaman bentuk tumor
10. **Fractal dimension rata-rata**: Rata-rata kompleksitas tepi tumor

B. Atribut SE (Standard Error)

1. **Radius SE**: Standar error jarak dari pusat ke titik terluar tumor
2. **Texture SE**: Standar error variasi intensitas permukaan tumor
3. **Perimeter SE** : Standard error keliling tumor
4. **Area SE**: Standar error luas permukaan tumor
5. **Smoothness SE**: Standar error keseragaman tekstur permukaan
6. **Compactness SE**: Standar error kekompakan (rapatnya bentuk tumor)
7. **Concavity SE**: Standar error cekungan pada permukaan tumor
8. **Concave points SE**: Standar error jumlah titik cekungan pada tumor
9. **Symmetry SE**: Standar error keseragaman bentuk tumor
10. **Fractal dimension SE**: Standar error kompleksitas tepi tumor

C. Atribut Worst (Nilai Terburuk)

1. **Radius worst**: Nilai terburuk jarak dari pusat ke titik terluar
2. **Texture worst**: Nilai terburuk variasi intensitas permukaan
3. **Perimeter worst**: Nilai terburuk keliling tumor
4. **Area worst**: Nilai terburuk luas permukaan tumor
5. **Smoothness worst**: Nilai terburuk keseragaman tekstur permuka
6. **Compactness worst**: Nilai terburuk kekompakan (rapatnya bentuk tumor)
7. **Concavity worst**: Nilai terburuk cekungan pada permukaan
8. **Concave points worst**: Nilai terburuk jumlah titik cekungan
9. **Symmetry worst**: Nilai terburuk keseragaman bentuk tumor
10. **Fractal dimension worst**: Nilai terburuk kompleksitas tepi tumor

Berikut adalah panduan umum tentang rentang nilai masing-masing atribut yang menunjukkan apakah kanker payudara lebih cenderung bersifat jinak (B) atau ganas (M) berdasarkan dataset Wisconsin Diagnostic Breast Cancer (WDBC):

### **A. Atribut Mean (Rata-rata)**

| **Atribut**             | **Rentang Nilai Jinak (B)**   | **Rentang Nilai Ganas (M)**  |
|-------------------------|-------------------------------|------------------------------|
| **Radius rata-rata**     | 6.0 - 10.0                    | > 20.0                       |
| **Texture rata-rata**    | 10.0 - 20.0                   | > 30.0                       |
| **Perimeter rata-rata**  | 40.0 - 80.0                   | > 130.0                      |
| **Area rata-rata**       | 150 - 800                     | > 1500                       |
| **Smoothness rata-rata** | 0.05 - 0.10                   | > 0.15                       |
| **Compactness rata-rata**| 0.00 - 0.10                   | > 0.20                       |
| **Concavity rata-rata**  | 0.00 - 0.10                   | > 0.20                       |
| **Concave points rata-rata** | 0.00 - 0.05                | > 0.10                       |
| **Symmetry rata-rata**   | 0.15 - 0.30                   | < 0.10                       |
| **Fractal dimension rata-rata** | 0.05 - 0.07           | > 0.08                       |

---

### **B. Atribut SE (Standard Error)**

| **Atribut**             | **Rentang Nilai Jinak (B)**   | **Rentang Nilai Ganas (M)**  |
|-------------------------|-------------------------------|------------------------------|
| **Radius SE**           | 0.1 - 1.0                     | > 1.5                        |
| **Texture SE**          | 0.5 - 2.0                     | > 3.0                        |
| **Perimeter SE**        | 0.5 - 2.5                     | > 3.0                        |
| **Area SE**             | 1.0 - 10.0                    | > 20.0                       |
| **Smoothness SE**       | 0.001 - 0.010                 | > 0.015                      |
| **Compactness SE**      | 0.001 - 0.05                  | > 0.05                       |
| **Concavity SE**        | 0.000 - 0.05                  | > 0.05                       |
| **Concave points SE**   | 0.001 - 0.01                  | > 0.02                       |
| **Symmetry SE**         | 0.005 - 0.02                  | > 0.03                       |
| **Fractal dimension SE**| 0.001 - 0.01                  | > 0.02                       |

---

### **C. Atribut Worst (Nilai Terburuk)**

| **Atribut**             | **Rentang Nilai Jinak (B)**   | **Rentang Nilai Ganas (M)**  |
|-------------------------|-------------------------------|------------------------------|
| **Radius worst**        | 10.0 - 20.0                   | > 30.0                       |
| **Texture worst**       | 15.0 - 25.0                   | > 30.0                       |
| **Perimeter worst**     | 70.0 - 120.0                  | > 160.0                      |
| **Area worst**          | 300 - 1000                    | > 2000                       |
| **Smoothness worst**    | 0.10 - 0.20                   | > 0.30                       |
| **Compactness worst**   | 0.10 - 0.20                   | > 0.30                       |
| **Concavity worst**     | 0.00 - 0.15                   | > 0.25                       |
| **Concave points worst**| 0.05 - 0.10                   | > 0.15                       |
| **Symmetry worst**      | 0.20 - 0.40                   | < 0.20                       |
| **Fractal dimension worst** | 0.05 - 0.10               | > 0.15                       |
""")
