from models import Base
from models import Hamburgueria
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT, TINYINT, BOOLEAN, DECIMAL, SmallInteger

class Cardapio(Base):
    __tablename__ = "cardapio"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    id_produto: Mapped[int] = mapped_column(Integer, ForeignKey('produto.id'))
    
    produto: Mapped[relationship] = mapped_column(relationship('Produto', back_populates='cardapio'))