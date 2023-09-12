from models import Base
from models import Hamburgueria
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey,Integer
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT, BOOLEAN, DECIMAL,VARCHAR


class FuncaoFuncionario(Base):
    __tablename__ = "funcao_funcionario"
    id: Mapped[int] = mapped_column(
        Integer(), primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(VARCHAR(100), nullable=False)
    descricao: Mapped[str] = mapped_column(VARCHAR(256))

    # funcionarios: Mapped[relationship] = mapped_column(
    #     relationship('Funcionario'))
