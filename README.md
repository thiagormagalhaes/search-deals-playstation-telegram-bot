## Search Deals Playstation *telegram bot*
*Bot* do Telegram para a *Playstation Store* em português (PlaystationStore)

#### Funcionalidades básicas
* Consulta promoções por `titulo do game`.

#### Implementações futuras
* Aceito sugestões :).

#### Instalação e configuração
1. Instalação das dependências:
`pip install -r requirements.txt`

2. Configuração do *token* de acesso ao *bot*:
	* Criar o diretório `config/`, com o arquivo `token.json`, no formato:

	    `{"token": "seu_token_aqui"}`

         obs: o *token* é gerado quando o *bot* é criado no [*@botfather*](https://telegram.me/BotFather)
3.  Executar o arquivo `src/bot.py`:

     `python3 bot.py`

     Para deixar executando em *background* e independente da sessão do *tty*:

     `nohup python3 bot.py &`
