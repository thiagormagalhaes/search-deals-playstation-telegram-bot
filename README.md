## Search Deals Playstation - *Telegram Bot*

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/99dd3531239e4be980fc271c23429312)](https://app.codacy.com/app/thiagormagalhaes/search-deals-playstation-telegram-bot?utm_source=github.com&utm_medium=referral&utm_content=thiagormagalhaes/search-deals-playstation-telegram-bot&utm_campaign=Badge_Grade_Dashboard)
[![Build Status](https://travis-ci.org/thiagormagalhaes/search-deals-playstation-telegram-bot.svg?branch=master)](https://travis-ci.org/thiagormagalhaes/search-deals-playstation-telegram-bot)
[![Maintainability](https://api.codeclimate.com/v1/badges/a3850ce887c38eaac7da/maintainability)](https://codeclimate.com/github/thiagormagalhaes/search-deals-playstation-telegram-bot/maintainability)

*Bot* do Telegram para a *Playstation Store* em português (PlaystationStore)

## Funcionalidades básicas
*   Consulta promoções por *titulo do game*.

## Implementações futuras
*   Aceito sugestões :)

## Instalação e configuração
1.  Instalação das dependências:
`pip install -r requirements.txt`


2.  Configuração do *token* de acesso ao *bot*:
*   Criar o diretório `config/`, com o arquivo `token.json`, no formato:

      `{"token": "seu_token_aqui"}`

      **OBS**: O *token* é gerado quando o *bot* é criado no [*@botfather*](https://telegram.me/BotFather)
      
3.  Executar o arquivo `src/bot.py`:

     `python3 bot.py`

     Para deixar executando em *background* e independente da sessão do *tty*:

     `nohup python3 bot.py &`
     
### Instalação usando Docker
1. Fazer a construção da imagem:
`docker build -t search-psn:v1 .`

2. Executar:
`docker run -d --name search-psn search-psn`