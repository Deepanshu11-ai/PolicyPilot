from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.routes import auth, upload, documents

app = FastAPI(
    title="AI Insurance Backend",
    version="1.0.0"
)

# ---------------- CORS (IMPORTANT for frontend) ----------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later restrict this
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- HEALTH CHECK ----------------
@app.get("/")
def root():
    return {"message": "Backend running successfully 🚀"}

@app.get("/health")
def health():
    return {"status": "ok"}

# ---------------- ROUTES ----------------
app.include_router(upload.router, prefix="", tags=["Upload"])
app.include_router(documents.router, prefix="", tags=["Documents"])
from routes import auth, upload, documents

app.include_router(auth.router)
app.include_router(upload.router)
app.include_router(documents.router)