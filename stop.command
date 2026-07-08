#!/usr/bin/env bash
# Двойной клик в Finder — останавливает бота.
cd "$(dirname "$0")" || exit 1
./run.sh stop
echo
echo "Это окно можно закрыть."
