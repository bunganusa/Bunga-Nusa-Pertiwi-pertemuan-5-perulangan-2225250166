print(" Deret Aritmetika")

# Input suku pertama (a) dan beda (d) sebagai float
a = float(input("Suku pertama a: "))
d = float(input("Beda d: "))

# Input banyak suku (n) sebagai integer
n = int(input("Banyak suku n: "))

# Validasi input n dengan while (harus bilangan bulat positif)
while n <= 0:
    print("n harus bilangan bulat positif (n > 0).")
    n = int(input("Banyak suku n: "))

total = 0.0  # Inisialisasi akumulator jumlah suku

print("\n--- Suku-suku Deret ---")
# Perulangan for untuk menghitung dan menampilkan suku
for i in range(n):
    suku = a + (i * d)
    total += suku
    print(f"Suku ke-{i + 1}: {suku:.2f}")

# Menampilkan total jumlah seluruh suku dengan dua angka di belakang koma
print(f"Jumlah seluruh suku: {total:.2f}")