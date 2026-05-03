# 🌍 Weather App - Quick Start Guide

## ✅ Your Code is Now Saved!

**GitHub Repository:** https://github.com/gnu25et102155-cyber/API-weather

## 📥 How to Clone to Your Personal Computer

### Option 1: Using Command Line (Recommended)

#### **Windows, Mac, or Linux:**

1. **Install Git** (if not already installed)
   - Windows: https://git-scm.com/download/win
   - Mac: `brew install git`
   - Linux: `sudo apt install git`

2. **Open Terminal/Command Prompt** and run:
   ```bash
   git clone https://github.com/gnu25et102155-cyber/API-weather.git
   cd API-weather
   ```

3. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app:**
   ```bash
   python weather.py
   ```

5. **Open in browser:**
   ```
   http://localhost:8000
   ```

### Option 2: GitHub Desktop (Easier for Beginners)

1. Download GitHub Desktop: https://desktop.github.com/
2. Sign in with your GitHub account
3. Click "Clone a repository"
4. Select: `gnu25et102155-cyber/API-weather`
5. Choose where to save on your computer
6. Click "Clone"

Then open terminal in the folder and run:
```bash
pip install -r requirements.txt
python weather.py
```

### Option 3: Direct Download (No Git)

1. Go to: https://github.com/gnu25et102155-cyber/API-weather
2. Click green **Code** button
3. Click **Download ZIP**
4. Extract the ZIP file
5. Open terminal in that folder
6. Run:
   ```bash
   pip install -r requirements.txt
   python weather.py
   ```

---

## 💻 Running on Your Personal Computer

### **Option 1: Python Command (Simplest)**
```bash
python weather.py
```

### **Option 2: Background Process (Linux/Mac)**
Run in background and access later:
```bash
nohup python weather.py > weather.log 2>&1 &
```

Check if running:
```bash
ps aux | grep weather.py
```

Stop it:
```bash
pkill -f "python weather.py"
```

### **Option 3: Command Prompt (Windows)**
```cmd
start python weather.py
```

---

## 📱 Access the App

### **Local Computer:**
- Open browser → `http://localhost:8000`

### **From Another Device (Same WiFi):**
- Find your computer's IP: 
  - Windows: `ipconfig` → look for IPv4
  - Mac/Linux: `hostname -I`
- Open browser → `http://<your-ip>:8000`

### **Example:**
```
http://192.168.1.100:8000
```

---

## 🔄 Making Changes & Updating GitHub

### **After making changes:**

1. **Check what changed:**
   ```bash
   git status
   ```

2. **Stage your changes:**
   ```bash
   git add .
   ```

3. **Commit with a message:**
   ```bash
   git commit -m "Description of changes"
   ```

4. **Push to GitHub:**
   ```bash
   git push origin main
   ```

### **Example workflow:**
```bash
# Edit your files (e.g., style.css)

git status  # See what changed
git add .   # Prepare changes
git commit -m "Improved UI styling"
git push origin main  # Upload to GitHub
```

---

## 📊 Project Structure

```
API-weather/
├── weather.py              ← Main Flask server (RUN THIS!)
├── index.html              ← Web page (frontend)
├── style.css               ← Styling
├── requirements.txt        ← Python dependencies
├── setup_device.py         ← Device setup script
├── DEPLOYMENT_GUIDE.md     ← Detailed guide
├── README.md               ← Project info
└── .gitignore              ← Ignored files
```

---

## 🚀 Features

✅ Search weather for any city worldwide  
✅ Auto-detect location from IP address  
✅ Works with VPN (shows country of VPN)  
✅ Works on multiple devices independently  
✅ Search history saved locally  
✅ Detailed weather information  

---

## 🌐 Test Cities

Try these to test your app:
- London
- Tokyo
- New York
- Sydney
- Dubai
- Paris
- Mumbai
- Berlin

---

## ⚡ Common Commands

| Command | What it does |
|---------|-------------|
| `git clone <url>` | Download repo to your computer |
| `git status` | See what changed |
| `git add .` | Stage all changes |
| `git commit -m "msg"` | Save changes locally |
| `git push` | Upload to GitHub |
| `git pull` | Download latest from GitHub |
| `git log` | See commit history |
| `pip install -r requirements.txt` | Install dependencies |
| `python weather.py` | Run the app |

---

## 🔐 Git Setup (First Time Only)

Configure your identity:
```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@gmail.com"
```

Verify it worked:
```bash
git config --list
```

---

## 📞 Troubleshooting

### **"Port 8000 already in use"**
```bash
# Find what's using port 8000
lsof -i :8000

# Kill it
kill -9 <PID>

# Or use different port:
python weather.py  # Change port in weather.py
```

### **"ImportError: No module named requests"**
```bash
pip install requests flask
```

### **"Git command not found"**
- Install Git from: https://git-scm.com/

### **Can't access from another device**
- Make sure both devices are on same WiFi
- Check firewall allows port 8000
- Use correct IP address

---

## 💡 Pro Tips

1. **Keep your code synced:**
   ```bash
   git pull origin main  # Get latest changes
   ```

2. **See all changes since last commit:**
   ```bash
   git diff
   ```

3. **Undo recent commit:**
   ```bash
   git reset --soft HEAD~1
   ```

4. **See full commit history:**
   ```bash
   git log --oneline
   ```

5. **Create a backup branch:**
   ```bash
   git branch backup
   ```

---

## ✨ Next Steps

1. ✅ Clone repository to your computer
2. ✅ Install requirements
3. ✅ Run `python weather.py`
4. ✅ Test the app
5. ✅ Make changes (if needed)
6. ✅ Commit and push to GitHub

---

**Enjoy your weather app!** 🌍☀️🌧️
