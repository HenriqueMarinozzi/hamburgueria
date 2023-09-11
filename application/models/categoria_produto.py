from models import Base
from models import Hamburgueria
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT, TINYINT, BOOLEAN, DECIMAL, SmallInteger

class CategoriaProduto(Base):
    __tablename__ = "categoria_produto"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    descricao: Mapped[str] = mapped_column(String(200), nullable=False)
    
    produtos: Mapped[relationship] = mapped_column(relationship('Produto'))