#!/usr/bin/env python

"""
Copyright (c) 2006-2018 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

from lib.core.enums import DBMS
from lib.core.settings import MSSQL_SYSTEM_DBS
from lib.core.unescaper import unescaper
from plugins.dbms.mssqlserver.enumeration import Enumeration
from plugins.dbms.mssqlserver.filesystem import Filesystem
from plugins.dbms.mssqlserver.fingerprint import Fingerprint
from plugins.dbms.mssqlserver.syntax import Syntax
from plugins.dbms.mssqlserver.takeover import Takeover
from plugins.generic.misc import Miscellaneous

class MSSQLServerMap(Syntax, Fingerprint, Enumeration, Filesystem): # [Python 2.x], Miscellaneous, Takeover):
    """
    This class defines Microsoft SQL Server methods
    """

    def __init__(self):
        self.excludeDbsList = MSSQL_SYSTEM_DBS

        Syntax.__init__(self)
        Fingerprint.__init__(self)
        Enumeration.__init__(self)
        Filesystem.__init__(self)
        Miscellaneous.__init__(self)
        Takeover.__init__(self)

    unescaper[DBMS.MSSQL] = Syntax.escape
