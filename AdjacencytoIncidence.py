print("--------------------Selamat datang!-----------------------------")
print("Ketik angka 0 untuk mengubah matriks adjacent menjadi incidental")
print("Ketik angka 1 untuk mengubah matriks incidental menjadi adjacent")
pilihan = int(raw_input("Angka pilihan: "))
if (pilihan == 0) :
    arr2 = []                                                           #Array berisi garis antar simpul
    print("Masukan matriks: ")
    inputBaris = raw_input().split()                                #Masukan di dalam satu baris dibagi-bagi
    jumlahSimpul = len(inputBaris)                                  #Untuk perlakuan pertama tidak masuk loop karena panjang list variabel inputBaris akan digunakan sebagai jumlah dimensi
    for j in range (int(jumlahSimpul)) :
        if (int(inputBaris[j]) != 0) :                              #Mengecek apakah suatu simpul terhubung ke simpul lain atau tidak
            if ((0,j) not in arr2) and ((j,0) not in arr2) :        #Karena matriks simetris dan garis di graf hanya digunakan sekali, maka cukup ambil satu saja
                for k in range(int(inputBaris[j])) :                #Menangani kasus nilai input lebih besar dari 1
                    arr2.append((0,j))
                    
    for i in range (1, int(jumlahSimpul)) :
        inputBaris = raw_input().split()                                #Masukan di dalam satu baris dibagi-bagi
        for j in range (int(jumlahSimpul)) :
            if (int(inputBaris[j]) != 0) :                              #Mengecek apakah suatu simpul terhubung ke simpul lain atau tidak
                if ((i,j) not in arr2) and ((j,i) not in arr2) :        #Karena matriks simetris dan garis di graf hanya digunakan sekali, maka cukup ambil satu saja
                    for k in range(int(inputBaris[j])) :                #Menangani kasus nilai input lebih besar dari 1
                        arr2.append((i,j))

    print("PERHATIAN: Simpul lambang abjad a,b,c,... direpresentasikan dengan lambang angka 0,1,2,...")
    print("PERHATIAN: (a,b) menyatakan bahwa simpul a dan b saling terhubung")
    print("PERHATIAN: Penomoran garis sesuai dengan urutan list hubungan yang terbentuk, dari kiri ke kanan")
    print("Hubungan yang terbentuk: ")
    print(arr2)
    arr3 = {}                                                           #Matriks hasil
    hasil = ""                                                          #Format print matriks
    print("Hasil: ")
    for a in range(int(jumlahSimpul)) :                                 #Jumlah baris sesuai jumlah simpul
        for b in range(len(arr2)) :                                     #jumlah kolom sesuai jumlah garis
            if a in arr2[b] :                                           #Mengecek apakah suatu simpul terlibat dalam masing-masing garis
                arr3[a,b] = 1
            else:
                arr3[a,b] = 0

            hasil += str(arr3[a,b]) + " "
            
        print(hasil)
        hasil = ""                                                      #String kembali kosong untuk print baris selanjutnya
if (pilihan == 1):
    print("Untuk yang incidence ke adjacency belum tersedia, silakan lihat program Adjacency2Incidence+incidence2adjacency.py atau inctoadj.c")
