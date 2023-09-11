from models import Base
from models import Hamburgueria
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT, TINYINT, BOOLEAN, DECIMAL, SmallInteger

class ClientePedido(Base):
    __tablename__ = "cliente_pedido"
    id_pedido: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_cliente: Mapped[int] = mapped_column(Integer, primary_key=True)
    data_pedido: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    
    cliente: Mapped[relationship] = mapped_column(relationship('Cliente'))
    pedido: Mapped[relationship] = mapped_column(relationship('Pedido'))