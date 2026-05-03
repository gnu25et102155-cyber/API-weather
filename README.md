# 🌤️ API-Weather App

A simple weather application that works independently on each device without relying on a central server.

## Features

✨ **Independent Operation** - Each device runs its own copy
📱 **Network Accessible** - Access from any device on the network  
🌡️ **Real-time Data** - Live weather from OpenWeatherMap API
🎨 **Clean UI** - Modern, responsive interface
🔌 **No Central Server Needed** - Each device is self-contained

## Quick Start

### Option 1: Automatic Setup (Recommended)
```bash
python setup_device.py
python weather.py
```

### Option 2: Manual Setup
```bash
pip install -r requirements.txt
python weather.py
```

### Access the App
- **Local**: http://localhost:8000
- **Network**: http://<your-device-ip>:8000

## Setup on Multiple Devices

Each device needs its own running copy:

1. **Device A**: Copy files → Install → Run server
2. **Device B**: Copy files → Install → Run server  
3. **Device C**: Copy files → Install → Run server

Now all devices work independently! 🚀

## API Endpoints

Get weather data from any running device:
```bash
curl http://localhost:8000/api/weather/London
```

Check device status:
```bash
curl http://localhost:8000/api/device-info
```

## Project Structure

```
API-weather/
├── weather.py              # Flask server (run this on each device)
├── index.html              # Web frontend
├── style.css               # Styling
├── requirements.txt        # Python dependencies
├── setup_device.py         # Auto setup script
├── DEPLOYMENT_GUIDE.md     # Detailed setup instructions
└── README.md               # This file
```

## Configuration

### Custom API Key
Set your own OpenWeatherMap API key:
```bash
export WEATHER_API_KEY="your_api_key_here"
python weather.py
```

### Custom Port
Edit `weather.py` and change port 8000 to your preferred port:
```python
app.run(host='0.0.0.0', port=8001, debug=False)
```

## Troubleshooting

See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for detailed troubleshooting.

## Requirements

- Python 3.7+
- Flask
- Requests library
- Internet connection (for weather data)

## License

Open source - Use freely!

## Support

For detailed setup instructions, see [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)