from models import Base
from models import Hamburgueria
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT, TINYINT, BOOLEAN, DECIMAL, SmallInteger

class Pagamento(Base):
    __tablename__ = "pagamento"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    data_pagamento: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    valor: Mapped[float] = mapped_column(DECIMAL(8, 2), nullable=False)
    
    formas_pagamento: Mapped[relationship] = mapped_column(relationship('FormaPagamento'))
    