(python3 ./backend/main.py) &
echo "starting flask backend"


(cd ./frontend && trunk serve) &
echo "starting leptos frontend"

wait