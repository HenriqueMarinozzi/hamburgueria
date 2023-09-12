from models import Base
from models import Hamburgueria
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Integer
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT, BOOLEAN, DECIMAL,VARCHAR

class CategoriaProduto(Base):
    __tablename__ = "categoria_produto"
    id: Mapped[int] = mapped_column(Integer(), primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)
    descricao: Mapped[str] = mapped_column(VARCHAR(200), nullable=False)

