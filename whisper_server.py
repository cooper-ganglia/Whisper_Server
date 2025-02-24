import os
import time
import logging
import whisper
import torch
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from openai import OpenAI

# Logging setup
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

# Configuration
folder_to_watch = '/Users/tyler/Desktop/WATCH FOLDER'  # Your specified folder
openai_api_key = 'YOUR API KEY HERE'  # Your OpenAI key
client = OpenAI(api_key=openai_api_key)

# Check if GPU is available
device = "cuda" if torch.cuda.is_available() else "cpu"
logging.info(f"🔄 Using device: {device}")

# Load Whisper model
model = whisper.load_model("medium").to(device)
client = OpenAI(api_key=openai_api_key)

# File handler class
class NewFileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        
        file_path = event.src_path
        logging.info(f"📂 New file detected: {file_path}")

        # Wait for file to be fully copied
        time.sleep(5)
        
        # Transcribe audio
        transcription = model.transcribe(file_path, verbose=True)
        if transcription:
            text = transcription["text"]
            transcript_file = f"{file_path}.txt"
            with open(transcript_file, "w") as f:
                f.write(text)
            logging.info(f"✅ Transcription saved: {transcript_file}")

            # Send to ChatGPT for summarization
            summary = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "Summarize this text in 50 words or less."},
                    {"role": "user", "content": text}
                ]
            ).choices[0].message.content
            
            summary_file = f"{file_path}_summary.txt"
            with open(summary_file, "w") as f:
                f.write(summary)
            logging.info(f"✅ Summary saved: {summary_file}")

observer = Observer()
observer.schedule(NewFileHandler(), watch_folder, recursive=False)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
