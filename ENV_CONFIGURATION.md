# PolicyPilot - Environment Configuration Guide

Complete guide for setting up environment variables and configuration files.

---

## Overview

PolicyPilot uses environment variables to configure sensitive information and settings. These should **never** be committed to version control.

---

## File Structure

```
policypilot/
├── insurance_ai/
│   ├── .env                    ← Create this (NEVER commit)
│   ├── .env.example            ← Reference template
│   ├── requirements.txt        ← Package dependencies
│   ├── manage.py
│   └── ...
├── frontend/
│   ├── .env                    ← Optional
│   ├── .env.example            ← Reference template
│   ├── package.json
│   └── ...
└── .gitignore                  ← Should exclude .env files
```

---

## Backend Environment (.env)

### Location
Create this file at: `insurance_ai/.env`

### Required Variables

#### Groq API Key (REQUIRED)
```env
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

**How to get it:**
1. Visit https://console.groq.com/
2. Sign up or log in
3. Navigate to API Keys section
4. Create new API key
5. Copy the full key (starts with `gsk_`)
6. Paste into `.env`

#### Django Settings (REQUIRED)
```env
DJANGO_SECRET_KEY=dev-secret-key-change-in-production
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

**IMPORTANT:** For production, set:
- `DEBUG=False`
- Generate new SECRET_KEY
- Set `ALLOWED_HOSTS` to your domain

### Optional Variables

#### Database Configuration
```env
# Default: SQLite (db.sqlite3)
# To use PostgreSQL:
DATABASE_ENGINE=django.db.backends.postgresql
DATABASE_NAME=policypilot_db
DATABASE_USER=postgres
DATABASE_PASSWORD=your_password
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

#### Logging
```env
LOG_LEVEL=INFO
LOG_FILE=policypilot.log
```

#### Model Configuration
```env
# HuggingFace model for embeddings
EMBEDDING_MODEL=all-MiniLM-L6-v2

# Groq LLM model
LLM_MODEL=llama-3.3-70b-versatile

# Embedding parameters
CHUNK_SIZE=500
CHUNK_OVERLAP=100
```

#### Cache Configuration
```env
# ChromaDB path (default: vector_db)
CHROMA_DB_PATH=vector_db

# Number of embeddings to cache
EMBEDDINGS_CACHE_SIZE=1000
```

### Complete Example (.env)

```env
# ================== API KEYS ==================
GROQ_API_KEY=gsk_your_actual_api_key_here

# ================== DJANGO SETTINGS ==================
DJANGO_SECRET_KEY=dev-super-secret-key-change-in-production
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,127.0.0.1:8000

# ================== DATABASE ==================
# Using SQLite (default)
# DATABASE_ENGINE=django.db.backends.sqlite3
# DATABASE_NAME=db.sqlite3

# For PostgreSQL (uncomment to use)
# DATABASE_ENGINE=django.db.backends.postgresql
# DATABASE_NAME=policypilot
# DATABASE_USER=postgres
# DATABASE_PASSWORD=secure_password
# DATABASE_HOST=localhost
# DATABASE_PORT=5432

# ================== MODELS & AI ==================
EMBEDDING_MODEL=all-MiniLM-L6-v2
LLM_MODEL=llama-3.3-70b-versatile
CHUNK_SIZE=500
CHUNK_OVERLAP=100

# ================== STORAGE ==================
CHROMA_DB_PATH=vector_db
MEDIA_ROOT=media
MEDIA_URL=/media/

# ================== LOGGING ==================
LOG_LEVEL=INFO
LOG_FILE=policypilot.log

# ================== SECURITY (PRODUCTION ONLY) ==================
# Set these to True for production
# SECURE_SSL_REDIRECT=False
# SESSION_COOKIE_SECURE=False
# CSRF_COOKIE_SECURE=False
```

---

## Frontend Environment (.env)

### Location
Create this file at: `frontend/.env`

### Variables

```env
# Backend API URL
REACT_APP_API_URL=http://127.0.0.1:8000

# App name
REACT_APP_NAME=PolicyPilot

# Environment
REACT_APP_ENV=development

# Enable debug mode
REACT_APP_DEBUG=true
```

### Complete Example

```env
# Backend configuration
REACT_APP_API_URL=http://127.0.0.1:8000
REACT_APP_API_TIMEOUT=30000

# App information
REACT_APP_NAME=PolicyPilot
REACT_APP_VERSION=1.0.0

# Environment
REACT_APP_ENV=development
REACT_APP_DEBUG=true

