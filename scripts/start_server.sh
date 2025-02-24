#!/bin/bash
tmux new -d -s whisper-server "python3 /home/user/whisper_server.py"
echo "✅ Whisper Server started in tmux. Use 'tmux attach -t whisper-server' to check logs."
