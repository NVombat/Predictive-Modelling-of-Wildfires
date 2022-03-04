#!/bin/bash
echo "[KILLING-SERVER] [PORT] 8000"

#KILLING APPLICATION
sudo fuser -k 8000/tcp

echo "SERVER KILLED ON PORT [8000]"
