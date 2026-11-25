//#include <stdio.h>
//#include <stdlib.h>
//
//
//
//int main(void) {
//	FILE* arquivo = fopen("letras.txt", "rt");
//
//	if (arquivo == NULL) {
//		printf("Erro ao ler arquivo");
//		exit(1);
//	}
//
//	char frase[40];
//	char caractere;
//
//	while (fgets(frase, sizeof(frase), arquivo) != NULL) {
//		printf("%s", frase);
//	}
//	
//
//	fclose(arquivo);
//
//	return 0;
//}