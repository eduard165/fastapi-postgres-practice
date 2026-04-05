from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP
from app.db.database import Base
from sqlalchemy.sql import func

class User(Base):
    __tablename__ = "clientes"
    __table_args__ = {"schema": "logistica"}

    id_cliente = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    correo = Column(String, unique=True, index=True, nullable=False)
    telefono = Column(String, nullable=True)
    fecha_registro = Column(TIMESTAMP(timezone=True), server_default=func.now())
    activo = Column(Boolean, default=True)



