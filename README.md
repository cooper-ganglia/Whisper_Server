# Whisper Transcription Server (Linux + GPU)

This repository provides an automated transcription and summarization server using **OpenAI's Whisper** for speech-to-text and **GPT-4o** for text summarization. Designed to run on a **Linux server with an NVIDIA GPU**, it watches a folder for new audio/video files, transcribes them, generates a summary, and saves the results.

---

## 📦 Installation

### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/whisper-transcription-server.git
cd whisper-transcription-server
```

### **2. Run the Install Script**
```bash
chmod +x install_whisper.sh
./install_whisper.sh
```
This installs all necessary system packages, Python dependencies, and prepares the environment.

### **3. Add Your OpenAI API Key**
Edit `whisper_server.py` and replace `'YOUR API KEY HERE'` with your actual OpenAI API key:
```python
openai_api_key = 'YOUR API KEY HERE'
```

### **4. Start the Server**
```bash
./scripts/start_server.sh
```

---

## 🚀 Usage

- **Check logs:**  
  ```bash
  tmux attach -t whisper-server
  ```

- **Stop the server:**  
  ```bash
  ./scripts/stop_server.sh
  ```

- **Check server status:**  
  ```bash
  ./scripts/check_status.sh
  ```

---

## 🛠️ Auto-Start on Boot (Linux Systemd)
To enable the transcription server to start automatically on reboot:
```bash
sudo cp whisper.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable whisper.service
sudo systemctl start whisper.service
```

To check service status:
```bash
systemctl status whisper.service
```

---


Your **Whisper Transcription Server** is now fully set up and ready to be shared and deployed! 🚀

