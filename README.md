# Transl

This project is a simple wrapper for the magnificent [translate shell](https://github.com/soimort/translate-shell), that **registers all your calls to trans in a simple sqlite3 database**.

## Motivation

Back when I was starting with french and deutsch, I used to keep a notebook of new words and meaning of phrases. It's cool to go back and see what used to puzzle you, or how your vocabulary has grown over time.

When I started using `trans`, I became too lazy to keep logging my notes, so why not automate it?

## Installation

1. Make sure you have `trans` installed and available in your $PATH. (see <https://github.com/soimort/translate-shell#installation>)
2. Clone this repository: `git clone ...`
3. Create an alias for `transl` with `echo "alias transl=$(pwd)/transl.py" >> ~/.bash_aliases`, .zshrc or equivalent.
4. Try it out with `transl -h`

We currently accept the `-b`, `-p` and `-speak` flags from translate shell.

## Usage

Basic: "from:to" language parameters followed by the text.

    guites@macos transl % transl fr: "Quand je parle d'amour je parle de toi"
    Quand je parle d'amour je parle de toi

    When I talk about love I'm talking about you

    Translations of Quand je parle d'amour je parle de toi
    [ Français -> English ]

    Quand je parle d'amour je parle de toi
        , When I speak of love I speak of you

You can also specify only the `from:` language, and translate shell will translate into english, or specify only the `:to` language and translate shell will try to guess the idiom.

Brief mode: shorten your replies with `-b`

    guites@macos transl % transl en:de "a cow sits amidst the road" -b
    Eine Kuh sitzt mitten auf der Straße

Play: use the `-p` flag to speak the translate sentence out loud.

    guites@macos transl % transl pt:en "Dadinho é o caralho, meu nome é zé pequeno, porra\!" -p -b
    Dadinho is the fuck, my name is Zé Pequeno, dammit!

Speak: use the `-speak` flag to speak the original sentence out loud.

    guites@macos transl % transl fr: "O Satan, prends pitié de ma longue misère\!" -speak
    O Satan, prends pitié de ma longue misère!

    O Satan, take pity on my long misery!

    Translations of O Satan, prends pitié de ma longue misère!
    [ Français -> English ]

    O Satan, prends pitié de ma longue misère!
        , O Satan, have mercy on my long misery!

Every call will be logged to a `.trans.sqlite3` database file in your home directory. You can access it with

    sqlite3 ~/.trans.sqlite3

    Enter ".help" for usage hints.
    sqlite> .tables
    logs
    sqlite> .schema logs
    CREATE TABLE logs(id INTEGER PRIMARY KEY, languages TEXT, text TEXT, created_at TEXT DEFAULT CURRENT_TIMESTAMP, options TEXT);
    sqlite> SELECT * FROM logs;
    1|fr:|Quand je parle d'amour je parle de toi|2023-07-15 01:00:54|
    2|fr:|est-ce que cette merde est tellement bonne?|2023-07-15 01:02:53|
    3|fr:|O Satan, prends pitié de ma longue misère!|2023-07-16 16:39:15| -speak

## Contributions

PRs appreciated! I'm thinking on whats the best way to show some usage statistics on the terminal.
