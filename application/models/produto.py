from models import Base
from models import Hamburgueria
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey,Integer
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT, TINYINT, BOOLEAN, DECIMAL, VARCHAR

class Produto(Base):
    __tablename__ = "produto"
    id: Mapped[int] = mapped_column("id",Integer(), primary_key=True, autoincrement=True)
    quantidade: Mapped[int] = mapped_column(TINYINT, nullable=False)
    valor: Mapped[float] = mapped_column(DECIMAL(10, 2), nullable=False)
    descricao: Mapped[str] = mapped_column("descricao",VARCHAR(512), nullable=False)
    tempo_prepare: Mapped[int] = mapped_column(Integer(), nullable=False)
    

    # produtos: Mapped[relationship] = mapped_column(relationship('PedidoTemProduto', back_populates='pedido'))
    # clientes: Mapped[relationship] = mapped_column(relationship('ClientePedido', back_populates='pedido'))