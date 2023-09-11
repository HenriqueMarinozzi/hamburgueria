from models import Base
from models import Hamburgueria
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT, TINYINT, BOOLEAN, DECIMAL, SmallInteger

class Fornecedor(Base):
    __tablename__ = "fornecedor"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    empresa: Mapped[str] = mapped_column(String(100), nullable=False)
    cnpj: Mapped[str] = mapped_column(CHAR(14), nullable=False)
    horario_entrega: Mapped[str] = mapped_column(String(100), nullable=False)
    produto_fornecido: Mapped[str] = mapped_column(String(100), nullable=False)
    endereco: Mapped[str] = mapped_column(String(256), nullable=False)
    telefone: Mapped[str] = mapped_column(String(20))
    email: Mapped[str] = mapped_column(String(100))
    
    produtos: Mapped[relationship] = mapped_column(relationship('Produto'))