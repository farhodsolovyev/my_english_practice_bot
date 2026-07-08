#!/usr/bin/env bash
# Двойной клик в Finder — запускает бота.
cd "$(dirname "$0")" || exit 1
./run.sh start
echo
echo "Это окно можно закрыть."
