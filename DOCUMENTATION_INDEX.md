# 📚 PolicyPilot Documentation - Setup & Installation

Complete documentation suite for setting up PolicyPilot on a new machine.

---

## 📖 Documentation Files Overview

### For New Users (Start Here!)

| File | Purpose | Read Time |
|------|---------|-----------|
| **[QUICK_START.md](QUICK_START.md)** | Get running in 15 minutes | 5 min |
| **[SETUP_GUIDE.md](SETUP_GUIDE.md)** | Comprehensive setup guide | 30 min |
| **[WINDOWS_SETUP.md](WINDOWS_SETUP.md)** | Windows-specific instructions | 20 min |

### Configuration & Environment

| File | Purpose | Read Time |
|------|---------|-----------|
| **[ENV_CONFIGURATION.md](ENV_CONFIGURATION.md)** | Environment variables setup | 15 min |
| **[.env.example](insurance_ai/.env.example)** | Environment template | 2 min |

### Issue & Feature Documentation

| File | Purpose | Read Time |
|------|---------|-----------|
| **[README_FIX.md](README_FIX.md)** | Upload issue fixes | 5 min |
| **[POLICY_ID_FIX.md](POLICY_ID_FIX.md)** | Policy ID generation fix | 5 min |
| **[TROUBLESHOOTING.md](TROUBLESHOOTING.md)** | Common issues & solutions | 20 min |

---

## 🚀 Quick Navigation

### "I just want to run the app"
→ Read: **[QUICK_START.md](QUICK_START.md)** (5 min)

### "I'm on Windows"
→ Read: **[WINDOWS_SETUP.md](WINDOWS_SETUP.md)** (20 min)

### "I need detailed instructions"
→ Read: **[SETUP_GUIDE.md](SETUP_GUIDE.md)** (30 min)

### "I'm stuck on something"
→ Read: **[TROUBLESHOOTING.md](TROUBLESHOOTING.md)** (20 min)

### "I need to set up API keys"
→ Read: **[ENV_CONFIGURATION.md](ENV_CONFIGURATION.md)** (15 min)

### "I want to understand what was fixed"
→ Read: **[README_FIX.md](README_FIX.md)** + **[POLICY_ID_FIX.md](POLICY_ID_FIX.md)** (10 min)

---

## 📋 Setup Checklist

- [ ] **Python 3.9+** installed and verified
- [ ] **Node.js 14+** installed and verified
- [ ] **Repository cloned** to your machine
- [ ] **Backend dependencies** installed (`pip install -r requirements.txt`)
- [ ] **Frontend dependencies** installed (`npm install`)
- [ ] **.env file** created with Groq API key
- [ ] **Directories** created (media, vector_db, chroma_db)
- [ ] **Database** migrated (`python manage.py migrate`)
- [ ] **ML model** trained (`python core/ml/train.py`)
- [ ] **Django server** running (`python manage.py runserver`)
- [ ] **React server** running (`npm start`)
- [ ] **Frontend accessible** at http://localhost:3000
- [ ] **Backend accessible** at http://127.0.0.1:8000
- [ ] **Sample PDF uploaded** and tested

---

## 🎯 Choose Your Setup Path

### Path 1: Express Setup (15 minutes)
**For experienced developers who want to get running immediately**

1. Read: [QUICK_START.md](QUICK_START.md)
2. Execute the steps
3. Run the app
4. Done! 🎉

### Path 2: Comprehensive Setup (45 minutes)
**For those who want to understand everything**

1. Read: [SETUP_GUIDE.md](SETUP_GUIDE.md) completely
2. Verify all prerequisites
3. Follow step-by-step instructions
4. Test everything
5. Done! ✅

### Path 3: Windows Setup (45 minutes)
**For Windows users**

1. Read: [WINDOWS_SETUP.md](WINDOWS_SETUP.md) completely
2. Follow Windows-specific instructions
3. Use Windows commands provided
4. Test everything
5. Done! ✅

### Path 4: Detailed Learning (2+ hours)
**For those who want to learn deeply**

