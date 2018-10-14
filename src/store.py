import requests
from config.settings import STORE_ALL_DEALS, STORE_API_URL, STORE_URL_PRODUCT

game_contentType = ["all", "expansao", "avatar", "conjunto", "jogo"]


class Store():

    def totalGames(self):
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
        if (code):
            for product in r["links"]:
                deals.append(product["name"] + " - " + product["id"])
        else:
            for product in r["links"]:
                deals.append(product["name"])
        return deals

    @classmethod
    def info(self, _id):
        return requests.get(url=STORE_API_URL+_id).json()

    @classmethod
    def product_link(self, _id):
        return STORE_URL_PRODUCT + _id

    def product(self, args, error=""):
        product = self.info(args[0])

        response = "*Categoria:* " + product["game_contentType"] + "\n"
        response += "*Produto:* " + product["name"] + "\n"
        response += "*Preço:* " + \
            product["default_sku"]["display_price"] + "\n"
        response += "*Promoção:* " + product["default_sku"]["rewards"][0]["display_price"] + \
            " (" + str(product["default_sku"]["rewards"]
                       [0]["discount"]) + "% de desconto)\n"

        if "bonus_display_price" in product["default_sku"]["rewards"][0]:
            response += "*Plus:* " + product["default_sku"]["rewards"][0]["bonus_display_price"] + \
                " (" + str(product["default_sku"]["rewards"]
                           [0]["bonus_discount"]) + "% de desconto)\n"

        response += "*Preço promocional até " + \
            product["default_sku"]["rewards"][0]["end_date"] + "*"

        return response

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
                " de " + str(self.totalGames()) + "\n"
        else:
            response += "Exibindo 30 de " + str(self.totalGames()) + "\n\n"

        return response

    @classmethod
    def format_response(self, product, response, format_character=''):
        # check if product is on sale / has discount
        if product["default_sku"]["rewards"]:
            response += format_character + "Preço:" + format_character + " " + \
                product["default_sku"]["display_price"] + "\n"
            response += format_character + "Promoção:" + format_character + " " + \
                product["default_sku"]["rewards"][0]["display_price"] + " (" + \
                str(product["default_sku"]["rewards"][0]
                    ["discount"]) + "% de desconto)\n"

            if "bonus_display_price" in product["default_sku"]["rewards"][0]:
                response += format_character + "Plus:" + format_character + " " + \
                    product["default_sku"]["rewards"][0]["bonus_display_price"] + " (" + str(
                        product["default_sku"]["rewards"][0]["bonus_discount"]) + "% de desconto)\n"

            response += format_character + "Preço promocional até " + \
                product["default_sku"]["rewards"][0]["end_date"] + \
                format_character + "\n"
        else:
            response += format_character + "Promoção:" + \
                format_character + " Nenhum preço promocional encontrado! \n"

        return response

    def format_list(self, body, text_search):

        _list = []
        for product in body["links"]:
            if (product["name"].lower().find(str(text_search).lower()) >= 0):

                response = product["name"] + "\n"

                if "game_contentType" in product:
                    response += "Categoria: " + \
                        product["game_contentType"] + "\n"

                response = self.format_response(product, response)

                response += self.product_link(product["id"])

                _list.append(response)

        return _list
