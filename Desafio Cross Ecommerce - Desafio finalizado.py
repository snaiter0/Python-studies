import urllib.request
from urllib.error import HTTPError

db_write= list()
page = 1
PaginasSemResposta = 0
EnderecoDasPaginasComErro =list()

while (page != -1):
    try:
        webUrl = urllib.request.urlopen(f'http://challenge.dienekes.com.br/api/numbers?page={page}')

        #===============================//================================#
                        # Execução da extração e tratamento dos dados
        url = webUrl.read()
        dado = bytes.decode(url)
        semColchete = dado.replace("[", " ")
        semColchete = semColchete.replace("]", " ")
        semNumbers = semColchete.replace('"numbers": ', '"')
        semChaves = semNumbers.replace('{"', "")
        semChaves = semChaves.replace('}', "")
        espacoAposVirgula = semChaves.split(",")

        # ===============================//================================#

        # ===============================//================================#
            #Ordenação dos dados
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


        # ===============================//================================#

        # ===============================//================================#
                    # Exibição da lista dos dados

        def printList(espacoAposVirgula):
            for i in range(len(espacoAposVirgula)):
                print(espacoAposVirgula[i], end=" ")
            print()


        # ===============================//================================#

        # ===============================//================================#
                                #Registro dos dados
        if __name__ == '__main__':
            mergeSort(espacoAposVirgula)
            print(f"Pagina atual: {page}")
            page += 1
            print("Array ordenado: ", end="\n")
            printList(espacoAposVirgula)

            f = open("CrossEcommerce.txt", "a")
            f.write(str(espacoAposVirgula))

        # ===============================//================================#

        # ===============================//================================#
                            #Tratamento de erros de requisição
    except HTTPError:
        PaginasSemResposta +=1
        print(f"Paginas sem resposta: {PaginasSemResposta}")
        # quantas paginas tiveram este mesmo erro
        EnderecoDasPaginasComErro.append(page)

    except ValueError:
        print("O valor null não pode ser convertido em float")

        # ===============================//================================#

        # ===============================//================================#
                        #Laço condicional para finalização do programa
    if (len(espacoAposVirgula) <= 1):
        print("")
        print("A lista foi totalmente consumida.")
        print("")
        print("")
        print(f"O numero de paginas sem resposta foi de: {PaginasSemResposta}")
        print(f"Endereço das paginas sem resposta: {EnderecoDasPaginasComErro}")
        page = -1
        f.close()

    # ===============================//================================#

