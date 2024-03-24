# Backend
FROM python:latest

COPY backend/ /backend/

WORKDIR /backend

RUN pip install flask

EXPOSE 5000

CMD ["python3", "main.py"]

# Frontend
FROM rust:latest

COPY frontend /frontend/

WORKDIR /frontend

RUN cargo install trunk

CMD ["trunk", "serve"]
