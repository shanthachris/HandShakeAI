FROM python:3.12.6-slim@sha256:ad48727987b259854d52241fac3bc633574364867b8e20aec305e6e7f4028b26

RUN pip install --no-cache-dir pytest==8.4.1

WORKDIR /app

COPY access.log /app/access.log
