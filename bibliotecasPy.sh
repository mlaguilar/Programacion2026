#!/bin/bash

# Instalador de bibliotecas Python + ffmpeg

set -e

echo "Actualizando pip..."
python3 -m pip install --upgrade pip

echo "Instalando bibliotecas Python..."
pip3 install numpy matplotlib pandas scipy sympy numba

# ==============================
# Instalación de ffmpeg
# ==============================

echo "Instalando ffmpeg..."

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Ubuntu / Debian
    sudo apt update
    sudo apt install -y ffmpeg

elif [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS (requiere brew)
    if ! command -v brew &> /dev/null; then
        echo "Homebrew no está instalado. Instálalo primero: https://brew.sh/"
        exit 1
    fi
    brew install ffmpeg

elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    echo "En Windows debes instalar ffmpeg manualmente:"
    echo "https://ffmpeg.org/download.html"
    echo "Y agregarlo al PATH."
else
    echo "Sistema operativo no reconocido para instalar ffmpeg automáticamente."
fi

# ==============================
# Verificación
# ==============================

echo "Verificando instalación de Python..."

python3 -c "import numpy; print('numpy:', numpy.__version__)"
python3 -c "import matplotlib; print('matplotlib:', matplotlib.__version__)"
python3 -c "import pandas; print('pandas:', pandas.__version__)"
python3 -c "import scipy; print('scipy:', scipy.__version__)"
python3 -c "import sympy; print('sympy:', sympy.__version__)"
python3 -c "import numba; print('numba:', numba.__version__)"

echo "Verificando ffmpeg..."
if command -v ffmpeg &> /dev/null; then
    ffmpeg -version | head -n 1
    echo "ffmpeg instalado correctamente"
else
    echo "ffmpeg NO está disponible"
fi

echo "Instalación completa"