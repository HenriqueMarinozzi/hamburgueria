from models import Base
from models import Hamburgueria
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Integer
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT, BOOLEAN, DECIMAL

class PedidoTemProduto(Base):
    __tablename__ = "pedido_tem_produto"
    id_pedido: Mapped[int] = mapped_column(Integer(), primary_key=True)
    id_produto: Mapped[int] = mapped_column(Integer(), primary_key=True)
    quantidade: Mapped[int] = mapped_column(Integer(), nullable=False)
    valor: Mapped[float] = mapped_column(DECIMAL(8, 2), nullable=False)
    
    # produto: Mapped[relationship] = mapped_column(relationship('Produto'))
    # pedido: Mapped[relationship] = mapped_column(relationship('Pedido'))