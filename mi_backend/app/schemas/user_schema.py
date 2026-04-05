from pydantic import BaseModel, Field, EmailStr

class UserCreate(BaseModel):
    nombre: str = Field(..., description="Nombre del usuario", min_length=1)
    correo: EmailStr = Field(..., description="Correo electrónico del usuario")
    telefono: str = Field(None, description="Número de teléfono del usuario")
 