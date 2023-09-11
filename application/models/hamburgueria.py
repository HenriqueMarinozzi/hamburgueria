from typing import List
from models import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import Integer, VARCHAR

class Hamburgueria(Base):
    __tablename__ = "hamburgueria"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    endereco: Mapped[str] = mapped_column(String(256), nullable=False)
    telefone: Mapped[str] = mapped_column(String(20))
    email: Mapped[str] = mapped_column(String(100))
    
