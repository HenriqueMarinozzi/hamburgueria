from models import Base
from models import Hamburgueria
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT, TINYINT, BOOLEAN, DECIMAL, SmallInteger

class Cliente(Base):
    __tablename__ = "cliente"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    cpf: Mapped[str] = mapped_column(String(11), nullable=False, unique=True)
    rg: Mapped[str] = mapped_column(String(11), nullable=False)
    data_nascimento: Mapped[Date] = mapped_column(Date, nullable=False)
    email: Mapped[str] = mapped_column(String(100))
    telefone: Mapped[str] = mapped_column(String(20))
    endereco: Mapped[str] = mapped_column(String(256))