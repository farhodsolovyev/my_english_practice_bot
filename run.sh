#!/usr/bin/env bash
# Управление English Bot: запуск / остановка / статус / логи.
# Использование: ./run.sh {start|stop|restart|status|logs|install}

cd "$(dirname "$0")" || exit 1

VENV="venv"
PYBIN="$VENV/bin/python"
PIDFILE="bot.pid"
LOGFILE="bot.log"

color()  { printf "\033[%sm%s\033[0m\n" "$1" "$2"; }
ok()     { color "32" "$1"; }
warn()   { color "33" "$1"; }
err()    { color "31" "$1"; }

venv_ok() {
    # venv считается рабочим, только если его интерпретатор реально запускается
    [ -f "$PYBIN" ] && "$PYBIN" -c "import sys" >/dev/null 2>&1
}

ensure_venv() {
    if ! venv_ok; then
        if [ -d "$VENV" ]; then
            warn "venv повреждён — пересоздаю..."
            rm -rf "$VENV"
        else
            warn "venv не найден — создаю ($(python3 --version 2>&1))..."
        fi
        python3 -m venv "$VENV" || { err "Не удалось создать venv"; exit 1; }
    fi
    "$PYBIN" -m pip install -q --upgrade pip >/dev/null 2>&1
    if ! "$PYBIN" -m pip install -q -r requirements.txt; then
        warn "pip: не удалось доустановить зависимости (возможно, нет сети)."
        warn "Если бот не стартует — установи вручную: $PYBIN -m pip install -r requirements.txt"
    fi
}

is_running() {
    [ -f "$PIDFILE" ] && kill -0 "$(cat "$PIDFILE")" 2>/dev/null
}

# Убивает все инстансы этого бота (включая осиротевшие без pidfile).
# Иначе два процесса с одним токеном дают TelegramConflictError.
kill_all_instances() {
    [ -f "$PIDFILE" ] && kill "$(cat "$PIDFILE")" 2>/dev/null
    rm -f "$PIDFILE"
    local pids
    pids=$(pgrep -fi "python bot\.py" 2>/dev/null)
    [ -n "$pids" ] && kill $pids 2>/dev/null
    sleep 1
}

start() {
    if is_running; then
        ok "Бот уже запущен (PID $(cat "$PIDFILE"))"
        exit 0
    fi
    if [ ! -f ".env" ]; then
        err "Нет .env. Скопируй .env.example в .env и впиши токен от @BotFather."
        exit 1
    fi
    kill_all_instances   # подчистить возможные осиротевшие инстансы
    ensure_venv
    echo "Запускаю бота..."
    nohup "$PYBIN" bot.py >> "$LOGFILE" 2>&1 &
    echo $! > "$PIDFILE"
    sleep 2
    if is_running; then
        ok "✅ Запущен (PID $(cat "$PIDFILE")). Логи: ./run.sh logs"
    else
        err "❌ Не удалось запустить. Последние строки лога:"
        tail -n 25 "$LOGFILE"
        rm -f "$PIDFILE"
        exit 1
    fi
}

stop() {
    if is_running || pgrep -fi "python bot\.py" >/dev/null 2>&1; then
        kill_all_instances
        ok "🛑 Бот остановлен"
    else
        warn "Бот не запущен"
        rm -f "$PIDFILE"
    fi
}

case "${1:-}" in
    start)   start ;;
    stop)    stop ;;
    restart) stop; sleep 1; start ;;
    status)
        if is_running; then ok "✅ Работает (PID $(cat "$PIDFILE"))"; else warn "⛔️ Остановлен"; fi
        ;;
    logs)    touch "$LOGFILE"; tail -n 50 -f "$LOGFILE" ;;
    install) ensure_venv; ok "Готово" ;;
    *)
        echo "Использование: ./run.sh {start|stop|restart|status|logs|install}"
        ;;
esac
