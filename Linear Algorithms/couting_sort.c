#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <locale.h>

// https://github.com/luscafter/cana

#define MAX 255 // Número máximo de caracteres da tabela ASCII

// Função responsável pela ordenação couting-sort

void counting_sort(char *v)
{
    int i, count[MAX + 1];
    char output[strlen(v)];

    memset(count, '\0', sizeof(count));

    for(i = 0; v[i]; ++i)
        ++count[v[i]];

    for(i = 1; i <= MAX; ++i)
        count[i] += count[i - 1];

    for(i = 0; v[i]; ++i){
        output[count[v[i]] - 1] = v[i];
        --count[v[i]];
    }

    for(i = 0; v[i]; ++i)
        v[i] = output[i];
}

int main(void)
{
    setlocale(LC_ALL, "Portuguese");

    char *text = (char *) malloc(100 * sizeof(char));

    if(text == NULL){
        printf("Não foi possível alocar memória!\n");
        exit(1);
    }

    printf("Informe um texto: ");
    fgets(text, 100, stdin);
    setbuf(stdin, NULL);

    text[strlen(text) - 1] = '\0'; // Elimina o "\n" no final do texto

    printf("\nTexto original: [%s]\n", text);

    counting_sort(text);

    printf("\nTexto ordenado: [%s]\n", text);

    return EXIT_SUCCESS;
}
