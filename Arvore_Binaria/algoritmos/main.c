// Dada a definição de árvore binária, como seriam os algoritmos para
// realizar as seguintes tarefas:

//1- Listar os valores de cada nó da árvore de forma crescente

//2- Listar os valores de cada nó da árvore de forma decrescente
//3- Buscar por um elemento na árvore dado o valor de uma chave

#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
	int valor;
	struct Node *esquerda;
	struct Node *direita;

} Node;

// 1 - Listar os valores de cada nó da árvore em ordem crescente

void emOrdem(Node *raiz){
	if(raiz != NULL){
		emOrdem(raiz -> esquerda);
		printf("%d ",raiz -> valor);
		emOrdem(raiz -> direita);
	}
}

// 2 - Listar os valores em cada nó da árvore em ordem decrescente

void emOrdemDecrescente(Node *raiz){
	if (raiz != NULL){
		emOrdemDecrescente(raiz -> direita);
		printf("%d ", raiz -> valor);
		emOrdemDecrescente(raiz -> esquerda);
	}
}

// 3- Buscar um elemento na árvore binária dado um valor de chave

Node* buscar(Node *raiz, int chave){
	if (raiz == NULL || raiz->valor ==chave)
		return raiz;
	if (chave< raiz->valor)
		return buscar(raiz->esquerda,chave);
	else
		return buscar(raiz->direita,chave);
}


// Função para inserir  na Árvore Binária de busca

Node* inserir(Node *raiz,int valor){
	if (raiz == NULL){
		Node *novo = (Node*)malloc(sizeof(Node));
		novo ->valor = valor;
		novo ->esquerda = NULL;
		novo ->direita = NULL;
		return novo;
	}
	if (valor < raiz -> valor){
		raiz->esquerda = inserir(raiz->esquerda,valor);
	
	}
	else
		raiz-> direita = inserir(raiz->direita,valor);
	return raiz;
}

// Exemplo de uso completo

int main() {
    Node *raiz = NULL;
    raiz = inserir(raiz, 10);
    raiz = inserir(raiz, 5);
    raiz = inserir(raiz, 15);
    raiz = inserir(raiz, 3);
    raiz = inserir(raiz, 7);
    raiz = inserir(raiz, 12);
    raiz = inserir(raiz, 20);

    printf("Em ordem crescente: ");
    emOrdem(raiz);
    printf("\n");

    printf("Em ordem decrescente: ");
    emOrdemDecrescente(raiz);
    printf("\n");

    int chave = 7;
    Node *resultado = buscar(raiz, chave);
    if (resultado != NULL)
        printf("Valor %d encontrado na árvore.\n", chave);
    else
        printf("Valor %d não encontrado na árvore.\n", chave);

    return 0;
}

