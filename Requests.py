# Importo o Requests
import requests

# Inicio a sessão para o tratamento (cookie JSESSIONID).
sessao = requests.Session()

# URL de busca.
url = "http://pesquisa.in.gov.br/imprensa/core/consulta.action"

# Variáveis do formulário e respectivos parâmetros de busca.
payload = {
    "edicao.txtPesquisa" : "brasil", # Palavra buscada em questão.
    "edicao.consultaAntiga" : "1,1000,1010,1020,2,2000,3,3000,3020,", # Opcional. Mantive igual à busca padrão.
    "edicao.fonetica": "null,", # Busca a palavra exata (grafia).
    "edicao.dtInicio" : "01/08", # Data início
    "edicao.dtFim" : "15/08", # Data fim
    "edicao.ano" : "2017" # Ano selecionado no menu drop-down.
}

# Passo a URL + parâmetros por sessão.
r = sessao.post(url, payload)

# UTF-8.
r.encoding

print(r.text)
# print(r.cookies)
# print(r.headers)

# Salva a página HTML.
htmlArquivo = r.text
arquivo = open("portalimprensa.html", "w", encoding="utf-8")  
arquivo.write(str(htmlArquivo))
arquivo.close()
