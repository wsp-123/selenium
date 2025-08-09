#!/usr/bin/env bash
set -euo pipefail

# Install Firefox from Mozilla's APT repo (latest version, avoids Snap)
echo "Setting up Mozilla APT repository for Firefox..."

# Create keyring directory
sudo install -d -m 0755 /etc/apt/keyrings

# Import signing key
wget -q https://packages.mozilla.org/apt/repo-signing-key.gpg -O- \
  | sudo tee /etc/apt/keyrings/packages.mozilla.org.asc > /dev/null

# Add repository to sources
echo "deb [signed-by=/etc/apt/keyrings/packages.mozilla.org.asc] https://packages.mozilla.org/apt mozilla main" \
  | sudo tee /etc/apt/sources.list.d/mozilla.list > /dev/null

# Pin Mozilla packages with highest priority
echo '
Package: *
Pin: origin packages.mozilla.org
Pin-Priority: 1000
' | sudo tee /etc/apt/preferences.d/mozilla

# Install Firefox
sudo apt-get update -y
sudo apt-get install -y firefox

# Install Python deps
pip install --upgrade pip
pip install -r requirements.txt

# Run the service
echo "Starting Flask app on 0.0.0.0:8080..."
python3 app.py
