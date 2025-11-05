from sqlalchemy import String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from app.core.config import config
from passlib.hash import pbkdf2_sha256


engine = create_engine(config.db_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, index=True)
    email: Mapped[str] = mapped_column(String, index=True)
    password: Mapped[str] = mapped_column(String, index=True)
    
    def set_password(self, plain_password: str):
        """Gera e salva o hash da senha."""
        self.password = pbkdf2_sha256.hash(plain_password)

    
    def check_password(self, plain_password: str) -> bool:
        """Verifica se a senha informada confere com o hash armazenado."""
        return pbkdf2_sha256.verify(plain_password, self.password)
