import requests
from flask import Flask, jsonify, send_file, render_template_string, request
import os
import socket
from datetime import datetime

app = Flask(__name__)

# API Key - can be set via environment variable for security
API_KEY = os.getenv("WEATHER_API_KEY", "91e828401c93afe11fefff459b786295")

def get_device_ip():
    """Get the local IP address of this device"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "localhost"

def get_country_emoji(country_code):
    """Convert country code to flag emoji"""
    try:
        return ''.join(chr(127397 + ord(char)) for char in country_code)
    except:
        return "🌍"

@app.route('/')
def serve_frontend():
    """Serve the HTML frontend"""
    return send_file('index.html')

@app.route('/style.css')
def serve_css():
    """Serve the CSS file"""
    return send_file('style.css', mimetype='text/css')

@app.route('/api/weather/<city>')
def get_weather_api(city):
    """API endpoint to get weather data in JSON format"""
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            # Convert Unix timestamps to readable time
            sunrise = datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M:%S')
            sunset = datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M:%S')
            
            return jsonify({
                "success": True,
                "location": f"{data['name']}, {data['sys']['country']}",
                "temperature": data["main"]["temp"],
                "feels_like": data["main"]["feels_like"],
                "description": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"],
                "pressure": data["main"]["pressure"],
                "visibility": data.get("visibility", 0),
                "sunrise": sunrise,
                "sunset": sunset,
                "country": data['sys']['country']
            })
        else:
            return jsonify({
                "success": False,
                "error": data.get("message", "Something went wrong")
            }), 400
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/api/device-info')
def device_info():
    """Get information about this device"""
    return jsonify({
        "device_ip": get_device_ip(),
        "server_status": "running",
        "message": "This app instance is running independently on this device"
    })

@app.route('/api/current-location')
def get_current_location():
    """Detect user's current location based on their IP address"""
    try:
        # Get user's IP address
        user_ip = request.remote_addr
        
        # Check for proxy/VPN (X-Forwarded-For header)
        if request.headers.getlist("X-Forwarded-For"):
            user_ip = request.headers.getlist("X-Forwarded-For")[0]
        
        print(f"🌍 User IP: {user_ip}")
        
        # Try ip-api.com first
        try:
            geo_url = f"http://ip-api.com/json/{user_ip}?fields=status,country,countryCode,city,lat,lon"
            geo_response = requests.get(geo_url, timeout=5)
            geo_data = geo_response.json()
            
            if geo_data.get('status') == 'success':
                country_emoji = get_country_emoji(geo_data.get('countryCode', ''))
                
                return jsonify({
                    "success": True,
                    "ip": user_ip,
                    "city": geo_data.get('city', 'Unknown'),
                    "country": geo_data.get('country', 'Unknown'),
                    "country_code": geo_data.get('countryCode', ''),
                    "country_emoji": country_emoji,
                    "latitude": geo_data.get('lat'),
                    "longitude": geo_data.get('lon')
                })
        except Exception as e1:
            print(f"⚠️ ip-api.com failed: {str(e1)}")
        
        # Fallback: Use ipapi.co
        try:
            geo_url2 = f"https://ipapi.co/{user_ip}/json/"
            geo_response2 = requests.get(geo_url2, timeout=5)
            geo_data2 = geo_response2.json()
            
            if geo_data2.get('country_code'):
                country_emoji = get_country_emoji(geo_data2.get('country_code', ''))
                
                return jsonify({
                    "success": True,
                    "ip": user_ip,
                    "city": geo_data2.get('city', 'Unknown'),
                    "country": geo_data2.get('country_name', 'Unknown'),
                    "country_code": geo_data2.get('country_code', ''),
                    "country_emoji": country_emoji,
                    "latitude": geo_data2.get('latitude'),
                    "longitude": geo_data2.get('longitude')
                })
        except Exception as e2:
            print(f"⚠️ ipapi.co failed: {str(e2)}")
        
        # If both fail, return a helpful response
        return jsonify({
            "success": False,
            "ip": user_ip,
            "error": "Location services temporarily unavailable. Try searching for a city directly."
        }), 503
            
    except Exception as e:
        print(f"❌ Location detection error: {str(e)}")
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

if __name__ == '__main__':
    device_ip = get_device_ip()
    print("\n" + "="*70)
    print("🌤️  WEATHER APP SERVER STARTED")
    print("="*70)
    print(f"📍 Device IP: {device_ip}")
    print(f"🌐 Local Access: http://localhost:8000")
    print(f"📱 Network Access (on other devices): http://{device_ip}:8000")
    print("\n💡 IMPORTANT: Each device needs to run this server independently")
    print("   When this device shuts down, the app will stop working here")
    print("   Other devices must run their own copy of this app")
    print("="*70 + "\n")
    
    # Run the server on all available network interfaces
    app.run(host='0.0.0.0', port=8000, debug=False)