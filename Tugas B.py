def f(x):
  """
  Fungsi untuk menghitung nilai f(x) = 2x3 + 2x + 15/x.
  Args:
    x: Bilangan bulat sembarang.
  Returns:
    Nilai f(x) untuk x yang diberikan.
  """
  if x == 0:
    return "Tidak terdefinisi"
  else:
    return 2 * x * 3 + 2 * x + 15 / x

# User input
x = int(input("Masukkan bilangan bulat: "))

# Call fungsi
result = f(x)

# Print hasil
print("f(x) =", result)