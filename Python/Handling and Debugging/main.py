# 
# Exception Handling adalah mekanisme untuk menangani error yang terjadi saat program dijalankan.
# Bertujuan untuk:
# Menghindari crash program.
# Menangani situasi error dengan cara yang terkontrol.

#Syntax Error: Kesalahan dalam aturan sintaks.
# Runtime Error: Kesalahan yang terjadi saat program berjalan.
# Logical Error: Program berjalan tanpa error tetapi memberikan hasil yang salah.

# Terdiri dari tiga blok utama:
# Try: Blok kode yang mungkin menyebabkan error.
# Catch (C++) atau Except (Python): Blok untuk menangani error.
# Finally (opsional di Python): Blok yang selalu dijalankan.

#Conoth Exception Handling
try:
    a = 10
    b = 0
    hasil = a / b
except ZeroDivisionError as e:
    print("Error: Pembagian dengan nol tidak diperbolehkan.", e)
    
finally:
    print("Program selesai.")
    
#=======================================================================



