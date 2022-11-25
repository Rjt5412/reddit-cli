import unittest
from typer.testing import CliRunner
import os
from reddit_cli.main import app


HOME_DIR = os.getenv("HOME")

runner = CliRunner()


class Tests(unittest.TestCase):
    def test_login(self):
        username = "abcd"
        password = "pass1234"
        result = runner.invoke(
            app, ["login", username], input=f"{password}\n{password}\n"
        )
        self.assertEqual(result.exit_code, 0)

    def test_profile_prefs(self):
        result = runner.invoke(app, ["profile-prefs"])
        self.assertEqual(result.exit_code, 0)

    def test_subreddit_subscribed(self):
        result = runner.invoke(app, ["subreddit-subscribed"])
        self.assertEqual(result.exit_code, 0)

    def test_subreddit_new(self):
        result = runner.invoke(app, ["subreddit-new"])
        self.assertEqual(result.exit_code, 0)

    def test_subreddit_popular(self):
        result = runner.invoke(app, ["subreddit-popular"])
        self.assertEqual(result.exit_code, 0)

    def test_subreddit_search(self):
        search_query = "cricket"
        result = runner.invoke(app, ["subreddit-search", search_query])
        self.assertEqual(result.exit_code, 0)
