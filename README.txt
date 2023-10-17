WebScanner em Python
By: www.linkedin.com/in/gabriel-de-avila-farias/

[AVISO]: O script trata-se de uma ferramenta destinada à pentests legítimos,
o criador não se responsabiliza por quaisquer finalidades para as quais esta ferramenta venha ser utilizada.

[WARNING]: The script is a tool intended for legitimate pentests,
the creator is not responsible for any purposes for which this tool may be used.


-- MODO DE USO --
python main.py http://www.exemplo.com

(1) Utilizar a url completa sem a barra no final (/), o script
se encarregará de coloca-la, a wordlist deve ser um arquivo de
extensão txt com o exato nome: "wordlist.txt" e deve estar no
mesmo diretório que o script, por padrão a wordlist que existe neste
repositório é idêntica a small list do dirb, pode ser alterada ou 
trocada facilmente.

[!] O script é focado no uso fácil e prático.
[!] User-Agent: As requisições http/https, possuem um campo
denominado User-Agent que informa ao servidor web qual aplicação
realiza a requisição, para que seja possível ultrapassar a maioria
das defesas que bloqueim requisições a partir deste campo, por padrão
a requisição é feita utilizando o seguinte User-Agent:
'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/118.0.5993.69 Mobile/15E148 Safari/604.1'
Isto pode ser alterado no código fonte (main.py).

-- HOW TO USE --
python main.py http://www.example.com

(1) Use the full url without the slash at the end (/), the script
will take care of placing it, the wordlist must be a
txt extension with the exact name: "wordlist.txt" and must be in the
same directory as the script, by default the wordlist that exists in this
repository is identical to the dirb small list, it can be changed or
changed easily.

[!] The script is focused on easy and practical use.
[!] User-Agent: http/https requests have a field
called User-Agent that informs the web server which application
makes the request, so that it is possible to overcome the majority
of defenses that block requests from this field, by default
the request is made using the following User-Agent:
'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/118.0.5993.69 Mobile/15E148 Safari/604.1'
This can be changed in the source code (main.py).


