from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import List

app = FastAPI()

# SQLAlchemy setup
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:mysecretpassword@localhost/test_bse"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# User table model
class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    deal_date = Column(String(100))
    security_code = Column(String(100))
    security_name = Column(String(100))
    client_name = Column(String(100))
    deal_type = Column(String(100))
    quantity = Column(Integer)
    price = Column(Integer)

# API endpoints
@app.get("/users", response_model=List[User])
def get_users():
    db = SessionLocal()
    users = db.query(User).all()
    db.close()
    return users

@app.post("/users", response_model=User)
def create_user(user: User):
    db = SessionLocal()
    db.add(user)
    db.commit()
    db.refresh(user)
    db.close()
    return user

@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user: User):
    db = SessionLocal()
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    for field, value in user.__dict__.items():
        if field != "_sa_instance_state" and value is not None:
            setattr(db_user, field, value)
    db.commit()
    db.refresh(db_user)
    db.close()
    return db_user
