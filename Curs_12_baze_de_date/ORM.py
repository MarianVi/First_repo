# ORM --> Object Relational Maping

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


# Conectare la DB

engine = create_engine('sqlite:///users.db')

# Creare tabele
Base.metadata.create_all(engine)

# Pornire sesiune
Session = sessionmaker(bind=engine)
session = Session()

# Adaugare
u = User(name='Andrei', age=29)
u2 = User(name='Andreea', age=30)
session.add(u)
session.add(u2)
session.commit()
users = session.query(User).all()
for user in users:
    print(user.id, user.name, user.age)

user = session.query(User).filter_by(name='Andrei').first()
session.delete(user)
session.commit()