1. Read: [SETUP_GUIDE.md](SETUP_GUIDE.md)
2. Read: [ENV_CONFIGURATION.md](ENV_CONFIGURATION.md)
3. Read: [README_FIX.md](README_FIX.md)
4. Read: [POLICY_ID_FIX.md](POLICY_ID_FIX.md)
5. Read: [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
6. Bookmark documentation for reference
7. Done! 🎓

---

## 📁 File Structure Created

After setup, you should have:

```
policypilot/
├── insurance_ai/
│   ├── .venv/                          (Created)
│   ├── media/                          (Created)
│   ├── vector_db/                      (Created)
│   ├── chroma_db/                      (Created)
│   ├── .env                            (Create manually)
│   ├── db.sqlite3                      (Created by migrate)
│   ├── core/
│   ├── insurance_ai/
│   ├── manage.py
│   └── requirements.txt
│
├── frontend/
│   ├── node_modules/                   (Created)
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── .env                            (Optional)
│
├── sample pdf/
│   ├── h1.pdf
│   ├── h2.pdf
│   ├── h3.pdf
│   └── life_ins_1.pdf
│
├── Documentation Files (NEW)
│   ├── QUICK_START.md
│   ├── SETUP_GUIDE.md
│   ├── WINDOWS_SETUP.md
│   ├── ENV_CONFIGURATION.md
│   ├── README_FIX.md
│   ├── POLICY_ID_FIX.md
│   ├── TROUBLESHOOTING.md
│   ├── CODE_CHANGES.md
│   └── DOCUMENTATION_INDEX.md (this file)
│
└── README.md (Original)
```

---

## ⚡ Commands Reference

### Quick Copy-Paste Commands

#### macOS/Linux Backend Setup
```bash
cd policypilot/insurance_ai
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdir -p media vector_db chroma_db
python manage.py migrate
python core/ml/train.py
```

#### Windows Backend Setup
```cmd
cd policypilot\insurance_ai
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
mkdir media vector_db chroma_db
python manage.py migrate
python core/ml/train.py
```

#### Frontend Setup (All OS)
```bash
cd policypilot/frontend
npm install
```

#### Start Servers

**Terminal 1 - Backend:**
```bash
cd insurance_ai
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python manage.py runserver
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm start
```

---

## 🔑 Key Information

### Groq API Key
- **Where to get:** https://console.groq.com/
- **How to use:** Add to `.env` file as `GROQ_API_KEY=gsk_xxx`
- **Format:** Should start with `gsk_`

### Access Points
- **Frontend:** http://localhost:3000
- **Backend API:** http://127.0.0.1:8000/api/
- **Admin Panel:** http://127.0.0.1:8000/admin

### Virtual Environment
- **Purpose:** Isolates Python packages for this project
- **Activation (macOS/Linux):** `source .venv/bin/activate`
- **Activation (Windows):** `.venv\Scripts\activate`
- **Deactivation:** `deactivate`

---

## ✅ Testing Your Setup

### 1. Backend Test
```bash
cd insurance_ai
python manage.py runserver
```
Should show: `Starting development server at http://127.0.0.1:8000/`

### 2. Frontend Test
```bash
cd frontend
npm start
```
Should show: `Compiled successfully!` and open http://localhost:3000

### 3. Upload Test
1. On http://localhost:3000
2. Upload a PDF from `sample pdf/` folder
3. Should create new policy directory in `vector_db/`

### 4. API Test
```bash
curl "http://127.0.0.1:8000/api/"
```
Should return API endpoints

---

## 🐛 Common Issues

### "Module not found"
→ See: [TROUBLESHOOTING.md - Module not found](TROUBLESHOOTING.md#issue-module-not-found)

### "Groq API key not found"
→ See: [ENV_CONFIGURATION.md - Troubleshooting](ENV_CONFIGURATION.md#troubleshooting)

### "Port already in use"
→ See: [SETUP_GUIDE.md - Port already in use](SETUP_GUIDE.md#issue-port-8000-already-in-use)

### "Python/Node not found"
→ See: [TROUBLESHOOTING.md](TROUBLESHOOTING.md) at the beginning

For complete troubleshooting, check:
- **[TROUBLESHOOTING.md](TROUBLESHOOTING.md)** - Common issues
- **[WINDOWS_SETUP.md Troubleshooting](WINDOWS_SETUP.md#troubleshooting-for-windows)** - Windows-specific
- **[SETUP_GUIDE.md Troubleshooting](SETUP_GUIDE.md#troubleshooting)** - Comprehensive

---

## 📞 Getting Help

### Step-by-Step Help
1. Check [TROUBLESHOOTING.md](TROUBLESHOOTING.md) first
2. Search for your error message in the documentation
3. Follow the solution provided
4. If still stuck, check relevant setup guide

### Documentation by Topic

| Topic | File |
|-------|------|
| Installation | [SETUP_GUIDE.md](SETUP_GUIDE.md) |
| Windows Setup | [WINDOWS_SETUP.md](WINDOWS_SETUP.md) |
| Quick Start | [QUICK_START.md](QUICK_START.md) |
| Environment Variables | [ENV_CONFIGURATION.md](ENV_CONFIGURATION.md) |
| Errors & Issues | [TROUBLESHOOTING.md](TROUBLESHOOTING.md) |
| Code Fixes | [README_FIX.md](README_FIX.md), [POLICY_ID_FIX.md](POLICY_ID_FIX.md) |

---

## 📊 Setup Time Estimates

| Method | Time | Skill Level |
|--------|------|-------------|
| **Quick Start** | 15 min | All |
| **Comprehensive** | 45 min | Intermediate |
| **Windows Setup** | 45 min | All |
| **Learning Deep-Dive** | 2+ hours | Advanced |

---

## 🎓 Learning Resources

### Official Documentation
- Django: https://docs.djangoproject.com/
- React: https://react.dev/
- LangChain: https://python.langchain.com/
- Groq: https://console.groq.com/docs

### Video Tutorials (YouTube)
- "How to install Python [Your OS]"
- "How to install Node.js [Your OS]"
- "Django REST Framework tutorial"
- "React.js tutorial for beginners"

### Practice
- Upload sample PDFs
- Try each feature
- Read code comments
- Check server logs

---

## ✨ What's New

These are new setup documentation files created for easier onboarding:

✅ [QUICK_START.md](QUICK_START.md) - 15-minute setup  
✅ [SETUP_GUIDE.md](SETUP_GUIDE.md) - Comprehensive guide  
✅ [WINDOWS_SETUP.md](WINDOWS_SETUP.md) - Windows-specific  
✅ [ENV_CONFIGURATION.md](ENV_CONFIGURATION.md) - Environment setup  
✅ [DOCUMENTATION_INDEX.md](DOCUMENTATION_INDEX.md) - This file  

Plus previous documentation:
✅ [README_FIX.md](README_FIX.md) - Issue explanation  
✅ [POLICY_ID_FIX.md](POLICY_ID_FIX.md) - Fix explanation  
✅ [TROUBLESHOOTING.md](TROUBLESHOOTING.md) - Solutions  

---

## 🎯 Next Steps

1. **Choose your path** from the options above
2. **Read** the relevant documentation
3. **Follow** the setup steps carefully
4. **Test** each component as you go
5. **Use** the troubleshooting guide if needed
6. **Enjoy** using PolicyPilot! 🎉

---

## 📋 Verification Checklist (After Setup)

Run these commands to verify everything works:

```bash
# Backend verification
cd insurance_ai
source .venv/bin/activate
python manage.py check
python manage.py migrate --check

# Frontend verification
cd ../frontend
npm list react
npm list react-dom

# API endpoint check
curl http://127.0.0.1:8000/api/

# Database check
ls db.sqlite3

# Vector DB check
ls vector_db/
```

All should succeed without errors ✅

---

**Last Updated:** April 13, 2026  
**Version:** 1.0  
**Status:** Complete Setup Documentation Package ✅

**Total Documentation:** 8+ guides covering all aspects of setup and configuration
