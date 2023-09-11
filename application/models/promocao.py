from models import Base
from models import Hamburgueria
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT, TINYINT, BOOLEAN, DECIMAL, SmallInteger

class Promocao(Base):
    __tablename__ = "promocao"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    desconto: Mapped[float] = mapped_column(DECIMAL(5, 2), nullable=False)
    data_inicio: Mapped[Date] = mapped_column(Date, nullable=False)
    data_fim: Mapped[Date] = mapped_column(Date, nullable=False)