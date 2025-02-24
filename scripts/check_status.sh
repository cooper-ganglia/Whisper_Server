#!/bin/bash
tmux ls | grep whisper-server && echo "✅ Whisper Server is running." || echo "❌ Whisper Server is NOT running."
