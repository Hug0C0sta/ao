import uuid

from sqlalchemy import Column, String, UUID

from src.models.base import Base


class Opinion(Base):
    __tablename__ = 'opinion'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    opinion = Column(String)
    # fk_order_id = Column(Integer, ForeignKey('order.id'))
