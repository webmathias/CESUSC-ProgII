def teste():
    pass
def sort(_list):
    list = _list[:]
    for j in range(len(list)-1):
        for i in range(len(list)-1-j):
            if list[i] < list[i+1]:
                aux = list[i]
                list[i] = list[i+1]
                list[i+1] = aux
    return list

candidatos = int(input('Numero de candidatos'))
vagas = int(input('Vagas'))
pontos = []
for i in range(candidatos):
    pontos.append(int(input()))
pontos = sort(pontos)
classificados = vagas
pontuacaoMaisAlta = pontos[vagas-1]
for i in range(vagas, len(pontos)):
    if(pontuacaoMaisAlta == pontos[i]):
        classificados += 1
    else:
        break
print(classificados)

