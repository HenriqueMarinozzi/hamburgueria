from models import Base
from models import Hamburgueria
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT, TINYINT, BOOLEAN, DECIMAL, VARCHAR, DATE


class Cliente(Base):
    __tablename__ = "cliente"
    id: Mapped[int] = mapped_column(
        "id", INTEGER, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column("nome", VARCHAR(100), nullable=False)
    cpf: Mapped[str] = mapped_column(
        "cpf", VARCHAR(11), nullable=False, unique=True)
    rg: Mapped[str] = mapped_column("rg", VARCHAR(11), nullable=False)
    data_nascimento: Mapped[DATE] = mapped_column(
        "data_nascimento", DATE, nullable=False)
    email: Mapped[str] = mapped_column("email", VARCHAR(100))
    telefone: Mapped[str] = mapped_column("telefone", VARCHAR(20))
    endereco: Mapped[str] = mapped_column("endereco", VARCHAR(256))
