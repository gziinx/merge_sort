def merge_sort(lista):
    if len(lista) > 1:
        esquerda = lista[:len(lista)//2]
        direita = lista[len(lista)//2:]

        merge_sort(esquerda)
        merge_sort(direita)

        index_esquerda = 0
        index_direita = 0
        index_merge = 0

        while index_esquerda < len(esquerda) and index_direita < len(direita):
            if esquerda[index_esquerda] <direita[index_direita]:
                lista[index_merge] = esquerda[index_esquerda]
                index_esquerda+=1
            else:
                lista[index_merge] = direita[index_direita]
                index_direita+=1
            index_merge+=1

        while index_esquerda < len(esquerda):
            lista[index_merge] = esquerda[index_esquerda]
            index_esquerda += 1
            index_merge += 1

        while index_direita < len(direita):
            lista[index_merge] = direita[index_direita]
            index_direita += 1
            index_merge += 1

listateste = [11,3423,4,5,5,4,5,7,68,1,999,23,43,565]
merge_sort(listateste)
print(listateste)