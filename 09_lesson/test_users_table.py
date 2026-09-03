import os
import pytest
from dotenv import load_dotenv
from UsersTable import UsersTable


load_dotenv()

"""
Из файла .env значение переменной возвращается в строковом значении,
поэтому глобальные переменные требуют перезаписи в числовом значении.
"""

USER_ID_RAW = os.getenv('USER_ID')
USER_ID = int(USER_ID_RAW)

USER_EMAIL = os.getenv('USER_EMAIL')

SUBJECT_ID_RAW = os.getenv('SUBJECT_ID')
SUBJECT_ID = int(SUBJECT_ID_RAW)

NEW_EMAIL = os.getenv('NEW_EMAIL')

NEW_SUBJECT_ID_RAW = os.getenv('NEW_SUBJECT_ID')
NEW_SUBJECT_ID = int(NEW_SUBJECT_ID_RAW)


@pytest.fixture
def db():

    connect = os.getenv("MY_CONNECTION_STRING")
    db_connection = UsersTable(connect)
    yield db_connection


def test_insert_user(db):

    len_before = db.get_users_table()

    user_id = USER_ID
    user_email = USER_EMAIL
    subject_id = SUBJECT_ID

    db.create_user(user_id, user_email, subject_id)
    len_after = db.get_users_table()

    result = db.get_user_data_by_id(user_id)
    print(result)

    db.delete(user_id)
    db.close()

    assert len_after > len_before
    assert result['user_id'] == user_id
    assert result['user_email'] == user_email
    assert result['subject_id'] == subject_id


def test_insert_user2(db):

    len_before = db.get_users_table()

    user_id = USER_ID
    user_email = USER_EMAIL
    subject_id = SUBJECT_ID

    db.create_user(user_id, user_email, subject_id)
    len_after = db.get_users_table()

    result = db.get_user_data_by_email(user_email)
    print(result)

    db.delete(user_id)
    db.close()

    assert len_after > len_before
    assert result['user_id'] == user_id
    assert result['user_email'] == user_email
    assert result['subject_id'] == subject_id


def test_update_user(db):

    user_id = USER_ID
    user_email = USER_EMAIL
    subject_id = SUBJECT_ID

    db.create_user(user_id, user_email, subject_id)
    result = db.get_user_data_by_id(user_id)
    print(result)

    new_email = NEW_EMAIL
    new_subject_id = NEW_SUBJECT_ID
    db.update_user_by_id(new_email, new_subject_id, user_id)
    result2 = db.get_user_data_by_id(user_id)
    print(result2)

    db.delete(user_id)
    db.close()

    assert result2['user_id'] == result['user_id']
    assert result2['user_email'] != result['user_email']
    assert result2['subject_id'] != result['subject_id']
    assert result2['subject_id'] == new_subject_id
    assert result2['user_email'] == new_email


def test_delete_user(db):

    len_before = db.get_users_table()

    user_id = USER_ID
    user_email = USER_EMAIL
    subject_id = SUBJECT_ID

    db.create_user(user_id, user_email, subject_id)
    len_middle = db.get_users_table()

    db.delete(user_id)
    len_after = db.get_users_table()
    result = db.get_user_data_by_id(user_id)
    print(result)

    assert len_before < len_middle
    assert len_middle > len_after
    assert len_before == len_after
    assert result is None
