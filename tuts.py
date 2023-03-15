from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import  declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class Address(Base):
    __tablename__ = "addresses"
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="addresses")
    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)
    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
            self.name,
            self.fullname,
            self.nickname,
        )
    addresses = relationship("Address", order_by=Address.id, back_populates="user")


from sqlalchemy import create_engine
engine = create_engine("sqlite:///:memory:", echo=True)
Base.metadata.create_all(engine)


from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

ed_user = User(name="ed", fullname="Ed Jones", nickname="edsnickname")
session.add(ed_user)

session.add_all(
    [
        User(name="wendy", fullname="Wendy Williams", nickname="windy"),
        User(name="mary", fullname="Mary Contrary", nickname="mary"),
        User(name="fred", fullname="Fred Flintstone", nickname="freddy"),
    ]
)
