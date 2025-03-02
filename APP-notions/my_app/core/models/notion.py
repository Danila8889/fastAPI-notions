from sqlalchemy.orm import Mapped
from .mixins.id_mixin import IdInPkMixin
from .base import Base


class Notion(IdInPkMixin, Base):
    network: Mapped[str]
