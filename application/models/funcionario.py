from models import Base
from models import Hamburgueria
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT, TINYINT, BOOLEAN, DECIMAL, SmallInteger

class Funcionario(Base):
    __tablename__ = "funcionario"
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    salario = Column(Decimal(10, 2), nullable=False)
    carga_horaria = Column(Integer, nullable=False)
    nome = Column(String(100), nullable=False)
    cpf = Column(CHAR(11), nullable=False)
    rg = Column(String(11), nullable=False)
    id_funcao = Column(Integer, ForeignKey('funcao_funcionario.id'))
    
    funcao = relationship("FuncaoFuncionario", back_populates="funcionarios")