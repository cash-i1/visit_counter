(python3 ./backend/main.py) &
echo "starting flask backend"


(cargo run --manifest-path=./frontend/Cargo.toml) &
echo "starting leptos frontend"

wait