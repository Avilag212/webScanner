import requests
import sys

def busca(target):
    try:
        header = {'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/118.0.5993.69 Mobile/15E148 Safari/604.1'}
        response = requests.get(target,headers=header)
        #response = requests.get(target)
        if(response.status_code == 404):
            pass
        else:
            print(f"[+]Encontrado: {target} |       CODE:{response.status_code}")
    except NameError as erro:
        print(erro)


if(__name__ == '__main__'):
    if(len(sys.argv)<2):
        print("Modo de uso: python main.py <url_base>")
    else:
        with open('wordlist.txt', 'r') as arquivo:
            for term in arquivo.readlines():
                busca(f'{sys.argv[1]}/{term.rstrip()}')
        
