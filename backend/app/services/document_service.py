import os
from fastapi import UploadFile
from sqlalchemy.orm import Session
from app.repositories.document_repo import DocumentRepository

UPLOAD_DIR = "uploads"

class DocumentService:
    @staticmethod
    async def save_upload(db: Session, file: UploadFile):
        if not os.path.exists(UPLOAD_DIR):
            os.makedirs(UPLOAD_DIR)
            
        file_location = f"{UPLOAD_DIR}/{file.filename}"
        with open(file_location, "wb") as f:
            f.write(await file.read())

        return DocumentRepository.create_document(db, file.filename, file_location)