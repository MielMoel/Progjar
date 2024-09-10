import random
from statistics import median, mode

def hitung_rata_rata(bilangan):
    """
    Fungsi untuk menghitung rata-rata dari daftar bilangan bulat.
    Args:
        bilangan: Daftar bilangan bulat.
    Returns:
        Rata-rata dari bilangan bulat.
    """
    return sum(bilangan) / len(bilangan)

def hitung_median(bilangan):
    """
    Fungsi untuk menghitung median dari daftar bilangan bulat.

    Args:
        bilangan: Daftar bilangan bulat.

    Returns:
        Median dari bilangan bulat.
    """
    return median(bilangan)

def hitung_modus(bilangan):
    """
    Fungsi untuk menghitung modus dari daftar bilangan bulat.
    Args:
        bilangan: Daftar bilangan bulat.
    Returns:
        Modus dari bilangan bulat. Jika tidak ada modus, akan mengembalikan pesan.
    """
    try:
        return mode(bilangan)
    except:
        return "Tidak ada modus yang jelas, semua nilai unik."

# Input User
bilangan = []
for i in range(10):
    angka = int(input(f"Masukkan bilangan bulat ke-{i+1}: "))
    bilangan.append(angka)

# Tiga bilangan acak
bilangan_acak = random.sample(bilangan, 3)

# Rata-rata, median, modus dari tiga bilangan acak
rata_rata = hitung_rata_rata(bilangan_acak)
nilai_median = hitung_median(bilangan_acak)
nilai_modus = hitung_modus(bilangan_acak)

# Print hasil
print("\nBilangan yang dimasukkan:", bilangan)
print("Bilangan yang dipilih secara acak:", bilangan_acak)
print("Rata-rata dari 3 bilangan acak:", rata_rata)
print("Median dari 3 bilangan acak:", nilai_median)
print("Modus dari 3 bilangan acak:", nilai_modus)