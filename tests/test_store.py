from unittest import TestCase
from unittest.mock import Mock, patch
from src.store import Store

class TestStore(TestCase):

    def setUp(self):
        self.store = Store()

    @patch("src.store.Store.url")
    def test_total_games(self, _url):
        total_games = 12345
        _url.return_value = {"total_results": total_games}

        resp = self.store.totalGames()

        self.assertEqual(resp, str(total_games))

    @patch("src.store.STORE_API_URL", new="http://urlplaystore.com/")
    @patch("src.store.requests.get")
    def test_url_type_all(self, _get):
        to_json = Mock()
        api_response = {"playstation": "api return"}
        to_json.json.return_value = api_response
        _get.return_value = to_json
        arg_type = "all"

        resp = self.store.url(store="STOREALLDEALS", kind=arg_type)

        self.assertEqual(resp, api_response)
        _get.assert_called_once_with(
            url="http://urlplaystore.com/STOREALLDEALS?size=30")

    @patch("src.store.STORE_API_URL", new="http://urlplaystore.com/")
    @patch("src.store.requests.get")
    def test_url_type_jogos(self, _get):
        to_json = Mock()
        api_response = {"playstation": "api return"}
        to_json.json.return_value = api_response
        _get.return_value = to_json
        arg_type = "jogos"

        resp = self.store.url(store="STOREALLDEALS", kind=arg_type)

        self.assertEqual(resp, api_response)
        _get.assert_called_once_with(
            url="http://urlplaystore.com/STOREALLDEALS?size=30&game_content_type=jogos")

    @patch("src.store.STORE_API_URL", new="http://urlplaystore.com/")
    @patch("src.store.requests.get")
    def test_info(self, _get):
        to_json = Mock()
        api_response = {"playstation": "api return"}
        to_json.json.return_value = api_response
        _get.return_value = to_json

        _id = "TESTEID"
        resp = self.store.info(_id)

        self.assertEqual(resp, api_response)
        _get.assert_called_once_with(url="http://urlplaystore.com/" + _id)

    def test_info_without_id(self):
        with self.assertRaises(TypeError):
            self.store.info(None)

    @patch("src.store.Store.url")
    def test_deals_true(self, _url):
        mock_list = Mock()
        api_response = list()
        api_response.append("PRODUTOA - PD1")
        api_response.append("PRODUTOB - PD2")
        mock_list.json.return_value = api_response

        produtos = [{"name": "PRODUTOA", "id": "PD1"},
                    {"name": "PRODUTOB", "id": "PD2"}]

        _url.return_value = {"links": produtos}

        resp = self.store.deals()

        self.assertEqual(resp, api_response)

    @patch("src.store.Store.url")
    def test_deals_without_id(self, _url):
        mock_list = Mock()
        api_response = list()
        api_response.append("PRODUTOA")
        api_response.append("PRODUTOB")
        mock_list.json.return_value = api_response

        produtos = [{"name": "PRODUTOA", "id": "PD1"},
                    {"name": "PRODUTOB", "id": "PD2"}]

        _url.return_value = {"links": produtos}

        resp = self.store.deals(False)

        self.assertEqual(resp, api_response)