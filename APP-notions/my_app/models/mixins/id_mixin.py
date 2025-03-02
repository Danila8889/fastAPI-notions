from sqlalchemy.orm import Mapped, mapped_column


class IdInPkMixin:
    id: Mapped[int] = mapped_column(primary_key=True)