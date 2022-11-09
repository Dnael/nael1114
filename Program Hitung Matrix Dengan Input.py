#Isi Nama Kelompok Dan Anggota
i=("Kelompok ...")
i2=('''  NAMA     NIM 
	''')
print(i.center(50))
print("_______________________________________________________________")
print("              Nama                      Nim       Kelas")
print(i2)
print("_______________________________________________________________")
#Input Banyak Baris & Kolom
JB = int(input("Masukan Jumlah Baris =  "))
JK = int(input("Masukan Jumlah Kolom =  "))	
#loop Untuk Input Nilai Matrix Pertama
MT1= ('t')
while MT1 == ('t') or MT1 == ('T'):
	print("Matrix Pertama")
	A1 = []
	print("Masukan Nilai Matrix Pertama Secara Berurutan (satu per satu) = ")
	#Input Nilai Baris & Kolom Matrix Pertama
	for i in range(JB):		 
		a =[]
		for j in range(JK):	 
			a.append(int(input()))
		A1.append(a)
	print("_______________________________________________")
	# Print Nilai Matrix Pertama
	for i in range(JB):
		for j in range(JK):
			print(A1[i][j], end = " ")
		print()
	MT1=(str(input("Yakin Nilai Matrix Pertama Sudah Benar  (B/T) =  ")))
#loop Untuk Input Nilai Matrix Kedua
MT2= ('t')
while MT2 == ('t') or MT2 == ('T'):
	print("Matrix Kedua")
	A2 = []
	print("Masukan Nilai Matrix Kedua Secara Berurutan (satu per satu) = ")
	#Input Nilai Baris & Kolom Matrix Kedua
	for i in range(JB):		 
		a =[]
		for j in range(JK):	 
			a.append(int(input()))
		A2.append(a)
	# Print Nilai Matrix Kedua
	print("______________________________________________ ")
	for i in range(JB):
		for j in range(JK):
			print(A2[i][j], end = " ")
		print()
	MT2=(str(input("Yakin Nilai Matrix Kedua Sudah Benar  (B/T) =  ")))
#Pilihan Penjumlahan atau pengurangan
print("_______________________________________________________________")
M3='y'
while M3 == 'y' or M3 == 'Y':
	pilih=(str(input("Pilih Penjumlahan atau Pengurangan   (+/-)   =  ")))
	if pilih == ('+'):
		print("_______________________________________+")
		for i in range(0, len(A1)):
			for j in range(0, len(A1[0])):
				print (A1[i][j] + A2[i][j], end=' ')
			print ()
	elif pilih == ('-'):
		print("_______________________________________-")
		for i in range(0, len(A1)):
			for j in range(0, len(A1[0])):
				print (A1[i][j] - A2[i][j], end=' ')
			print ()
	M3=(str(input("Ingin Mengubah Oprasi Matematika (y/t)  =")))

	
