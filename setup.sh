#!/bin/bash

echo "--------------------------------------------------------"
echo "  Energy Trading Blockchain - Streamlit Launcher"
echo "--------------------------------------------------------"

# 1. Virtual environment check
if [ ! -d "venv" ]; then
    echo "[1/3] Creating Python virtual environment..."
    python3 -m venv venv
fi

echo "[2/3] Installing Python dependencies..."
source venv/bin/activate
pip install -q -r requirements.txt

echo "[3/3] Launching Streamlit Energy Trading Dashboard..."
cd streamlit_app
streamlit run app.py
