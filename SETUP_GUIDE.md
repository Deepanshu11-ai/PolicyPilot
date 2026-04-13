# PolicyPilot - Setup Guide for New Machine 🚀

Complete step-by-step instructions for setting up PolicyPilot on a new machine.

---

## Table of Contents

1. [System Requirements](#system-requirements)
2. [Prerequisites Installation](#prerequisites-installation)
3. [Clone Repository](#clone-repository)
4. [Backend Setup (Django)](#backend-setup-django)
5. [Frontend Setup (React)](#frontend-setup-react)
6. [Configuration](#configuration)
7. [Database Setup](#database-setup)
8. [ML Model Setup](#ml-model-setup)
9. [Running the Application](#running-the-application)
10. [Testing](#testing)
11. [Troubleshooting](#troubleshooting)

---

## System Requirements

### Minimum Requirements
- **OS:** macOS, Linux, or Windows
- **Python:** 3.9 or higher
- **Node.js:** 14.0 or higher
- **npm:** 6.0 or higher
- **RAM:** 4GB minimum (8GB recommended)
- **Disk Space:** 5GB (for virtual environments and models)
- **Internet:** Required (for downloading models and LLM API calls)

### Recommended Setup
- **OS:** macOS or Linux (smoother experience)
- **Python:** 3.11 or higher
- **RAM:** 8GB or more
- **CPU:** Multi-core processor
- **GPU:** Optional (for faster embeddings)

---

## Prerequisites Installation

### macOS

#### 1. Install Homebrew (if not already installed)
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

#### 2. Install Python 3.11+
```bash
brew install python@3.11
python3 --version  # Verify installation
```

#### 3. Install Node.js
```bash
brew install node
node --version    # Verify installation
npm --version     # Verify npm installation
```

### Windows

#### 1. Install Python
- Download from https://www.python.org/downloads/
- Run installer and **CHECK: "Add Python to PATH"**
- Verify: Open Command Prompt and run `python --version`

#### 2. Install Node.js
- Download from https://nodejs.org/ (LTS version)
- Run installer with default settings
- Verify in Command Prompt: `node --version` and `npm --version`

### Linux (Ubuntu/Debian)

```bash
# Update package manager
sudo apt update
sudo apt upgrade

# Install Python
sudo apt install python3.11 python3.11-venv python3-pip

# Install Node.js
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install -y nodejs

# Verify installations
python3 --version
node --version
npm --version
```

---

## Clone Repository

### 1. Choose a Location
```bash
cd ~/projects  # or your preferred directory
```

### 2. Clone the Repository
```bash
git clone https://github.com/Deepanshu11-ai/policypilot.git
cd policypilot
```

### 3. Verify Structure
```bash
ls -la
# You should see:
# - insurance_ai/     (Django backend)
# - frontend/         (React frontend)
# - sample pdf/       (Sample policy files)
# - README.md
# - requirements.txt
```

---

## Backend Setup (Django)

### 1. Navigate to Backend Directory
```bash
cd insurance_ai
```

### 2. Create Virtual Environment
```bash
# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate

# Windows
python -m venv .venv
.venv\Scripts\activate
```

**Verify activation:** Your prompt should show `(.venv)` prefix.

### 3. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**Expected time:** 5-10 minutes (depending on internet speed)

### 4. Verify Installation
```bash
python -m pip list | grep -E "Django|langchain|chromadb"
# You should see:
# Django 6.0.4
# chromadb 1.5.7
# langchain 1.2.15
# langchain-community 0.4.1
```

---

## Frontend Setup (React)

### 1. Navigate to Frontend Directory
```bash
cd ../frontend
```

### 2. Install Dependencies
```bash
npm install
```

**Expected time:** 3-5 minutes

### 3. Verify Installation
```bash
npm --version
ls -la node_modules | head -20
```

---

## Configuration

### 1. Set Up Environment Variables

#### Backend (.env file)
Navigate to `insurance_ai/` directory:

```bash
cd insurance_ai
touch .env
```

Edit `.env` file with your Groq API key:
```
GROQ_API_KEY=your_actual_groq_api_key_here
DJANGO_SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

**Get Groq API Key:**
1. Visit https://console.groq.com/
2. Sign up / Log in
3. Create new API key
4. Copy the key to `.env`

#### Frontend (.env file - Optional)
Navigate to `frontend/` directory:

```bash
touch .env
```

Add:
```
REACT_APP_API_URL=http://127.0.0.1:8000
```

### 2. Create Required Directories
```bash
cd insurance_ai

# Create media directory for uploaded files
mkdir -p media

# Create vector_db directory for ChromaDB
mkdir -p vector_db

# Create chroma_db directory
mkdir -p chroma_db

# Verify
ls -la
```

---

## Database Setup

### 1. Apply Django Migrations
```bash
cd insurance_ai
python manage.py migrate
```

**Expected output:**
```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying ... OK
```

### 2. Create Superuser (Admin Account) - Optional
```bash
python manage.py createsuperuser
# Follow prompts for username, email, password
```

This allows access to Django admin at http://127.0.0.1:8000/admin

### 3. Verify Database
```bash
ls -la
# You should see db.sqlite3 file
```

---

## ML Model Setup

### 1. Train the Claim Prediction Model
```bash
cd insurance_ai
python core/ml/train.py
```

**Expected output:**
```
✅ Model trained & saved
```

### 2. Verify Model Creation
```bash
ls -la core/ml/models/
# You should see:
# - claim_model_3.pkl (trained model)
```

### 3. Download HuggingFace Embeddings (First Run)
The embeddings will be downloaded automatically on first use. This may take 2-3 minutes.

To pre-download manually:
```bash
python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('all-MiniLM-L6-v2')"
```

---

## Running the Application

### Option 1: Run Both Servers Separately (Recommended for Development)

#### Terminal 1: Django Backend
```bash
cd insurance_ai
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
python manage.py runserver
```

**Expected output:**
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

#### Terminal 2: React Frontend
```bash
cd frontend
npm start
```

**Expected output:**
```
Compiled successfully!

You can now view frontend in the browser.
  Local:            http://localhost:3000
  On Your Network:  http://xxx.xxx.x.x:3000
```

#### Access the Application
- **Frontend:** http://localhost:3000
- **Backend API:** http://127.0.0.1:8000/api/
- **Django Admin:** http://127.0.0.1:8000/admin

### Option 2: Run Backend Only (For API Testing)
```bash
cd insurance_ai
source .venv/bin/activate
python manage.py runserver
```

Then test with curl or Postman:
```bash
curl -X POST http://127.0.0.1:8000/api/upload-policy/ \
  -F "file=@sample.pdf"
```

---

## Testing

### 1. Test Backend Setup
```bash
cd insurance_ai

# Run Django tests
python manage.py test

# Test policy ID generation
python test_policy_id.py

# Test PDF upload process
python test_upload.py
```

### 2. Test API Endpoints

#### Test Upload Endpoint
```bash
curl -X POST http://127.0.0.1:8000/api/upload-policy/ \
  -F "file=@sample\ pdf/h1.pdf"
```

**Expected response:**
```json
{
  "message": "uploaded successfully",
  "policy_id": 16,
  "chunks": 120
}
```

#### Test Coverage Endpoint
```bash
curl "http://127.0.0.1:8000/api/coverage/?policy_id=1"
```

#### Test Ask Endpoint
```bash
curl -X POST http://127.0.0.1:8000/api/ask/ \
  -H "Content-Type: application/json" \
  -d '{"query":"What is covered?","policy_id":1}'
```

### 3. Test Frontend
1. Open http://localhost:3000
2. Upload a PDF from `sample pdf/` directory
3. Set it as active policy
4. Try each feature:
   - Coverage Analysis
   - Ask Questions
   - Scenario Simulation
   - Policy Score
   - Hidden Clauses Detection
   - Claim Prediction
   - Compare Policies

### 4. Manual Testing Workflow
```bash
# 1. Upload sample policy
# 2. Set active policy
# 3. Get coverage analysis
# 4. Ask a question about the policy
# 5. Simulate a scenario
# 6. Run claim prediction
# 7. Compare two policies
```

---

## Troubleshooting

### Issue: "Python not found" or "python: command not found"

**Solution:**
- macOS: Use `python3` instead of `python`
- Windows: Ensure Python is added to PATH (reinstall with PATH option checked)
- Linux: Install python3: `sudo apt install python3`

### Issue: "pip: command not found"

**Solution:**
```bash
python -m pip install --upgrade pip
# Then use: python -m pip install -r requirements.txt
```

### Issue: Virtual Environment Not Activating

**Solution:**
- macOS/Linux: `source .venv/bin/activate`
- Windows: `.venv\Scripts\activate`
- Verify: Prompt should show `(.venv)` prefix

### Issue: "Module not found" errors

**Solution:**
```bash
# Ensure virtual environment is activated
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate      # Windows

# Reinstall requirements
pip install -r requirements.txt
```

### Issue: "Groq API key not found"

**Solution:**
1. Create `.env` file in `insurance_ai/` directory
2. Add: `GROQ_API_KEY=your_key_here`
3. Get key from https://console.groq.com/
4. Restart Django server

### Issue: "Port 8000 already in use"

**Solution:**
```bash
# Use a different port
python manage.py runserver 8001

# Or kill the process using port 8000
# macOS/Linux:
lsof -i :8000
kill -9 <PID>

# Windows:
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

### Issue: "Port 3000 already in use"

**Solution:**
```bash
# Use a different port
PORT=3001 npm start

# Or kill the process
# macOS/Linux:
lsof -i :3000
kill -9 <PID>

# Windows:
netstat -ano | findstr :3000
taskkill /PID <PID> /F
```

### Issue: "Embedding generation failed"

**Solution:**
- Check internet connection
- Verify HuggingFace is accessible
- Clear cache: `rm -rf ~/.cache/huggingface/`
- Restart server

### Issue: "ChromaDB error: database locked"

**Solution:**
```bash
# Remove corrupted database
rm -rf vector_db/

# Restart server and re-upload
```

### Issue: "PDF upload fails silently"

**Solution:**
1. Check Django server logs for error messages
2. Verify PDF file is not corrupted: `file your_pdf.pdf`
3. Check disk space: `df -h`
4. Check folder permissions: `ls -la media/`

### Issue: Slow embedding generation

**Solution:**
- First run downloads models (takes 2-3 min)
- Subsequent runs are faster
- Larger PDFs take longer
- Consider GPU acceleration (if available)

### Issue: "No such file or directory: vector_db"

**Solution:**
```bash
cd insurance_ai
mkdir -p vector_db
mkdir -p media
mkdir -p chroma_db
```

---

## Project Structure

```
policypilot/
├── insurance_ai/              # Django Backend
│   ├── core/
│   │   ├── ml/
│   │   │   ├── train.py       # Train claim prediction model
│   │   │   ├── predictor.py   # Load and use model
│   │   │   └── models/
│   │   ├── services/
│   │   │   ├── rag.py         # PDF processing
│   │   │   ├── coverage.py    # Coverage analysis
│   │   │   ├── scoring.py     # Policy scoring
│   │   │   ├── simulator.py   # Scenario simulation
│   │   │   ├── claim_llm.py   # Claim explanation
│   │   │   └── utils.py       # Utility functions
│   │   ├── static/
│   │   │   ├── main.js        # Main frontend logic
│   │   │   ├── dashboard.js   # UI helpers
│   │   │   └── css/
│   │   ├── templates/
│   │   │   └── index.html     # Main page
│   │   ├── views.py           # API endpoints
│   │   ├── urls.py            # URL routing
│   │   └── models.py          # Database models
│   ├── insurance_ai/          # Django project settings
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── manage.py              # Django CLI
│   ├── requirements.txt       # Python dependencies
│   ├── db.sqlite3            # SQLite database
│   ├── media/                # Uploaded PDF files
│   ├── vector_db/            # ChromaDB vector databases
│   └── .env                  # Environment variables (create this)
│
├── frontend/                  # React Frontend
│   ├── src/
│   │   ├── App.js
│   │   ├── App.css
│   │   └── index.js
│   ├── public/
│   │   └── index.html
│   ├── package.json
│   ├── .env                  # Environment variables (optional)
│   └── node_modules/
│
├── sample pdf/               # Sample policy files for testing
│   ├── h1.pdf
│   ├── h2.pdf
│   ├── h3.pdf
│   └── life_ins_1.pdf
│
├── README.md                 # Original project README
└── SETUP_GUIDE.md           # This file
```

---

## Useful Commands Reference

### Backend (Django)

```bash
# Activate virtual environment
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate      # Windows

# Install/update dependencies
pip install -r requirements.txt

# Run server
python manage.py runserver

# Run on different port
python manage.py runserver 8001

# Run tests
python manage.py test

# Make migrations (if models changed)
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Check project
python manage.py check

# Train ML model
python core/ml/train.py

# Test policy ID generation
python test_policy_id.py

# Test upload process
python test_upload.py
```

### Frontend (React)

```bash
# Navigate to frontend
cd frontend

# Install dependencies
npm install

# Start development server
npm start

# Build for production
npm run build

# Run tests
npm test

# Check for issues
npm run lint
```

### General

```bash
# Check Python version
python --version

# Check Node.js version
node --version
npm --version

# List installed packages
pip list

# Create directory
mkdir -p vector_db media chroma_db

# Check disk space
df -h

# List files with details
ls -la

# Count files
ls | wc -l
```

---

## Next Steps After Setup

1. ✅ **Upload Sample Policies**
   - Use files in `sample pdf/` directory
   - Or upload your own insurance policies

2. ✅ **Explore Features**
   - Test each feature with uploaded policies
   - Check server logs to understand flow

3. ✅ **Customize**
   - Update UI styling in `static/css/`
   - Modify prompts in service files
   - Add new features as needed

4. ✅ **Deploy**
   - Set `DEBUG=False` in `.env`
   - Configure production database
   - Set up proper web server (Gunicorn, Nginx)

5. ✅ **Monitor**
   - Check logs regularly
   - Monitor API usage
   - Clean up old uploads periodically

---

## Getting Help

### Documentation Files
- `README.md` - Original project documentation
- `CODE_CHANGES.md` - Code modifications details
- `TROUBLESHOOTING.md` - Common issues and solutions
- `POLICY_ID_FIX.md` - Policy ID generation fix

### Common Resources
- Django Docs: https://docs.djangoproject.com/
- React Docs: https://react.dev/
- LangChain Docs: https://python.langchain.com/
- Groq Docs: https://console.groq.com/docs

### Test Files
- `test_policy_id.py` - Test policy ID generation
- `test_upload.py` - Test PDF upload and processing

---

## System Architecture Overview

```
User Browser (Frontend)
     │
     ├─→ http://localhost:3000 (React)
     │        │
     │        ├─→ Upload PDF
     │        ├─→ Ask Questions
     │        ├─→ Get Coverage
     │        ├─→ Simulate Scenarios
     │        └─→ Compare Policies
     │
     └─→ http://127.0.0.1:8000 (Django API)
              │
              ├─→ PDF Processing (LangChain + ChromaDB)
              ├─→ Vector Storage (ChromaDB)
              ├─→ LLM Queries (Groq/LLaMA)
              ├─→ ML Prediction (Scikit-learn)
              └─→ Database (SQLite)
```

---

## Quick Start Checklist

- [ ] Python 3.9+ installed
- [ ] Node.js 14+ installed
- [ ] Repository cloned
- [ ] Virtual environment created and activated
- [ ] Dependencies installed (pip install -r requirements.txt)
- [ ] Frontend dependencies installed (npm install)
- [ ] .env file created with Groq API key
- [ ] Directories created (media, vector_db, chroma_db)
- [ ] Migrations applied (python manage.py migrate)
- [ ] ML model trained (python core/ml/train.py)
- [ ] Django server running (python manage.py runserver)
- [ ] React server running (npm start)
- [ ] Frontend accessible at http://localhost:3000
- [ ] Backend accessible at http://127.0.0.1:8000

---

## Support & Issues

If you encounter issues:

1. **Check Troubleshooting section** above
2. **Review server logs** for error messages
3. **Run test scripts** to diagnose issues
4. **Check documentation files** for detailed explanations
5. **Verify all prerequisites** are installed correctly

---

**Last Updated:** April 13, 2026
**Version:** 1.0
**Status:** Production Ready ✅
