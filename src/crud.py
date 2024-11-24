from typing import Optional, Type, TypeVar
from sqlalchemy.orm import Session


# from sqlmodel import Session, SQLModel, select

# T = TypeVar("T", bound=SQLModel)


def create(session: Session, model, data):
    obj = model(**data.model_dump())
    session.add(obj)
    session.flush()
    session.refresh(obj)
    return obj


# def get_all(session: Session, model: Type[T]) -> list[T]:
#     query = select(model)
#     return session.exec(query).all()


# def get_one(session: Session, model: Type[T], id: int) -> Optional[T]:
#     query = select(model).where(model.id == id)
#     return session.exec(query).one_or_none()


# def update(session: Session, model: Type[T], id: int, data: T) -> Optional[T]:
#     query = select(model).where(model.id == id)
#     obj = session.exec(query).one_or_none()

#     if not obj:
#         return None

#     obj.sqlmodel_update(data.model_dump(exclude_unset=True))

#     session.flush()
#     session.refresh(obj)
#     return obj


# def delete(session: Session, model: Type[T], id: int) -> bool:
#     query = select(model).where(model.id == id)
#     obj = session.exec(query).one_or_none()

#     if not obj:
#         return False

#     session.delete(obj)
#     session.flush()
#     return True
