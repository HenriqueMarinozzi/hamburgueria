from models import Base
from models import Hamburgueria
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Integer
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT, BOOLEAN, DECIMAL, DATETIME

class Pagamento(Base):
    __tablename__ = "pagamento"
    id: Mapped[int] = mapped_column("id",Integer(), primary_key=True, autoincrement=True)
    data_pagamento: Mapped[DATETIME] = mapped_column("data_pagamento",DATETIME, nullable=False)
    valor: Mapped[float] = mapped_column("valor",DECIMAL(8, 2), nullable=False)
    
    # formas_pagamento: Mapped[relationship] = mapped_column(relationship('FormaPagamento'))
    