"""
BOT Configurations
"""
import os
from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TOKEN = config(
    'TOKEN', default=None)

STORE_API_URL = config(
    'STORE_API_URL', default="https://store.playstation.com/store/api/chihiro/00_09_000/container/BR/pt/999/")

STORE_ALL_DEALS = config(
    'STORE_ALL_DEALS', default="STORE-MSF77008-ALLDEALS")

STORE_URL_PRODUCT = config(
    'STORE_URL_PRODUCT', "https://store.playstation.com/pt-br/product/")
