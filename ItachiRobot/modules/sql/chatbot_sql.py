import threading

from sqlalchemy import Column, String

from ItachiRobot.modules.sql import BASE, SESSION


class RudraChats(BASE):
    __tablename__ = "Rudra_chats"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id


RudraChats.__table__.create(checkfirst=True)
INSERTION_LOCK = threading.RLock()


def is_Rudra(chat_id):
    try:
        chat = SESSION.query(RudraChats).get(str(chat_id))
        return bool(chat)
    finally:
        SESSION.close()


def set_Rudra(chat_id):
    with INSERTION_LOCK:
        Rudrachat = SESSION.query(RudraChats).get(str(chat_id))
        if not Rudrachat:
            Rudrachat = RudraChats(str(chat_id))
        SESSION.add(Rudrachat)
        SESSION.commit()


def rem_Rudra(chat_id):
    with INSERTION_LOCK:
        Rudrachat = SESSION.query(RudraChats).get(str(chat_id))
        if Rudrachat:
            SESSION.delete(Rudrachat)
        SESSION.commit()
