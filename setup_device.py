#!/usr/bin/env python3
"""
Setup script to configure the weather app on a new device
Run this once on each device to install dependencies
"""

import subprocess
import sys
import os

def install_dependencies():
    """Install required Python packages"""
    print("📦 Installing required packages...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    print("✅ Dependencies installed successfully!")

def get_device_info():
    """Display information about running the app"""
    print("\n" + "="*60)
    print("🌤️ Weather App - Device Setup Complete!")
    print("="*60)
    print("\n✨ To run the weather app on this device:")
    print("   python weather.py")
    print("\n📱 Then access it from any device on your network:")
    print("   - Find this device's IP: hostname -I")
    print("   - Open browser: http://<device-ip>:8000")
    print("\n💡 Example: http://192.168.1.100:8000")
    print("="*60 + "\n")

if __name__ == "__main__":
    try:
        install_dependencies()
        get_device_info()
    except Exception as e:
        print(f"❌ Error during setup: {e}")
        sys.exit(1)
