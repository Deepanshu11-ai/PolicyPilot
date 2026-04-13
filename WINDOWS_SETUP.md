# PolicyPilot - Windows Setup Guide 🪟

Complete guide for setting up PolicyPilot on Windows.

---

## Prerequisites

### 1. Install Python 3.9+

1. Go to https://www.python.org/downloads/
2. Download Windows installer
3. **IMPORTANT:** Check ✅ "Add Python to PATH"
4. Click "Install Now"
5. Verify:
   ```cmd
   python --version
   ```

### 2. Install Node.js

1. Go to https://nodejs.org/
2. Download LTS version
3. Run installer with default settings
4. Verify in Command Prompt:
   ```cmd
   node --version
   npm --version
   ```

### 3. Install Git (Optional but Recommended)

1. Go to https://git-scm.com/download/win
2. Run installer with default settings
3. Verify:
   ```cmd
   git --version
   ```

---

## Setup Steps

### Step 1: Clone Repository

Open Command Prompt and run:

```cmd
cd Desktop
git clone https://github.com/Deepanshu11-ai/policypilot.git
cd policypilot
```

Or without Git:
1. Download ZIP from GitHub
2. Extract to desired location
3. Open Command Prompt in the folder

### Step 2: Backend Setup

```cmd
cd insurance_ai

# Create virtual environment
python -m venv .venv

# Activate virtual environment
.venv\Scripts\activate

# Upgrade pip
python -m pip install --upgrade pip

# Install dependencies (this will take 5-10 minutes)
pip install -r requirements.txt

# Create required directories
mkdir media
mkdir vector_db
mkdir chroma_db

# Apply database migrations
python manage.py migrate

# Train ML model (this will take 2-3 minutes)
python core/ml/train.py
```

**Verify activation:** Command prompt should show `(.venv)` prefix.

### Step 3: Create Environment Variables File

1. In `insurance_ai\` folder, create a new file named `.env`
2. Add these lines:
```
GROQ_API_KEY=your_actual_groq_api_key_here
DJANGO_SECRET_KEY=dev-secret-key-windows
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

Get your Groq API key:
1. Visit https://console.groq.com/
2. Sign up or log in
3. Create new API key
4. Copy and paste in `.env`

### Step 4: Frontend Setup

