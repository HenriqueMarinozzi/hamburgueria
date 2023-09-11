from models import Base
from models import Hamburgueria
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT, TINYINT, BOOLEAN, DECIMAL, SmallInteger

class EstoqueProduto(Base):
    __tablename__ = "estoque_produto"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    id_produto: Mapped[int] = mapped_column(Integer, ForeignKey('produto.id'), nullable=False)
    quantidade_disponivel: Mapped[int] = mapped_column(Integer, nullable=False)
    
    produto: Mapped[relationship] = mapped_column(relationship('Produto'))