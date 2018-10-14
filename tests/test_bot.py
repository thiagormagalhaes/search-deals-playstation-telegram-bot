from unittest import TestCase
from unittest.mock import patch
from src import bot
import app


class TestBot(TestCase):

    print = print

    @patch("src.bot.TOKEN", new=None)
    @patch("src.bot.dotenv.set_key")
    def test_config_token_without_key_value(self, _set_key):

        def _set_key(env, key, value):
            pass

        _set_key.side_effect = _set_key

        input_values = [
            "Copie aqui o token dado pelo @botfather: "
        ]
        output = []

        def mock_input(s):
            output.append(s)
            return input_values.pop(0)

        app.bot.input = mock_input

        bot.config_token()

        self.assertEqual(
            output, ["Copie aqui o token dado pelo @botfather: "])

    @patch("src.bot.TOKEN", new="KEYDEFINED")
    def test_config_token_key_value(self):

        input_values = [
            "Copie aqui o token dado pelo @botfather: "
        ]
        output = []

        def mock_input(s):
            output.append(s)
            return input_values.pop(0)

        app.bot.input = mock_input

        bot.config_token()

        self.assertEqual(output, [])

    @patch("src.bot.TOKEN", new=None)
    @patch("src.bot.dotenv.find_dotenv")
    @patch("src.bot.dotenv.set_key")
    def test_no_env_file(self, _find_dotenv, _set_key):

        def _set_key(env, key, value):
            pass

        _set_key.side_effect = _set_key

        _find_dotenv.return_value = ''

        input_values = [
            "Copie aqui o token dado pelo @botfather: "
        ]
        output = []

        def mock_input(s):
            output.append(s)
            return input_values.pop(0)

        app.bot.input = mock_input

        bot.config_token()

        self.assertEqual(
            output, ["Copie aqui o token dado pelo @botfather: "])

    @patch("src.bot.now_str")
    def test_main(self, _now):

        expected = '[22:00:00]'

        _now.return_value = expected

        self.assertEqual(bot.now_str(), expected)
