from sqlalchemy import create_engine, text


class UsersTable:
    __scripts = {
        # создание нового пользователя
        "insert_new_user": text("""
            INSERT INTO users (user_id, "user_email", subject_id)
            VALUES (:user_id, :user_email, :subject_id)
            """),
        # удаление пользователя по id
        "delete_by_id": text(
            "DELETE FROM users WHERE user_id = :id_to_delete"),
        # получение пользователя по максимальному id
        "select_by_id": text("""
            SELECT * FROM users WHERE user_id = :user_id
            ORDER BY user_id DESC LIMIT 1
            """),
        # получение пользователя по максимальному email
        "select_by_email": text("""
            SELECT * FROM users WHERE user_email = :user_email
            ORDER BY user_id DESC LIMIT 1
            """),
        # получение максимального id
        "get_max_id": text(
            "SELECT user_id FROM users ORDER BY user_id DESC LIMIT 1"),
        # получение всех данных таблицы users
        "get_users_table": text("SELECT * FROM users ORDER BY user_id ASC"),
        # изменение email по id пользователя
        "update_user_by_id": text("""
            UPDATE users SET user_email = :user_email,
            subject_id = :subject_id WHERE user_id = :user_id
            """)
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)
        self.acc = None

    def _ensure_connection(self):
        # Гарантирует наличие активного соединения(частный случай)
        if self.acc is None or self.acc.closed:
            self.acc = self.__db.connect()
        return self.acc

    def get_max_id(self):
        conn = self._ensure_connection()
        result = conn.execute(self.__scripts["get_max_id"])
        max_id = result.scalar()

        return max_id

    def get_users_table(self):
        conn = self._ensure_connection()
        return conn.execute(self.__scripts["get_users_table"]).all()

    def get_user_data_by_id(self, user_id):
        conn = self._ensure_connection()
        result = conn.execute(
            self.__scripts["select_by_id"], {"user_id": user_id})
        row = result.mappings().first()
        # оператор first() выдает первое значение в массиве или списке
        # оператор all() выдает весь массив или список

        return row

    def get_user_data_by_email(self, user_email):
        conn = self._ensure_connection()
        result = conn.execute(
            self.__scripts["select_by_email"], {"user_email": user_email})
        row = result.mappings().first()

        return row

    def create_user(self, user_id, user_email, subject_id):
        conn = self._ensure_connection()
        conn.execute(
            self.__scripts["insert_new_user"],
            {
                "user_id": user_id,
                "user_email": user_email,
                "subject_id": subject_id
                })
        conn.commit()

    def update_user_by_id(self, user_email, subject_id, user_id):
        conn = self._ensure_connection()
        conn.execute(
            self.__scripts["update_user_by_id"],
            {
                "user_email": user_email,
                "subject_id": subject_id,
                "user_id": user_id
                })
        conn.commit()

    def delete(self, user_id):
        conn = self._ensure_connection()
        conn.execute(
            self.__scripts["delete_by_id"],
            {"id_to_delete": user_id}
        )
        conn.commit()  # подтверждаем удаление

    def close(self):
        if self.acc and not self.acc.closed:
            self.acc.close()
            self.acc = None
