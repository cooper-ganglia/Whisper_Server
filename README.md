# Whisper Transcription Server (Linux + GPU)

## 📦 Installation

1. Clone this repository or copy these files to the server.

2. Run the install script:
   ```bash
   chmod +x install_whisper.sh
   ./install_whisper.sh

3. Open the whisper_server.py file and replace 'YOUR API KEY HERE' with your actual OpenAI API key:
openai_api_key = 'YOUR API KEY HERE'

4. Start the server:
./scripts/start_server.sh


🚀 Usage
To check logs:

tmux attach -t whisper-server
To stop the server:

./scripts/stop_server.sh
To check status:

./scripts/check_status.sh
🛠️ Auto-Start on Boot
Enable systemd service:

sudo cp whisper.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable whisper.service
sudo systemctl start whisper.service