"""
1. create a package called `dal` at project root
2. create a sub-package under `dal` package named `settings`
3. create a config file named `secrets.yaml` and copy-paste following code

https://paste.centos.org/view/a3746a77

4. create a python file under `dal` named `db_conn_helper.py`
  and copy-paste following code.

  https://paste.centos.org/view/c6f75a2d


5. execute `db_conn_helper.py` from the "run" button available at entrypoint clause.

"""

import pymysql
import toml
import yaml

from pymysql.connections import Connection

_settings = {}


def make_connection():
    try:
        connection = pymysql.connect(
            user="root",
            password="root",
            host="127.0.0.1",
            port=3306,
            database="starwarsDB"
        )
    except pymysql.err.Error as ex:
        print(f"[ ERROR ] cannot establish connection - {ex}")

    return connection


def _load_from_yaml():
    """
   loads settings from "settings/secrets.yaml" file
   and stores them into global ``_settings`` variable

   Returns:

   """

    global _settings

    with open("settings/secrets.yaml", "r") as fp:
        doc = yaml.load(fp, Loader=yaml.FullLoader)

    if not doc:
        return

    for key_, val_ in doc.items():
        _settings[key_] = val_


def get_db_conn() -> Connection:
    """
   Makes actual DB connection
   Returns:

   """

    _load_from_yaml()

    try:
        connection = pymysql.connect(**_settings)
    except pymysql.err.Error as ex:
        print(f"[ ERROR ] cannot make connection {ex}")
    return connection


def get_db_conn_toml():
    """picks configurations from settings/secret.toml

   {
   'host': '127.0.0.1',
   'user': 'adam',
   'port': 3306,
   'database': 'starwarsDB',
   'password': 'qwerty@123'
 }
 """

    with open("settings/secrets.toml", "r") as fp:
        config = toml.load(fp)
        dbconfig = config.get("mysqldb")
        conn_ = pymysql.connect(**dbconfig)
        return conn_


if __name__ == "__main__":
    conn = make_connection()
    toml_conn = get_db_conn_toml()
    yaml_conn = get_db_conn()
    breakpoint()
