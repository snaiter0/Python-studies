import urllib.request
from time import sleep
from urllib.error import HTTPError

page = 9700                                 #Inicia a variavel Pagina, que será a localização onde o programa irá
                                            # consumir a API (Deverá iniciar em 1 para consumir 100% da API)
PaginasSemResposta = 0                      #Numeros de paginas sem resposta
EnderecoDasPaginasComErro =list()                            #Lista de endereços das paginas que não retornarão resposta

while (page != -1):                                          #Laço de repetição para consumir todas as paginas da API
    try:
        webUrl = urllib.request.urlopen(f'http://challenge.dienekes.com.br/api/numbers?page={page}')  #URL da API
                                    # com a variavel "page", capaz de ser substituida, e assim avançar entre as paginas.
        data = webUrl.read()                                    #Função para ler o HTML da pagina
        dado = bytes.decode(data)                               #Função para decodificar os dados, de bytes para string
        semColchete = dado.replace("[", " ")                    #Transformação para o devido consumo dos dados
        semColchete = semColchete.replace("]", " ")
        semColchete = semColchete.replace('"numbers": ', '"')   #Ajustando a string para que a leitura de dados float possa ocorrer devidamente
        semColchete = semColchete.replace('{"', "")
        semColchete = semColchete.replace('}', "")
        espacoAposVirgula = semColchete.split(",")              #Transformando a enorme string em array



                    #------------------------------------------------------------------
                        #Este algoritmo não é de minha autoria, se chama merge sort, no fim do código estou
                        #disponibilizando sua fonte, autoria e mairoes informações de lógica, mas basicamente o código
                        #cria 3 variaveis direita, esquerda e meio. A partir do meio, ele compara 2 valores, e então o
                        #maior soma 1 ponto na variavel direita, e o menor, soma 1 ponto na variavel esquerda.
                        #Ao fim das comparações 1x1, estabelece suas novas ordens, dessa maneira, o código é inumeras
                        #vezes mais eficiente do que um buble sort comum, pois sua lógica não compara o primeiro valor
                        #com todos os outros valores.

        def mergeSort(espacoAposVirgula):
            if len(espacoAposVirgula) > 1:

                # Finding the mid of the array
                mid = len(espacoAposVirgula) // 2

                # Dividing the array elements
                L = espacoAposVirgula[:mid]

                # into 2 halves
                R = espacoAposVirgula[mid:]

                # Sorting the first half
                mergeSort(L)

                # Sorting the second half
                mergeSort(R)

                i = j = k = 0

                # Copy data to temp arrays L[] and R[]
                while i < len(L) and j < len(R):
                    if L[i] < R[j]:
                        espacoAposVirgula[k] = L[i]
                        i += 1
                    else:
                        espacoAposVirgula[k] = R[j]
                        j += 1
                    k += 1

                # Checking if any element was left
                while i < len(L):
                    espacoAposVirgula[k] = L[i]
                    i += 1
                    k += 1

                while j < len(R):
                    espacoAposVirgula[k] = R[j]
                    j += 1
                    k += 1


        # Code to print the list

        def printList(espacoAposVirgula):
            for i in range(len(espacoAposVirgula)):
                print(espacoAposVirgula[i], end=" ")
            print()


        # Driver Code
        if __name__ == '__main__':
            mergeSort(espacoAposVirgula)                #Executa a função merge sort
            print(f"Pagina atual: {page}")              #Exibe a pagina atual consumida
            page += 1                                   #Avança para a execução e a contagem da próxima pagina a ser
                                                        # consumida

            print("Array ordenado: ", end="\n")         #Printa o array ordenado de forma crescente (Pode ser
                                                        # substituido para "numbers" caso seja necessário)
            printList(espacoAposVirgula)



        # Lógica merge sort, utilizei este algoritmo que está disponivel na geeksforgeeks:
            #https://www.geeksforgeeks.org/merge-sort/
                # This code is contributed by Mayank Khanna
                    #---------------------------------------------------------------------------


    except HTTPError:                                         #Cria excecão contra HTTP error 500 internal error
        PaginasSemResposta +=1                                #Conta quantas paginas não retornaram resposta
        print(f"Paginas sem resposta: {PaginasSemResposta}")  #Sinaliza que a pagina não retornou resposta, e exibe
        # quantas paginas tiveram este mesmo erro
        EnderecoDasPaginasComErro.append(page)


    except ValueError:                          #Caso receba um valor nulo ex: (' ')
        print("O valor null não pode ser convertido em float")

    if (len(espacoAposVirgula) <= 1):           #Confere se o array está vazio
        print("")
        print("")                               #Espaçamento para apresentar os dados finais :)
        print("")
        print("A lista foi totalmente consumida.")
        print(f"O numero de paginas sem resposta foi de: {PaginasSemResposta}")
        print("Endereço das paginas sem resposta:")
        print(EnderecoDasPaginasComErro)
        page = -1                               #Condição para sair do laço de repetição