Open new Command Prompt window (don't close the first one):

```cmd
cd policypilot\frontend

# Install dependencies (this will take 3-5 minutes)
npm install
```

---

## Running the Application

### Start Backend Server

In first Command Prompt window:
```cmd
cd policypilot\insurance_ai
.venv\Scripts\activate
python manage.py runserver
```

You should see:
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

### Start Frontend Server

In second Command Prompt window:
```cmd
cd policypilot\frontend
npm start
```

You should see:
```
Compiled successfully!

You can now view frontend in the browser.
  Local:            http://localhost:3000
```

### Access Application

1. **Frontend:** Open browser and go to http://localhost:3000
2. **Backend API:** http://127.0.0.1:8000/api/
3. **Admin Panel:** http://127.0.0.1:8000/admin

---

## First Test

1. On http://localhost:3000, you should see the PolicyPilot interface
2. Upload a PDF from the `sample pdf\` folder
3. Click "Set Active Policy"
4. Click "Get Coverage Details"
5. Try other features!

---

## Common Windows Commands Reference

```cmd
# Navigate directories
cd folder_name          # Go into folder
cd ..                   # Go up one level
dir                     # List files and folders
cls                     # Clear screen

# Python
python --version        # Check Python version
python -m venv .venv    # Create virtual environment
.venv\Scripts\activate  # Activate virtual environment
.venv\Scripts\deactivate # Deactivate virtual environment
pip install package     # Install a package
pip list                # List installed packages

# Node.js
node --version          # Check Node.js version
npm --version           # Check npm version
npm install             # Install dependencies
npm start               # Start development server

# Git
git clone url           # Clone repository
git status              # Check status
git pull                # Update from remote

# File operations
mkdir folder            # Create folder
rmdir folder            # Delete empty folder
del file                # Delete file
type file.txt           # View file contents
```

---

## Troubleshooting for Windows

### Issue: "Python is not recognized as an internal or external command"

**Solution 1:**
- Reinstall Python and CHECK ✅ "Add Python to PATH"
- Restart Command Prompt after reinstalling

**Solution 2:**
- Use full path:
```cmd
C:\Users\YourUsername\AppData\Local\Programs\Python\Python311\python.exe --version
```

### Issue: "npm is not recognized..."

**Solution:**
- Reinstall Node.js
- Restart Command Prompt
- Verify: `npm --version`

### Issue: Virtual environment not activating

**Make sure you're in the correct folder:**
```cmd
cd insurance_ai
.venv\Scripts\activate
```

**You should see `(.venv)` in the prompt.**

### Issue: "ModuleNotFoundError: No module named 'django'"

**Solution:**
1. Check virtual environment is activated (should see `.venv` in prompt)
2. Reinstall dependencies:
```cmd
pip install -r requirements.txt
```

### Issue: "Port 8000 is already in use"

**Solution:**
```cmd
# Use a different port
python manage.py runserver 8001

# Or find and kill the process
netstat -ano | findstr :8000
taskkill /PID <PID_NUMBER> /F
```

### Issue: "Port 3000 is already in use"

**Solution:**
```cmd
# Use a different port
set PORT=3001
npm start

# Or find and kill the process
netstat -ano | findstr :3000
taskkill /PID <PID_NUMBER> /F
```

### Issue: ".env file not found"

**Solution:**
1. Make sure you're in the `insurance_ai\` folder
2. Create file named `.env` (note: no extension)
3. Open with Notepad and add your API key

**To create .env file in Command Prompt:**
```cmd
cd insurance_ai
type nul > .env
notepad .env
```

### Issue: "SSL Certificate error" when downloading packages

**Solution 1:**
```cmd
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
```

**Solution 2:**
- Check internet connection
- Try again later
- Check if corporate firewall is blocking downloads

### Issue: "Groq API key not working"

**Solution:**
1. Get new key from https://console.groq.com/
2. Make sure `.env` file has correct format:
```
GROQ_API_KEY=your_key_here
```
3. No quotes around the key
4. Restart Django server after updating `.env`

### Issue: Embeddings take very long time

This is normal! First time download can take 5-10 minutes:
- HuggingFace downloads ~200MB model
- Subsequent uses will be much faster
- Ensure stable internet connection

---

## Reinstall Everything (Fresh Start)

If something goes wrong, you can start fresh:

```cmd
# Delete virtual environment
rmdir /s .venv

# Delete node_modules
cd frontend
rmdir /s node_modules
cd ..

# Delete databases
del db.sqlite3
rmdir /s vector_db
rmdir /s chroma_db

# Now follow Setup Steps again from Step 2
```

---

## Step-by-Step Video Alternative

If you prefer video guides:
1. Search "How to install Python Windows" on YouTube
2. Search "How to install Node.js Windows" on YouTube
3. Follow the installation steps in those videos first

---

## File Structure (What You Should See)

```
C:\Users\YourUsername\...\policypilot\
├── insurance_ai\
│   ├── .venv\              (Created after setup)
│   ├── core\
│   ├── media\              (Created during setup)
│   ├── vector_db\          (Created during setup)
│   ├── chroma_db\          (Created during setup)
│   ├── db.sqlite3          (Created after migrate)
│   ├── .env                (Create manually)
│   ├── requirements.txt
│   ├── manage.py
│   └── ...
├── frontend\
│   ├── node_modules\       (Created after npm install)
│   ├── src\
│   ├── public\
│   ├── package.json
│   └── ...
├── sample pdf\
│   └── *.pdf               (Sample files for testing)
└── ...
```

---

## Testing (After Setup)

### Test 1: Backend API
```cmd
curl -X GET http://127.0.0.1:8000/api/
```

Or open in browser: http://127.0.0.1:8000/api/

### Test 2: Frontend
Open browser: http://localhost:3000

### Test 3: Upload Policy
1. Open http://localhost:3000
2. Click "Choose File" and select a PDF
3. Click "Upload PDF Policy"
4. Should see success message with Policy ID

---

## Performance Notes for Windows

- **First run:** Slower (downloads models)
- **Embedding generation:** 2-5 minutes per PDF
- **Subsequent runs:** Much faster
- **RAM usage:** ~2GB (keep other programs closed)

---

## Next Steps

1. ✅ Follow all setup steps
2. ✅ Run both servers
3. ✅ Access http://localhost:3000
4. ✅ Upload and test with sample PDFs
5. ✅ Try all features
6. ✅ Read documentation for deeper understanding

---

## Useful Resources

- Python Docs: https://docs.python.org/3/
- Node.js Docs: https://nodejs.org/docs/
- Django Docs: https://docs.djangoproject.com/
- React Docs: https://react.dev/
- Groq Docs: https://console.groq.com/docs

---

**Still having issues?** 
Check [SETUP_GUIDE.md Troubleshooting](SETUP_GUIDE.md#troubleshooting) for more detailed solutions.

---

**Last Updated:** April 13, 2026  
**Version:** 1.0  
**Status:** Windows Compatible ✅
