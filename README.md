# Search Deals Playstation - _Telegram Bot_

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/99dd3531239e4be980fc271c23429312)](https://app.codacy.com/app/thiagormagalhaes/search-deals-playstation-telegram-bot?utm_source=github.com&utm_medium=referral&utm_content=thiagormagalhaes/search-deals-playstation-telegram-bot&utm_campaign=Badge_Grade_Dashboard)
[![Build Status](https://travis-ci.org/thiagormagalhaes/search-deals-playstation-telegram-bot.svg?branch=master)](https://travis-ci.org/thiagormagalhaes/search-deals-playstation-telegram-bot)
[![Maintainability](https://api.codeclimate.com/v1/badges/a3850ce887c38eaac7da/maintainability)](https://codeclimate.com/github/thiagormagalhaes/search-deals-playstation-telegram-bot/maintainability)

_Bot_ do Telegram para a _Playstation Store_ em português (PlaystationStore)

## Funcionalidades básicas

      - Consulta promoções por _titulo do game_.

## Implementações futuras

      - Aceito sugestões :)

## Instalação e configuração

      1. Instalação das dependências:

            `pip install -r requirements.txt`

      2. Configuração do _token_ de acesso ao _bot_:

            - Criar o diretório `config/`, com o arquivo `token.json`, no formato:

            `{"token": "seu_token_aqui"}`

      **OBS**: O _token_ é gerado quando o _bot_ é criado no [_@botfather_](https://telegram.me/BotFather)

      3. Executar o arquivo `src/bot.py`:

            `python3 bot.py`

      Para deixar executando em _background_ e independente da sessão do _tty_:

            `nohup python3 bot.py &`

### Instalação usando Docker

      1. Fazer a construção da imagem:
            `docker build -t search-psn:v1 .`
      2. Executar:
            `docker run -d --name search-psn search-psn`
