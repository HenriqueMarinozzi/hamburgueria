from models import Base
from models import Hamburgueria
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey,Integer, DateTime
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT, BOOLEAN, DECIMAL,VARCHAR

class FeedbackCliente(Base):
    __tablename__ = "feedback_cliente"
    id: Mapped[int] = mapped_column(Integer(), primary_key=True, autoincrement=True)
    id_cliente: Mapped[int] = mapped_column(Integer(), ForeignKey('cliente.id'), nullable=False)
    avaliacao: Mapped[int] = mapped_column(Integer(), nullable=False)
    comentario: Mapped[str] = mapped_column(VARCHAR(512))
    data_feedback: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    
    # cliente: Mapped[relationship] = mapped_column(relationship('Cliente'))