from typing import List
from models import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import INTEGER, VARCHAR


class Hamburgueria(Base):
    __tablename__ = "hamburgueria"
    id: Mapped[int] = mapped_column(INTEGER, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(VARCHAR(100), nullable=False)
    endereco: Mapped[str] = mapped_column(VARCHAR(256), nullable=False)
    telefone: Mapped[str] = mapped_column(VARCHAR(20))
    email: Mapped[str] = mapped_column(VARCHAR(100))
