def tambah_matriks(matriks1, matriks2):
  """
  Menghitung penjumlahan dua buah matriks.
  Args:
    matriks1: Matriks pertama.
    matriks2: Matriks kedua.
  Returns:
    Matriks hasil penjumlahan.
  """

  # memeriksa apakah kedua matriks nya sama
  if len(matriks1) != len(matriks2) or len(matriks1[0]) != len(matriks2[0]):
    raise ValueError("Kedua matriks harus memiliki dimensi yang sama.")

  # fungsi pembuat matriks dengan dimensi yang sama dari hasil penjumlahan
  hasil = [[0 for _ in range(len(matriks1[0]))] for _ in range(len(matriks1))]

  # kalkulasi setiap elemen matriks yang sesuai
  for i in range(len(matriks1)):
    for j in range(len(matriks1[0])):
      hasil[i][j] = matriks1[i][j] + matriks2[i][j]

  return hasil


# matriks acak
matriks1 = [[6, 7, 8], [11, 12, 13]]
matriks2 = [[5, 4, 3], [14, 13, 12]]

# call fungsi
hasil = tambah_matriks(matriks1, matriks2)

# print hasil
print("Matriks 1:")
for baris in matriks1:
  print(baris)

print("\nMatriks 2:")
for baris in matriks2:
  print(baris)

print("\nHasil Penjumlahan:")
for baris in hasil:
  print(baris)