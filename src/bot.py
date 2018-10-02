from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import datetime
import logging
import store
import json
import os

# Habilitar o logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(bot, update):
    """Mensagem inicial do comando /start"""
    update.message.reply_text('Bem vindo ao meu primeiro bot')

def help(bot, update):
    update.message.reply_text("""
    Bot para ver preços da PlayStation Store - em construção!

    /list - Retorna informações da promoção e os primeiros 30 produtos em promoção com o Titulo e o ID.

    /search palavra - Retorna os produtos em promoção que tenham a palavra passada.

    /product ID - Retorna as informações do produto pelo ID passado.
    """)

def list(bot, update, args):
    r = store.deals()

    response = "*DETALHES*\n\n"
    response += "*Catálogo:* " + store.allDeals() + "\n"
    response += "*Descrição:* " + store.url()["name"] + "\n\n"

    if (len(args) > 0):
      response += "Exibindo " + args[0] + " de " + str(store.totalGames()) + "\n"
    else:
      response += "Exibindo 30 de " + str(store.totalGames()) + "\n\n"

    update.message.reply_text(text=response, parse_mode="markdown")

    for product in r:
      update.message.reply_text(product)

def search(bot, update, args):
    if (len(args) == 0):
      update.message.reply_text("É necessário informar uma palavra para realizar a busca.")
      return

    count = 0
    r = store.url(store.totalGames())
    update.message.reply_text("Aguarde... buscando em " + str(len(r["links"])) + " produtos")
    for product in r["links"]:
      if (product["name"].lower().find(str(args[0]).lower()) >= 0):
        count += 1
        response = product["name"] + "\n"

        if "game_contentType" in product:
          response += "Categoria: " + product["game_contentType"] + "\n"

        response += "Preço: " + product["default_sku"]["display_price"] + "\n"
        response += "Promoção: " + product["default_sku"]["rewards"][0]["display_price"] + " (" + str(product["default_sku"]["rewards"][0]["discount"]) + "% de desconto)\n"

        if "bonus_display_price" in product["default_sku"]["rewards"][0]:
          response += "Plus: " + product["default_sku"]["rewards"][0]["bonus_display_price"] + " (" + str(product["default_sku"]["rewards"][0]["bonus_discount"]) + "% de desconto)\n"

        response += "Preço promocional até " + product["default_sku"]["rewards"][0]["end_date"] + "\n"

        response += "https://store.playstation.com/pt-br/product/" + product["id"]
        update.message.reply_text(text=response)

    if (count == 0):
      update.message.reply_text("Nenhum resultado para a palvra: " + args[0])
    else:
      update.message.reply_text(str(count) + " resultado(s) encontrados para a palavra: " + args[0])

def product(bot, update, args):
    product = store.info(args[0])

    if "codeName" in product:
      update.message.reply_text("Não foi encontrado produto com o código informado")
      return

    response = "*Categoria:* " + product["game_contentType"] + "\n"
    response += "*Produto:* " + product["name"] + "\n"
    response += "*Preço:* " + product["default_sku"]["display_price"] + "\n"
    response += "*Promoção:* " + product["default_sku"]["rewards"][0]["display_price"] + " (" + str(product["default_sku"]["rewards"][0]["discount"]) + "% de desconto)\n"

    if "bonus_display_price" in product["default_sku"]["rewards"][0]:
      response += "*Plus:* " + product["default_sku"]["rewards"][0]["bonus_display_price"] + " (" + str(product["default_sku"]["rewards"][0]["bonus_discount"]) + "% de desconto)\n"

    response += "*Preço promocional até " + product["default_sku"]["rewards"][0]["end_date"] + "*"
    print(response)
    update.message.reply_text(text=response, parse_mode="markdown")
    response = "https://store.playstation.com/pt-br/product/" + product["id"]
    update.message.reply_text(text=response)

def echo(bot, update):
    """Responder comandos invalidos"""
    update.message.reply_text("Comando inválido - ver lista de comandos")


def error(bot, update, error):
    """Log de Erros"""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    """Iniciar o bot"""
    # Criar o EventHandler
    config = json.loads(open(os.getcwd()[0:int(len(os.getcwd())-4)]+"/config/token.json").read())
    updater = Updater(config["token"])

    # Obter o dispatcher para registrar os handlers
    dp = updater.dispatcher

    # comandos habilitados
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("list", list, pass_args=True))
    dp.add_handler(CommandHandler("search", search, pass_args=True))
    dp.add_handler(CommandHandler("product", product, pass_args=True))

    # p/ comandos não reconhecidos
    #dp.add_handler(MessageHandler(Filters.text, echo))

    # log de erros
    dp.add_error_handler(error)

    # Iniciar o Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