# Feature flags
REACT_APP_ENABLE_POLICY_COMPARISON=true
REACT_APP_ENABLE_CLAIM_PREDICTION=true
REACT_APP_ENABLE_HIDDEN_CLAUSES=true
```

---

## Environment-Specific Configurations

### Development

**`insurance_ai/.env`:**
```env
GROQ_API_KEY=gsk_your_dev_key
DJANGO_SECRET_KEY=dev-secret
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
LOG_LEVEL=DEBUG
```

**`frontend/.env`:**
```env
REACT_APP_API_URL=http://127.0.0.1:8000
REACT_APP_ENV=development
REACT_APP_DEBUG=true
```

### Production

**`insurance_ai/.env`:**
```env
GROQ_API_KEY=gsk_your_prod_key
DJANGO_SECRET_KEY=generate_with_python_secrets
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
LOG_LEVEL=WARNING
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
```

**`frontend/.env`:**
```env
REACT_APP_API_URL=https://yourdomain.com/api
REACT_APP_ENV=production
REACT_APP_DEBUG=false
```

### Staging

**`insurance_ai/.env`:**
```env
GROQ_API_KEY=gsk_your_staging_key
DJANGO_SECRET_KEY=staging_secret_key
DEBUG=False
ALLOWED_HOSTS=staging.yourdomain.com
LOG_LEVEL=INFO
```

**`frontend/.env`:**
```env
REACT_APP_API_URL=https://staging.yourdomain.com/api
REACT_APP_ENV=staging
REACT_APP_DEBUG=false
```

---

## Security Best Practices

### 1. Never Commit .env Files
Add to `.gitignore`:
```
# Environment variables
.env
.env.local
.env.*.local
```

### 2. Use .env.example Template
Create `insurance_ai/.env.example`:
```env
# Copy this file to .env and fill in your values
GROQ_API_KEY=your_api_key_here
DJANGO_SECRET_KEY=your_secret_key_here
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1
```

Then commit `.env.example` but NOT `.env`

### 3. Protect Sensitive Values
- Never share API keys in messages or documents
- Use separate keys for dev/staging/production
- Rotate keys regularly
- Use password managers to store keys

### 4. Secure Key Generation
```bash
# Generate Django secret key
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

# Python secrets module
python -c 'import secrets; print(secrets.token_urlsafe(50))'
```

### 5. Environment Variable Validation
Add to `insurance_ai/settings.py`:
```python
import os
from pathlib import Path

# Check required environment variables
REQUIRED_ENV_VARS = ['GROQ_API_KEY', 'DJANGO_SECRET_KEY']

for var in REQUIRED_ENV_VARS:
    if not os.getenv(var):
        raise ValueError(f"Missing required environment variable: {var}")
```

---

## Loading Environment Variables

### Django (Backend)

Django automatically loads `.env` if you use `python-dotenv`:

```python
# In settings.py
from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY = os.getenv('GROQ_API_KEY')
DEBUG = os.getenv('DEBUG', 'False') == 'True'
```

### React (Frontend)

React automatically loads variables prefixed with `REACT_APP_`:

```javascript
// In your component
console.log(process.env.REACT_APP_API_URL);
// Output: http://127.0.0.1:8000
```

---

## Troubleshooting

### Issue: "Groq API key not found"

**Solution:**
1. Verify `.env` file exists in `insurance_ai/` folder
2. Check format: `GROQ_API_KEY=gsk_xxxx` (no quotes)
3. Restart Django server
4. Check file doesn't have BOM (use UTF-8 encoding)

### Issue: Environment variables not loading

**Solution (Django):**
```bash
# Add python-dotenv
pip install python-dotenv

# In your code
from dotenv import load_dotenv
load_dotenv()
```

**Solution (React):**
- Variables must start with `REACT_APP_`
- Restart npm server after changing `.env`
- Check for typos in variable names

### Issue: "DEBUG is still True in production"

**Solution:**
```python
# In settings.py, ensure proper conversion
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
```

### Issue: Variables not available in subprocess

**Solution:**
Pass environment variables explicitly:
```python
import subprocess
import os

env = os.environ.copy()
env['CUSTOM_VAR'] = 'value'
subprocess.run(['python', 'script.py'], env=env)
```

---

## Docker Environment Variables

If using Docker:

### Dockerfile
```dockerfile
# Use ARG for build-time variables
ARG GROQ_API_KEY
ENV GROQ_API_KEY=${GROQ_API_KEY}
```

### docker-compose.yml
```yaml
services:
  backend:
    environment:
      - GROQ_API_KEY=${GROQ_API_KEY}
      - DEBUG=False
      - ALLOWED_HOSTS=localhost
```

### Run with environment
```bash
docker run -e GROQ_API_KEY=gsk_xxxx my-app
# or
docker-compose --env-file .env up
```

---

## Environment Variables Reference

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| GROQ_API_KEY | Yes | - | Groq API key |
| DJANGO_SECRET_KEY | Yes | - | Django secret key |
| DEBUG | No | False | Django debug mode |
| ALLOWED_HOSTS | No | localhost | Allowed domains |
| DATABASE_ENGINE | No | sqlite3 | Database engine |
| CHROMA_DB_PATH | No | vector_db | Vector DB path |
| EMBEDDING_MODEL | No | all-MiniLM-L6-v2 | Embedding model |
| CHUNK_SIZE | No | 500 | Document chunk size |
| LOG_LEVEL | No | INFO | Logging level |

---

## Common Configuration Scenarios

### Local Development
```env
GROQ_API_KEY=gsk_dev_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
LOG_LEVEL=DEBUG
```

### Testing
```env
GROQ_API_KEY=gsk_test_key
DEBUG=True
DATABASE_NAME=test_db
LOG_LEVEL=DEBUG
```

### Production
```env
GROQ_API_KEY=gsk_prod_key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com
LOG_LEVEL=WARNING
```

---

## Next Steps

1. ✅ Create `insurance_ai/.env` with API key
2. ✅ (Optional) Create `frontend/.env`
3. ✅ Never commit `.env` files
4. ✅ Commit `.env.example` as template
5. ✅ Restart servers after changing `.env`
6. ✅ For production, update settings accordingly

---

**Last Updated:** April 13, 2026  
**Version:** 1.0  
**Status:** Complete ✅
