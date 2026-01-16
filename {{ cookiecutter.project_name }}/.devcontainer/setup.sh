#!/bin/bash

set -e

echo "Installing uv..."
curl -LsSf https://astral.sh/uv/install.sh | sh > /dev/null 2>&1
echo "✅ uv installed."

echo "Installing system dependencies..."
sudo apt-get update > /dev/null 2>&1
sudo apt-get install -y build-essential > /dev/null 2>&1
echo "✅ System dependencies installed."

echo "Installing Python dependencies with Makefile..."
make setup > /dev/null 2>&1

echo "✅ Devcontainer setup complete."