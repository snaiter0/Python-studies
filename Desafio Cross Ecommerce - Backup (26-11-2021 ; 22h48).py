import urllib.request
from time import sleep
from urllib.error import HTTPError

page = 1
PaginasSemResposta = 0

while (page != -1):
    try:
        webUrl = urllib.request.urlopen(f'http://challenge.dienekes.com.br/api/numbers?page={page}')
        data = webUrl.read()
        dado = bytes.decode(data)
        semColchete = dado.replace("[", " ")
        semColchete = semColchete.replace("]", " ")
        semColchete = semColchete.replace('"', " ")
        semColchete = semColchete.replace("numbers :", "Numeros: ")
        espacoAposVirgula = semColchete.split(",")
        print(f'Numero da pagina em execução:{page-1}')


        def mergeSort(espacoAposVirgula):

            if len(espacoAposVirgula) > 1:
                mid = len(espacoAposVirgula) // 2
                lefthalf = espacoAposVirgula[:mid]
                righthalf = espacoAposVirgula[mid:]

                mergeSort(lefthalf)
                mergeSort(righthalf)

                i = 0
                j = 0
                k = 0
            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] < righthalf[j]:
                    espacoAposVirgula[k] = lefthalf[i]
                    i = i + 1
                else:
                    espacoAposVirgula[k] = righthalf[j]
                    j = j + 1
                    k = k + 1

            while i < len(lefthalf):
                espacoAposVirgula[k] = lefthalf[i]
                i = i + 1
                k = k + 1

            while j < len(righthalf):
                espacoAposVirgula[k] = righthalf[j]
                j = j + 1
                k = k + 1


            mergeSort(espacoAposVirgula)
        print(espacoAposVirgula)
        page += 1

    except HTTPError:
        print(f"Paginas sem resposta: {PaginasSemResposta}")
        PaginasSemResposta = +1

    if (len(espacoAposVirgula) <= 1):
        print("")
        print("")
        print("")
        print("A lista foi totalmente consumida.")
        print(f" O numero de paginas não ordenadas foi de: {PaginasSemResposta}")
        page = -1
