import datetime
import logging
import dotenv

from telegram.ext import Updater, CommandHandler
from config.settings import TOKEN
from src.store import Store


# Habilitar o logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

LOGGER = logging.getLogger(__name__)


STORE = Store()


def now_str():
    _now = datetime.datetime.now()
    return _now.strftime("[%H:%M:%S]")


def debug_log(msg):
    """ Printa uma mensagem de debug no console informando o tempo """
    print(now_str(), " - ", msg)


def start(bot, update):
    """ Mensagem inicial do comando / start """
    update.message.reply_text("""
    Bem-vindo ao meu primeiro bot!

    Digite / help para ver uma lista de comandos uteis.
    """)


def about(bot, update):
    update.message.reply_text(STORE.about())


def listDeals(bot, update, args):
    """ Handler consulta lista de produtos /list """
    products = STORE.deals()
    response = STORE.list_header(args)
    update.message.reply_text(text=response, parse_mode="markdown")

    response = ""
    for product in products:
        response += product + "\n"
        response += "\n"

    update.message.reply_text(response)


def search(bot, update, args):
    if (len(args) == 0):
        update.message.reply_text(
            "É necessário informar uma palavra para realizar a busca.")
        return

    response = STORE.url(STORE.totalGames())
    update.message.reply_text(
        "Aguarde... buscando em " + str(len(response["links"])) + " produtos")

    _list = STORE.format_list(response, args[0])

    for item in _list:
        update.message.reply_text(text=item)

    if (len(_list) == 0):
        update.message.reply_text("Nenhum resultado para a palvra: " + args[0])
    else:
        update.message.reply_text(
            str(len(_list)) + " resultado(s) encontrados para a palavra: " + args[0])


def product(bot, update, args):

    try:
        response = STORE.product(args)
        update.message.reply_text(text=response, parse_mode="markdown")
        link = STORE.product_link(args[0])
        update.message.reply_text(text=link)
    except ValueError:
        update.message.reply_text(
            "Não foi encontrado produto com o código informado")


def echo(bot, update):
    """ Responder comandos invalidos """
    update.message.reply_text("Comando inválido - ver lista de comandos")


def error(bot, update, error):
    """ Log de Erros """
    LOGGER.warning('Update "%s" caused error "%s"', update, error)


def config_token():
    """ Se a(key=TOKEN) não existir ou estiver None no
        .env -> Criar token
    """
    if not TOKEN:
        token = input("Copie aqui o token dado pelo @botfather: ")

        if not dotenv.find_dotenv():
            file = open(".env", "w+")
            file.write("TOKEN=")
            file.close()

        dotenv.set_key('.env', 'TOKEN', token)
        return token

    return TOKEN


def main():
    """Iniciar o bot"""
    # Criar o EventHandler
    updater = Updater(config_token())

    # Obter o dispatcher para registrar os handlers
    dipatcher = updater.dispatcher

    # comandos habilitados
    dipatcher.add_handler(CommandHandler("start", start))
    dipatcher.add_handler(CommandHandler("about", about))
    dipatcher.add_handler(CommandHandler("list", listDeals, pass_args=True))
    dipatcher.add_handler(CommandHandler("search", search, pass_args=True))
    dipatcher.add_handler(CommandHandler("product", product, pass_args=True))

    # log de erros
    dipatcher.add_error_handler(error)

    # Informar inicialização do bot no console
    debug_log("Bot inicializado com sucesso!")
    # Iniciar o Bot
    updater.start_polling()

    updater.idle()