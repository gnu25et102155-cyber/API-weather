import requests
from flask import Flask, jsonify, send_file, request
from datetime import datetime
import socket

app = Flask(__name__)
API_KEY = "91e828401c93afe11fefff459b786295"

def get_device_ip():
    """Get local device IP"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "localhost"

@app.route('/')
def home():
    """Serve home page"""
    return send_file('index.html', mimetype='text/html')

@app.route('/style.css')
def style():
    """Serve CSS"""
    return send_file('style.css', mimetype='text/css')

@app.route('/api/weather/<city>')
def weather(city):
    """Get weather for a city"""
    try:
        api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(api_url, timeout=10)
        data = response.json()
        
        if response.status_code == 200:
            sunrise = datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M:%S')
            sunset = datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M:%S')
            
            return jsonify({
                "success": True,
                "location": f"{data['name']}, {data['sys']['country']}",
                "temperature": round(data["main"]["temp"], 1),
                "feels_like": round(data["main"]["feels_like"], 1),
                "description": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"],
                "wind_speed": round(data["wind"]["speed"], 2),
                "pressure": data["main"]["pressure"],
                "visibility": round(data.get("visibility", 0) / 1000, 1),
                "sunrise": sunrise,
                "sunset": sunset,
                "country": data['sys']['country']
            })
        else:
            return jsonify({"success": False, "error": data.get("message", "City not found")}), 400
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/location')
def location():
    """Get current location from IP"""
    try:
        user_ip = request.remote_addr
        if request.headers.getlist("X-Forwarded-For"):
            user_ip = request.headers.getlist("X-Forwarded-For")[0]
        
        # Try ipapi.co
        geo_url = f"https://ipapi.co/{user_ip}/json/"
        geo_response = requests.get(geo_url, timeout=5)
        geo_data = geo_response.json()
        
        if geo_data.get('country_code'):
            return jsonify({
                "success": True,
                "ip": user_ip,
                "city": geo_data.get('city', 'Unknown'),
                "country": geo_data.get('country_name', 'Unknown'),
                "country_code": geo_data.get('country_code', ''),
                "latitude": geo_data.get('latitude'),
                "longitude": geo_data.get('longitude')
            })
        else:
            return jsonify({"success": False, "error": "Could not determine location"}), 400
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == '__main__':
    ip = get_device_ip()
    print("\n" + "="*60)
    print("🌍 WEATHER APP RUNNING")
    print("="*60)
    print(f"Local:   http://localhost:8000")
    print(f"Network: http://{ip}:8000")
    print("="*60 + "\n")
    app.run(host='0.0.0.0', port=8000, debug=False)
