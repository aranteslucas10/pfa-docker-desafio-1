import os
import mysql.connector


def get_conn():
    return mysql.connector.connect(
        database=os.getenv('DB_DATABASE'),
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWD'),
    )


def set_modulos():
    if get_modulos() == []:
        conn = get_conn()
        cursor = conn.cursor()
        sql = "INSERT INTO modulo (name) VALUES ('Docker'), ('Fundamentos de Arquitetura de Software'), ('Comunicação'), ('RabbitMQ'), ('Autenticação e Keycloak')"
        cursor.execute(sql)
        conn.commit()
        conn.close()


def get_modulos():
    conn = get_conn()
    cursor = conn.cursor()
    sql = "SELECT name FROM modulo"
    cursor.execute(sql)
    rows = cursor.fetchall()
    conn.close()
    return rows
