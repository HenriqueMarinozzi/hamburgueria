from models import Base
from models import Hamburgueria
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT, TINYINT, BOOLEAN, DECIMAL, SmallInteger

class HistoricoPedido(Base):
    __tablename__ = "historico_pedido"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    id_pedido: Mapped[int] = mapped_column(Integer, ForeignKey('pedido.id'), nullable=False)
    id_cliente: Mapped[int] = mapped_column(Integer, ForeignKey('cliente.id'), nullable=False)
    data_pedido: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    valor_total: Mapped[float] = mapped_column(DECIMAL(10, 2), nullable=False)
    
    pedido: Mapped[relationship] = mapped_column(relationship('Pedido'))
    cliente: Mapped[relationship] = mapped_column(relationship('Cliente'))