from sqlalchemy.orm import Session
from app.models.document import Document

class DocumentRepository:
    @staticmethod
    def create_document(db: Session, filename: str, file_path: str):
        db_doc = Document(filename=filename, file_path=file_path)
        db.add(db_doc)
        db.commit()
        db.refresh(db_doc)
        return db_doc

    @staticmethod
    def get_all(db: Session):
        return db.query(Document).all()