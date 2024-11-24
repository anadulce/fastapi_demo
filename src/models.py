from datetime import datetime

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, registry, relationship

table_registry = registry()


@table_registry.mapped_as_dataclass
class Genre:
    __tablename__ = 'genre'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)

    created_at: Mapped[datetime] = mapped_column(default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        default=func.now(), onupdate=func.now()
    )


@table_registry.mapped_as_dataclass
class Movie:
    __tablename__ = 'movie'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    title: Mapped[str]
    director: Mapped[str]
    year: Mapped[int]

    genre: Mapped[int] = mapped_column(ForeignKey('genre.id'))
    genre_relationship: Mapped[Genre] = relationship('Genre', backref='movies')

    created_at: Mapped[datetime] = mapped_column(default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        default=func.now(), onupdate=func.now()
    )
