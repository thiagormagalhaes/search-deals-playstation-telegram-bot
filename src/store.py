import requests


def storeApiUrl():
    return "https://store.playstation.com/store/api/chihiro/00_09_000/container/BR/pt/999/"


def allDeals():
    return "STORE-MSF77008-ALLDEALS"


game_contentType = ["all", "expansao", "avatar", "conjunto", "jogo"]
#game_contentType = ["all", "Expansão", "Avatar", "Conjunto", "Jogo completo"]


def totalGames():
    return str(url()["total_results"])


def url(size="30", store=allDeals(), contentType=game_contentType[0]):
    if (contentType == "all"):
        return requests.get(url=storeApiUrl()+store+"?size="+size).json()
    else:
        return requests.get(url=storeApiUrl()+store+"?size="+size+"&game_content_type="+contentType).json()


def deals(code=True):
    deals = list()
    r = url()
    if (code):
        for product in r["links"]:
            deals.append(product["name"] + " - " + product["id"])
    else:
        for product in r["links"]:
            deals.append(product["name"])
    return deals


def info(code):
    return requests.get(url=storeApiUrl()+code).json()
