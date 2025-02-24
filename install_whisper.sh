#!/bin/bash

echo "📦 Installing system dependencies..."
sudo apt update && sudo apt install -y ffmpeg python3 python3-pip tmux nvidia-cuda-toolkit

echo "🐍 Installing Python libraries..."
pip3 install -r requirements.txt

echo "🛠️ Creating watch folder..."
mkdir -p /home/user/watch_folder

echo "✅ Installation complete! Set up the API key and run start_server.sh"
