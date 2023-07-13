#!/bin/sh

set -e

# check if the BOT_TOKEN is set
if [ -z "$BOT_TOKEN" ]; then
    echo "BOT_TOKEN environment variable is missing"
    exit 1
fi

# create config.json file with the BOT_TOKEN in /app
echo "{\"token\":\"${BOT_TOKEN}\"}" > /app/config.json

# run the bot
cd /app
python3 index.py "$@"
