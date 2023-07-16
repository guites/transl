#!/usr/bin/env python3

import argparse
import os
import sqlite3
import subprocess

DB_PATH = os.path.join(os.path.expanduser("~"), ".trans.sqlite3")


class SqliteHandler:
    def __init__(self):
        self.connection = sqlite3.connect(DB_PATH)
        self.cursor = self.connection.cursor()
        self.__create_tables()

    def __create_tables(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS logs(id INTEGER PRIMARY KEY, languages TEXT, text TEXT, options TEXT, created_at TEXT DEFAULT CURRENT_TIMESTAMP);"
        )

    def register_log(self, languages, text, options):
        self.cursor.execute(
            "INSERT INTO logs (languages, text, options) VALUES (?, ?, ?)",
            (languages, text, options),
        )
        self.connection.commit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "languages",
        help="`from:`, `:to` or `from:to`",
    )
    parser.add_argument("text", help="text of interest")
    parser.add_argument("-b", "-brief", help="Brief mode.", action="store_true")
    parser.add_argument(
        "-speak", help="Listen to the original text.", action="store_true"
    )
    parser.add_argument(
        "-p", "-play", help="Listen to the translation.", action="store_true"
    )
    args = parser.parse_args()
    languages = args.languages
    text = args.text

    options = ""
    subprocess_args = ["trans", languages, text]

    if args.b:
        options += "-b"
        subprocess_args.append("-b")
    if args.speak:
        options += " -speak"
        subprocess_args.append("-speak")
    if args.p:
        options += "-play"
        subprocess_args.append("-play")

    completed = subprocess.run(subprocess_args)
    sql_handler = SqliteHandler()
    sql_handler.register_log(languages, text, options)
