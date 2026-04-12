from fastapi import APIRouter, UploadFile, File, Depends
from services.supabase_client import supabase
from utils.auth import get_current_user

router = APIRouter()

@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    user_id: str = Depends(get_current_user)
):
    file_bytes = await file.read()
    file_path = f"{user_id}/{file.filename}"

    # Upload to Supabase Storage
    supabase.storage.from_("policies").upload(
        path=file_path,
        file=file_bytes,
        file_options={"content-type": file.content_type}
    )

    file_url = supabase.storage.from_("policies").get_public_url(file_path)

    # Save metadata
    supabase.table("documents").insert({
        "user_id": user_id,
        "file_name": file.filename,
        "file_url": file_url
    }).execute()

    return {"message": "Uploaded successfully"}