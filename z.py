# if __name__== "__main__":
# 	MAX_PESAN = 160
# 	i = range(0,7)
# 	pesan=raw_input("Masukan pesan yang disandikan : \n\n\t")
# 	jum_pesan = len(pesan)
# 	if jum_pesan > MAX_PESAN:
# 		print "\n\nPesan yang dimasukan terlalu panjang!!, silahkan ulangi lagi\n\n\n"
# 	elif jum_pesan == 0:
# 		print "\n\nTidak ada pesan yang Anda masukan, silahkan ulangi lagi!!\n\n\n\n"
# 		for i in range(7):
# 			if i == 0 :
# 				baris = kolom = 6
# 				isi_matrix(0,"tengah")
# 	else:
# 		batas_kanan = batas_bawah = 6.join(str(i))
# 		batas_kiri = batas_atas = 6 - i
# 		baris = 7-i
# 		kolom = batas_kanan
# 		isi_matrix(batas_bawah,"bawah")
# 		isi_matrix(batas_bawah,"kiri")
# 		isi_matrix(batas_bawah,"atas")
# 		isi_matrix(batas_bawah,"kanan")
#
# 	print "\n\n\n=======================Matrix Enkripsi=======================\n\n"
# 	for i in range(13):
# 		print " "
# 		for j in range(13):
# 			print matrix[i][j]
# 		print "\n"
#
# 	print "\n=====================================================================\n\n"
# 	print "\n\nHasil Pesan yang telah disandikan : \n"
# 	for i in range(13):
# 		for j in range(13):
# 			if matrix[i][j] !=' ':
# 				print matrix[i][j]

import numpy as np

class CustomIndexTable:
    def __init__(self, rows, columns, elements):
        self.rows = rows
        self.columns = columns
        self.data = np.array(elements, dtype=object)
        self.data = self.data.reshape((len(rows), len(columns)))

    def __getitem__(self, index):
        x, y = index[:2], index[2:]
        return self.data[self.rows.index(x),self.columns.index(y)]

    def __setitem__(self, index, element):
        x, y = index[:2], index[2:]
        self.data[self.rows.index(x),self.columns.index(y)] = element

    def _where(self, element):
        x, y = np.where(self.data == element)
        return self.rows[x] + self.columns[y]

    def transpose(self):
        self.rows, self.columns = self.columns, self.rows
        self.data = self.data.T

    def where(self, sequence):
        elements = []
        start = 0
        for end in xrange(1, len(sequence)+1):
            if sequence[start:end] in self.data:
                elements.append(sequence[start:end])
                start = end
        return ''.join(self._where(e) for e in elements)

def input_matrix_data(text):
    return raw_input(text).split()

col_indices = input_matrix_data("Column indices: ")
row_indices = input_matrix_data("Row indices: ")
data = input_matrix_data("All data, sorted by row: ")

table = CustomIndexTable(row_indices, col_indices, data)
