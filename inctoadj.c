#include <stdio.h>
#include <stdlib.h>

void masukkanmatriksincidence(int** matriks1, int baris, int kolom);
void inisialisasimatriks2(int** matriks2, int baris, int kolom);
void temukanlangsungmasukkan(int** matriks1, int** matriks2, int baris, int kolom);
void printadjacency(int** matriks2, int baris, int kolom);

int main()
{
	int baris, kolom;

	printf("selamat datang di program konversi incidence ke adjacency!\n");
	printf("silakan masukkan jumlah baris: ");
	scanf("%d", &baris);
	printf("silakan masukkan jumlah kolom: ");
	scanf("%d", &kolom);

	// alokasi memori
	int** matriks1 = (int**)malloc(baris * sizeof(int*));

	for (int index=0;index<baris;++index)
	{
    matriks1[index] = (int*)malloc(kolom * sizeof(int));
	}
	int** matriks2 = (int**)malloc(baris * sizeof(int*));

	for (int index=0;index<baris;++index)
	{
    matriks2[index] = (int*)malloc(kolom * sizeof(int));
	}

	masukkanmatriksincidence(matriks1, baris, kolom);
	inisialisasimatriks2(matriks2, baris, kolom);
	temukanlangsungmasukkan(matriks1, matriks2, baris, kolom);
	printadjacency(matriks2, baris, kolom);

	return 0;
}

void masukkanmatriksincidence(int** matriks1, int baris, int kolom)
{
	int i,j;

	for (i=0;i<baris;i++){
		for (j=0;j<kolom;j++){
			scanf("%d", &matriks1[i][j]);
		}
	}
}

void inisialisasimatriks2(int** matriks2, int baris, int kolom)
{
	int i,j;

	for (i=0;i<baris;i++){
		for (j=0;j<kolom;j++){
			matriks2[i][j]=0;
		}
	}
}

void temukanlangsungmasukkan(int** matriks1, int** matriks2, int baris, int kolom)
{
	int tempA=999, tempB=999;
	int i,j;

	for (j=0;j<kolom;j++){
		for(i=0;i<baris;i++){
			if (matriks1[i][j]==1){
				if (tempA==999)
					tempA=i;
				else
					tempB=i;
			}
		}

		matriks2[tempA][tempB]=1;
		matriks2[tempB][tempA]=1;
	}
}

void printadjacency(int** matriks2, int baris, int kolom)
{
	int i,j;
	printf("\nhasil adjacencynya adalah :\n");
	for (i=0;i<baris;i++){
		for (j=0;j<baris;j++){
			printf("%d ", matriks2[i][j]);
		}
		printf("\n");
	}
}