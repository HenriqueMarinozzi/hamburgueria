from models import Base
from models import Hamburgueria
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT, TINYINT, BOOLEAN, DECIMAL, SmallInteger

class FormaPagamento(Base):
    __tablename__ = "forma_pagamento"
    id_pagamento: Mapped[int] = mapped_column(Integer, ForeignKey('pagamento.id'), primary_key=True)
    id_forma_pagamento: Mapped[int] = mapped_column(Integer, primary_key=True)
    
    pagamento: Mapped[relationship] = mapped_column(relationship('Pagamento'))