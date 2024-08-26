import pytest
from main_3 import init_db, add_user, get_user


@pytest.fixture
def db_conn():
    conn = init_db()
    yield conn
    conn.close()


def test_add_or_get_user(db_conn):
    add_user(db_conn, 'John', 30)
    user = get_user(db_conn, 'John')

    # Предполагаем, что get_user возвращает словарь
    assert user == {'id': 1, 'name': 'John', 'age': 30}

