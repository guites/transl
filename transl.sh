#!/usr/bin/bash

DB_PATH="$HOME/.transl.sqlite"

if [ ! -f "$DB_PATH" ]; then
    touch "$DB_PATH"
fi

CREATE_TABLE_STMT="CREATE TABLE IF NOT EXISTS logs(call TEXT NOT NULL CHECK(LENGTH(call) > 0), created_at TEXT DEFAULT CURRENT_TIMESTAMP);"

sqlite3 "$DB_PATH" "$CREATE_TABLE_STMT"

[ "$?" != 0 ] && echo "Error creating database. Exiting..." && exit 1

call="${@:1}"

trans "$@"

[ "$?" != 0 ] && echo "Error invoking trans. Exiting..." && exit 1

INSERT_STMT="INSERT INTO logs (call) VALUES (\"$call\")"

sqlite3 "$DB_PATH" "$INSERT_STMT"

[ "$?" != 0 ] && echo "Error saving trans call to database." && exit 1
