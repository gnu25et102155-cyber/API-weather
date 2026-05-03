# 🌤️ Weather App - Independent Device Setup Guide

## Overview
This weather app is designed to work **independently on each device**. When you shut down your main device, other devices won't be affected if they're running their own copy of the app.

## Setup Instructions for Each Device

### Step 1: Copy Files to the Device
Copy these 4 files to the target device:
```
- weather.py (the server)
- index.html (the web interface)
- style.css (styling)
- requirements.txt (dependencies)
```

### Step 2: Install Dependencies
On the target device, open terminal and run:
```bash
python setup_device.py
```

Or manually:
```bash
pip install -r requirements.txt
```

### Step 3: Start the Weather App Server
```bash
python weather.py
```

You should see:
```
======================================================================
🌤️  WEATHER APP SERVER STARTED
======================================================================
📍 Device IP: 192.168.1.100
🌐 Local Access: http://localhost:8000
📱 Network Access (on other devices): http://192.168.1.100:8000
======================================================================
```

### Step 4: Access the App
- **On the same device**: Open browser → `http://localhost:8000`
- **From another device on the same network**: `http://<device-ip>:8000`

## Important! 🎯

✅ **Each device runs independently**
- Device A can shut down - Device B will still work
- Device B can shut down - Device A will still work
- No dependency between devices

❌ **What WON'T work**
- Accessing Device B's app from Device A if Device B is powered off
- Accessing Device A's app from Device B if Device A is powered off

## Finding Your Device IP

### On Windows:
```bash
ipconfig
```
Look for "IPv4 Address" (usually starts with 192.168.x.x)

### On Mac/Linux:
```bash
hostname -I
```
or
```bash
ifconfig
```

## API Endpoints

Each running device provides these endpoints:

**Get Weather Data:**
```
GET http://device-ip:8000/api/weather/{city}
```
Example: `http://192.168.1.100:8000/api/weather/London`

**Check Device Status:**
```
GET http://device-ip:8000/api/device-info
```

## Troubleshooting

**Port 8000 already in use?**
- Change the port in `weather.py` line with `app.run(host='0.0.0.0', port=8000, ...)`
- Use a different port number like 8001, 8002, etc.

**Can't connect from another device?**
1. Make sure both devices are on the same Wi-Fi network
2. Check firewall settings - port 8000 might be blocked
3. Use the correct device IP (from `hostname -I`)

**API calls failing?**
- Verify internet connection (needed to call OpenWeatherMap API)
- Check API key in weather.py is valid
- Use `/api/device-info` endpoint to verify server is running

## Deployment Options

### Option 1: Run Manually (Recommended for Testing)
```bash
python weather.py
```

### Option 2: Run in Background (Linux/Mac)
```bash
nohup python weather.py > weather.log 2>&1 &
```

### Option 3: Auto-start on Boot
Create a systemd service (Linux) or Use Task Scheduler (Windows) to auto-start at boot.

---

**Remember**: Each device must have its own running copy of the app. Set up once, then your app will work independently! 🚀
