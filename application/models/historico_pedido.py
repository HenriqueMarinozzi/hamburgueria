from models import Base
from models import Hamburgueria
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Integer
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT, BOOLEAN, DECIMAL, DATETIME

class HistoricoPedido(Base):
    __tablename__ = "historico_pedido"
    id: Mapped[int] = mapped_column(Integer(), primary_key=True, autoincrement=True)
    id_pedido: Mapped[int] = mapped_column(INTEGER, ForeignKey('pedido.id'), nullable=False)
    id_cliente: Mapped[int] = mapped_column(INTEGER, ForeignKey('cliente.id'), nullable=False)
    data_pedido: Mapped[DATETIME] = mapped_column(DATETIME, nullable=False)
    valor_total: Mapped[float] = mapped_column(DECIMAL(10, 2), nullable=False)
    
    # pedido: Mapped[relationship] = mapped_column(relationship('Pedido'))
    # cliente: Mapped[relationship] = mapped_column(relationship('Cliente'))