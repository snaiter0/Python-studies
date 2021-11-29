import urllib.request
from time import sleep
from urllib.error import HTTPError

page = 9990
PaginasSemResposta = 0

while (page != -1):
    try:
        webUrl = urllib.request.urlopen(f'http://challenge.dienekes.com.br/api/numbers?page={page}')
        data = webUrl.read()
        dado = bytes.decode(data)
        semColchete = dado.replace("[", " ")
        semColchete = semColchete.replace("]", " ")
        semColchete = semColchete.replace('"numbers": ', '"')
        semColchete = semColchete.replace('{"', "")
        semColchete = semColchete.replace('}', "")
        espacoAposVirgula = semColchete.split(",")
        novo_x = []

        for i in espacoAposVirgula:
            novo_x.append(float(i))

        print(f'Numero da pagina em execução:{page - 1}')


        def mergeSort(novo_x):
            if len(novo_x) < 1:
                mid = len(novo_x) // 2
                lefthalf = novo_x[:mid]
                righthalf = novo_x[mid:]
                print("flag")
                mergeSort(lefthalf)
                mergeSort(righthalf)

                i = 0
                j = 0
                k = 0
            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] < righthalf[j]:
                    novo_x[k] = lefthalf[i]
                    i = i + 1
                else:
                    novo_x[k] = righthalf[j]
                    j = j + 1
                    k = k + 1

            while i < len(lefthalf):
                novo_x[k] = lefthalf[i]
                i = i + 1
                k = k + 1

            while j < len(righthalf):
                novo_x[k] = righthalf[j]
                j = j + 1
                k = k + 1

                mergeSort(novo_x)


        print(novo_x)
        page += 1

    except HTTPError:
        print(f"Paginas sem resposta: {PaginasSemResposta}")
        PaginasSemResposta = +1

    except ValueError:
        print("O valor null não pode ser convertido em float")

    if (len(novo_x) <= 1):
        print("")
        print("")
        print("")
        print("A lista foi totalmente consumida.")
        print(f" O numero de paginas não ordenadas foi de: {PaginasSemResposta}")
        page = -1
