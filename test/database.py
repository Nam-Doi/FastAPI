from fastapi.testclient import TestClient # http client gia lap gui request truc tiep vao FastAPI app trong cung 1 precess
from app.main import app
from app import schemas
import pytest
from app.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from app.database import get_db
from app.database import Base
from urllib.parse import quote_plus

password = quote_plus(settings.DATABASE_PASSWORD)

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.DATABASE_USERNAME}:{password}@{settings.DATABASE_HOSTNAME}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

# def override_get_db():
#     db = TestingSessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
    
# app.dependency_overrides[get_db] = override_get_db




# client = TestClient(app)

@pytest.fixture()
def session():
    print("my sesstion fixture run")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
    

"""
trường hợp này ta có thể dùng yield để có thể xác đinh những gì cần làm trước yield
và những gì làm sau khi yield chạy xong
ở đây ta khởi tạo bảng trước
sau đó xóa đi khi đã làm xong
"""
@pytest.fixture()
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    
