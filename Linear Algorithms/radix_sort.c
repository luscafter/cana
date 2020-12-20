#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

// https://github.com/luscafter/cana

#define MAX 10

// Função responsável por verificar o maior número do vetor

int bigger(int *v, size_t n)
{
    int maior = v[0];

    for(size_t i = 1; i < n; i++)
        if(maior < v[i])
            maior = v[i];

    return maior;
}

// Função responsável por verificar o menor número do vetor

int smaller(int *v, size_t n)
{
    int menor = v[0];

    for(size_t i = 1; i < n; i++)
        if(menor > v[i])
            menor = v[i];

    return menor;
}

// Função responsável pela ordenação radix sort

void radix_sort(int *v, size_t n)
{
    int i, *output, exp = 1, c[10];

    output = (int *) calloc(n, sizeof(int));

    int maior = bigger(v, n);

    while(maior / exp > 0){
        for(i = 0; i < 10; i++)
            c[i] = 0;

    	for(i = 0; i < n; i++)
    	    c[(v[i] / exp) % 10]++;

    	for(i = 1; i < 10; i++)
    	    c[i] += c[i - 1];

    	for(i = n - 1; i >= 0; i--)
    	    output[--c[(v[i] / exp) % 10]] = v[i];

    	for(i = 0; i < n; i++)
    	    v[i] = output[i];

    	exp *= 10;
    }

    free(output);
}

int main(void)
{
    setlocale(LC_ALL, "Portuguese");

    int v[MAX];

    for(size_t i = 0; i < MAX; i++){
        printf("v[%d] > ", i);
        scanf("%d", &v[i]);
    }

    printf("\nVetor original: [");

    for(size_t i = 0; i < MAX; i++){
        printf("%d", v[i]);
        if(i < MAX - 1)
            printf(", ");
    }

    printf("]\n\nVetor ordenado: [");

    radix_sort(v, MAX);

    for(size_t i = 0; i < MAX; i++){
        printf("%d", v[i]);
        if(i < MAX - 1)
            printf(", ");
    }

    printf("]\n\nMaior número: %d\n\nMenor número: %d\n", bigger(v, MAX), smaller(v, MAX));

    // Ou eu poderia simplesmente imprimir v[0] e v[MAX - 1]

    return EXIT_SUCCESS;
}
