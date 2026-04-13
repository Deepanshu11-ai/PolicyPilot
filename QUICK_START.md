# PolicyPilot - Quick Start Guide ⚡

**Get PolicyPilot running in 15 minutes!**

For detailed setup instructions, see [SETUP_GUIDE.md](SETUP_GUIDE.md)

---

## Prerequisites (5 minutes)

Ensure you have installed:
- Python 3.9+ ([Download](https://www.python.org/downloads/))
- Node.js 14+ ([Download](https://nodejs.org/))
- Git

Verify:
```bash
python --version
node --version
npm --version
```

---

## Setup (10 minutes)

### 1. Clone & Navigate
```bash
git clone https://github.com/Deepanshu11-ai/policypilot.git
cd policypilot
```

### 2. Backend Setup
```bash
cd insurance_ai

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create directories
mkdir -p media vector_db chroma_db

# Set up database
python manage.py migrate

# Train ML model
python core/ml/train.py
```

### 3. Create .env File
Create `insurance_ai/.env`:
```
GROQ_API_KEY=your_api_key_here
DJANGO_SECRET_KEY=dev-secret-key
DEBUG=True
```

Get your Groq API key from: https://console.groq.com/

### 4. Frontend Setup
```bash
cd ../frontend
npm install
```

---

## Run (⚡ 1 minute)

### Terminal 1: Backend
```bash
cd insurance_ai
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python manage.py runserver
```

### Terminal 2: Frontend
```bash
cd frontend
npm start
```

---

## Access

- **Frontend:** http://localhost:3000
- **Backend API:** http://127.0.0.1:8000/api/
- **Admin Panel:** http://127.0.0.1:8000/admin

---

## First Steps

1. ✅ Open http://localhost:3000
2. ✅ Upload a PDF from `sample pdf/` folder
3. ✅ Set as active policy
4. ✅ Try each feature!

---

## Issues?

Check [SETUP_GUIDE.md Troubleshooting section](SETUP_GUIDE.md#troubleshooting) for solutions to common problems.

**Most common issues:**
- "Module not found" → Verify virtual environment is activated
- "Groq key not found" → Check `.env` file exists with API key
- "Port already in use" → Use different port: `python manage.py runserver 8001`

---

**Total Setup Time:** ~15 minutes ⏱️

Enjoy using PolicyPilot! 🎉
