from database.db import Base
import sqlalchemy as sa
from database.db import session
from sqlalchemy.orm import relationship


class Users(Base):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer(), primary_key=True)
    username = sa.Column(sa.String(50), unique=True, index=True)
    password = sa.Column(sa.String(50))

    @classmethod
    def check_username(cls, username):
        user = session.query(cls).filter(cls.username == username).first()
        return user

    @classmethod
    def check_password(cls, pwd):
        user = session.query(cls).filter(cls.password == pwd).first()
        return user

    @classmethod
    def check_credentials(cls, username, pwd):
        user = session.query(cls).filter(cls.password == pwd, cls.username == username).first()
        return user
    

association_partisipants = sa.Table('association_partisipants', Base.metadata,
    sa.Column('id', sa.Integer(), primary_key=True),
    sa.Column('users_id', sa.ForeignKey('users.id')),
    sa.Column('chat_id', sa.ForeignKey('chat.id'))
)


association_message = sa.Table('association_message', Base.metadata,
    sa.Column('id', sa.Integer(), primary_key=True),
    sa.Column('message_id', sa.ForeignKey('message.id')),
    sa.Column('chat_id', sa.ForeignKey('chat.id'))
)


class Message(Base):
    __tablename__ = 'message'
    id = sa.Column(sa.Integer(), primary_key=True)
    text = sa.Column(sa.Text())
    user_to_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))
    user_from_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))

    # user_to = relationship("Users", backref="back_users_to")
    # user_from = relationship("Users", backref="back_users_from")
    
    
class Chat(Base):
    __tablename__ = 'chat'
    id = sa.Column(sa.Integer(), primary_key=True)
    partisipants = relationship("Users",
                    secondary=association_partisipants)
    messages = relationship("Message", secondary=association_message)