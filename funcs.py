def obterLista():
    msg = ''''''
    with open(r'dados//sites.txt', 'r') as file:
        sites = file.readlines()

    c = 1
    for site in sites:

        msg += f'[{c}] - {site}'

        c += 1
        
    return msg


def excluir_site(it):
    lista = []
    it = int(it)
    with open(r'dados//sites.txt', 'r') as file:
        sites = file.readlines()
    c = 1

    for site in sites:
        lista.append([c, site])
        c += 1

    for i in lista:
        if i[0] == it:
            lista.remove(i)
            msg = f'[!] Site {i[1]} excluído com sucesso!'

    with open(r'dados//sites.txt', 'w') as file:
        for i in lista:
            file.write(i[1])
    return msg


def adicionar_site(site):
    # Adicionando um site a lista (sites.txt)

    # Obtendo o ID
    with open(r'dados//sites.txt', 'r') as file:
        arq = file.read()
        sites = arq.split('|')
        sites.pop()
        ID = len(sites) + 1
        file.close()

    # Adicionando um site a lista (sites.txt)
    with open(r'dados//sites.txt', 'a') as file:
        file.write(f'127.0.0.{ID} {site}\n')

        return f'[!] Site {site} adicionado com sucesso!'
