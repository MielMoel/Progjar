def hitungan_nilai(nilai):
    """Calculates the letter skor, bobot, and kategori based on the given score.

    Args:
        nilai: Integer yang merepresentasikan nilai keseluruhan

    Returns:
        skor, bobot, and kategori.
    """
    if 81 <= nilai <= 100:
        return ("A", 4, "Istimewa")
    elif 71 <= nilai <= 80:
        return ("AB", 3.5, "Sangat baik")
    elif 66 <= nilai <= 70:
        return ("B", 3, "Baik")
    elif 61 <= nilai <= 65:
        return ("BC", 2.5, "Cukup baik")
    elif 56 <= nilai <= 60:
        return ("C", 2, "Cukup")
    elif 41 <= nilai <= 55:
        return ("D", 1, "Kurang")
    elif 0 <= nilai <= 40:
        return ("E", 0, "Sangat kurang")
    else:
        return ("Nilai invalid", None, None)

# user input
nilai = int(input("Masukkan nilai: "))

# Call fungsi
skor, bobot, kategori = hitungan_nilai(nilai)

# Print hasil
print(f"Nilai anda adalah {nilai}, dengan bobot {bobot} dan tipe kategori {kategori}")