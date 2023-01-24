import threading

from sqlalchemy import Column, String

from Loverbot.modules.sql import BASE, SESSION


class LoverChats(BASE):
    __tablename__ = "lover_chats"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id


LoverChats.__table__.create(checkfirst=True)
INSERTION_LOCK = threading.RLock()


def is_lover(chat_id):
    try:
        chat = SESSION.query(LoverChats).get(str(chat_id))
        return bool(chat)
    finally:
        SESSION.close()


def set_lover(chat_id):
    with INSERTION_LOCK:
        razerchat = SESSION.query(loverChats).get(str(chat_id))
        if not loverrchat:
            loverchat = LoverChats(str(chat_id))
        SESSION.add(loverchat)
        SESSION.commit()


def rem_lover(chat_id):
    with INSERTION_LOCK:
        loverchat = SESSION.query(LoverChats).get(str(chat_id))
        if loverchat:
            SESSION.delete(loverchat)
        SESSION.commit()


def get_all_lover_chats():
    try:
        return SESSION.query(LoverChats.chat_id).all()
    finally:
        SESSION.close()
