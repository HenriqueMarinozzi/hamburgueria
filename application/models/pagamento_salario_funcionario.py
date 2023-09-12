from models import Base
from models import Hamburgueria
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Integer
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT, BOOLEAN, DECIMAL, DATETIME, VARCHAR


class PagamentoSalarioFuncionario(Base):
    __tablename__ = "pagamento_salario_funcionario"
    id: Mapped[int] = mapped_column(
        Integer(), primary_key=True, autoincrement=True)
    id_funcionario: Mapped[int] = mapped_column(
        Integer, ForeignKey('funcionario.id'), nullable=False)
    data_pagamento: Mapped[DATETIME] = mapped_column(DATETIME, nullable=False)
    valor: Mapped[float] = mapped_column(DECIMAL(10, 2), nullable=False)
    forma_pagamento_salario: Mapped[str] = mapped_column(VARCHAR(100), nullable=False)

    # funcionario: Mapped[relationship] = mapped_column(relationship('Funcionario'))
