# website visit counter
this is a website that will add 1 to a number every time someone visits the site. it is made in **python** (flask, for the backend) and **rust** (leptos, for the frontend)

# how good is it 
this is not a good project. i dont know why i decided to make the backend in python but it is a bit crap and the rust code is also pretty bad and slodged together. the worst thing is the `run.sh` file i made to run the flask server and use trunk to run the leptos front end aswell. scuffed 🤮

# running
to run you should probably use the `run.sh` file. it requires `cargo`, rust wasm target (`wasm32-unknown-unknown`), `trunk`, `python3` and `flask`,

these can all be installed on **arch linux** using the command below (assuming `rustup` and `python3` are already installed)
```
rustup target add wasm32-unknown-unknown \
python3 -m pip install flask \
cargo install trunk
```

after this, just run the `run.sh` file and it *should* work