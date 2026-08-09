#!/bin/bash

set -e

echo "Instalando dependencias del sistema..."
sudo apt update
sudo apt install -y python3 python3-pip graphviz

echo "Instalando dependencias de Python..."
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

echo "Instalación completada."
