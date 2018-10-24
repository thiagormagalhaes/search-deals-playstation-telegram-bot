import requests
import jinja2

from config.settings import STORE_ALL_DEALS, STORE_API_URL, STORE_URL_PRODUCT

game_contentType = ["all", "expansao", "avatar", "conjunto", "jogo"]
templateLoader = jinja2.FileSystemLoader(searchpath="./src/")

templateEnv = jinja2.Environment(
    loader=templateLoader,
    autoescape=jinja2.select_autoescape(
        disabled_extensions=('txt',),
        default_for_string=True,
        default=True,
    ))

TEMPLATE_FILE = "template.txt"
label = templateEnv.get_template(TEMPLATE_FILE)


class Store():

    def total_games(self):
        return str(self.url()["total_results"])

    @classmethod
    def url(self, size="30", store=STORE_ALL_DEALS, kind=game_contentType[0]):
        if (kind == "all"):
            return requests.get(url=STORE_API_URL+store+"?size="+size).json()
        else:
            return requests.get(url=STORE_API_URL+store+"?size="+size+"&game_content_type="+kind).json()

    def deals(self, code=True):
        deals = list()
        r = self.url()

        label = jinja2.Template(
            '{{ name }}{% if code %} - {{ id }}{% endif %}')

        for product in r["links"]:
            deals.append(label.render(product, code=code))

        return deals

    @classmethod
    def info(self, _id):
        return requests.get(url=STORE_API_URL+_id).json()

    @classmethod
    def product_link(self, _id):
        return STORE_URL_PRODUCT + _id

    def product(self, args, error=""):
        product = self.info(args[0])

        dct = self.parser_product_to_dict(product)
        return label.render(dct)

    @classmethod
    def about(self):
        return """
        Bot para ver preços da PlayStation Store - em construção!

        /list - Retorna informações da promoção e os primeiros 30 produtos em promoção com o Titulo e o ID.

        /search palavra - Retorna os produtos em promoção que tenham a palavra passada.

        /product ID - Retorna as informações do produto pelo ID passado.
        """

    def list_header(self, args):

        response = "*DETALHES*\n\n"
        response += "*Catálogo:* " + STORE_ALL_DEALS + "\n"
        response += "*Descrição:* " + self.url()["name"] + "\n\n"

        if (len(args) > 0):
            response += "Exibindo " + args[0] + \
                " de " + str(self.total_games()) + "\n"
        else:
            response += "Exibindo 30 de " + str(self.total_games()) + "\n\n"

        return response

    @classmethod
    def parser_product_to_dict(self, product):

        d = dict()
        d["name"] = product["name"]
        d["link"] = self.product_link(product["id"])

        if "game_contentType" in product:
            d["category"] = product["game_contentType"]

        if product["default_sku"]["rewards"]:
            rewards = product["default_sku"]["rewards"][0]

            d["price"] = product["default_sku"]["display_price"]

            d["price_rewards"] = rewards["display_price"]
            d["discount"] = str(product["default_sku"]
                                ["rewards"][0]["discount"]) + "%"

            if "bonus_display_price" in rewards:
                d["bonus_price"] = rewards["bonus_display_price"]
                d["bonus_discount"] = str(
                    rewards["bonus_discount"]) + "%"

            d["end_date"] = rewards["end_date"]

        else:
            d["without_rewards"] = "Nenhum preço promocional encontrado! \n"

        return d

    def format_list(self, body, text_search):

        _list = []

        for product in body["links"]:

            if (product["name"].lower().find(str(text_search).lower()) >= 0):

                dct = self.parser_product_to_dict(product)
                _list.append(label.render(dct))

        return _list
