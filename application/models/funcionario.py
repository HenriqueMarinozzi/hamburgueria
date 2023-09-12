from models import Base
from models import Hamburgueria
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import Integer, VARCHAR, DECIMAL, INTEGER, CHAR, ForeignKey

class Funcionario(Base):
    __tablename__ = "funcionario"
    id: Mapped[int] = mapped_column("id", Integer(), primary_key=True, unique=True, autoincrement=True)
    salario: Mapped[str] = mapped_column("salario",DECIMAL(10, 2), nullable=False)
    carga_horaria:Mapped[int] = mapped_column("carga_horaria",INTEGER, nullable=False)
    nome:Mapped[str] = mapped_column("nome",VARCHAR(100), nullable=False)
    cpf: Mapped[str] =mapped_column("cpf",CHAR(11), nullable=False)
    rg: Mapped[str] =mapped_column("rg",VARCHAR(11), nullable=False)
    id_funcao: Mapped[int] = mapped_column("id_funcao",INTEGER, ForeignKey('funcao_funcionario.id'))
    funcao: Mapped[relationship("FuncaoFuncionario", back_populates="funcionarios")]
