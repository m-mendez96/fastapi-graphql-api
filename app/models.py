from sqlalchemy import (
    Boolean,
    Column,
    Date,
    DateTime,
    ForeignKey,
    Integer,
    PrimaryKeyConstraint,
    String,
    func,
)
from sqlalchemy.orm import relationship

from app.db import Base


class TypeDocument(Base):
    __tablename__ = "document_types"

    id = Column(Integer, primary_key=True, index=True)
    name_type_document = Column(String(50), unique=True, nullable=False)


class Country(Base):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True, index=True)
    country_code = Column(String(4), unique=True, nullable=False)
    country_name = Column(String(100), unique=True, nullable=False)


class AppUser(Base):
    __tablename__ = "app_users"

    id = Column(Integer, primary_key=True, index=True)
    last_name = Column(String(20), nullable=False)
    name = Column(String(20), nullable=False)
    is_militar = Column(Boolean, nullable=False, default=True)
    is_temporal = Column(Boolean, nullable=False, default=True)
    time_create = Column(DateTime(timezone=True), server_default=func.now())
    username = Column(String(20), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(20), unique=True, nullable=False)
    email_verified = Column(Boolean, default=False)
    verification_token = Column(String(255), nullable=True)

    documents = relationship("UserDocument", back_populates="user")
    contact_info = relationship(
        "ContactInfo", back_populates="user", uselist=False
    )


class UserDocument(Base):
    __tablename__ = "user_documents"

    user_id = Column(Integer, ForeignKey("app_users.id"), nullable=False)
    type_document_id = Column(
        Integer, ForeignKey("document_types.id"), nullable=False
    )
    document = Column(String(20), nullable=False)
    place_expedition = Column(String(60), nullable=False)
    date_expedition = Column(Date, nullable=False)

    __table_args__ = (PrimaryKeyConstraint("user_id", "type_document_id"),)

    user = relationship("AppUser", back_populates="documents")
    type_document = relationship("TypeDocument", backref="user_documents")


class ContactInfo(Base):
    __tablename__ = "contact_info"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(
        Integer, ForeignKey("app_users.id"), unique=True, nullable=False
    )
    address = Column(String(60), nullable=False)
    country_id = Column(Integer, ForeignKey("countries.id"), nullable=False)
    city = Column(String(50), nullable=False)
    phone = Column(String(20), nullable=False)
    cel_phone = Column(String(20), nullable=False)
    emergency_name = Column(String(100), nullable=False)
    emergency_phone = Column(String(20), nullable=False)

    user = relationship("AppUser", back_populates="contact_info")
    country = relationship("Country", backref="contact_infos")
