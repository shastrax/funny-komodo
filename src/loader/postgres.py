"""funny komodo postgresql support"""

import datetime
import time

import sqlalchemy
#from sqlalchemy import and_
#from sqlalchemy import select

from sql_table import Fortune

class PostGres:
    """mellow heeler postgresql support"""

    db_engine = None
    Session = None

    def __init__(self, session: sqlalchemy.orm.session.sessionmaker):
        self.Session = session

    def fortune_insert(self, uuid: str, message: str) -> Fortune:
        """fortune row insert"""

        candidate = Fortune(False, 0, uuid, message)

        session = self.Session()
        session.add(candidate)
        session.commit()
        session.close()

        return candidate
