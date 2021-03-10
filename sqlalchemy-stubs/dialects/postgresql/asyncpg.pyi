from typing import Any
from typing import Optional

from . import json as json
from .base import ENUM as ENUM
from .base import INTERVAL as INTERVAL
from .base import OID as OID
from .base import PGCompiler as PGCompiler
from .base import PGDialect as PGDialect
from .base import PGExecutionContext as PGExecutionContext
from .base import PGIdentifierPreparer as PGIdentifierPreparer
from .base import REGCLASS as REGCLASS
from .base import UUID as UUID
from ... import exc as exc
from ... import pool as pool
from ... import processors as processors
from ... import util as util
from ...sql import sqltypes as sqltypes
from ...util.concurrency import await_fallback as await_fallback
from ...util.concurrency import await_only as await_only

class AsyncpgTime(sqltypes.Time):
    def get_dbapi_type(self, dbapi: Any): ...

class AsyncpgDate(sqltypes.Date):
    def get_dbapi_type(self, dbapi: Any): ...

class AsyncpgDateTime(sqltypes.DateTime):
    def get_dbapi_type(self, dbapi: Any): ...

class AsyncpgBoolean(sqltypes.Boolean):
    def get_dbapi_type(self, dbapi: Any): ...

class AsyncPgInterval(INTERVAL):
    def get_dbapi_type(self, dbapi: Any): ...
    @classmethod
    def adapt_emulated_to_native(cls, interval: Any, **kw: Any): ...

class AsyncPgEnum(ENUM):
    def get_dbapi_type(self, dbapi: Any): ...

class AsyncpgInteger(sqltypes.Integer):
    def get_dbapi_type(self, dbapi: Any): ...

class AsyncpgBigInteger(sqltypes.BigInteger):
    def get_dbapi_type(self, dbapi: Any): ...

class AsyncpgJSON(json.JSON):
    def get_dbapi_type(self, dbapi: Any): ...
    def result_processor(self, dialect: Any, coltype: Any) -> None: ...

class AsyncpgJSONB(json.JSONB):
    def get_dbapi_type(self, dbapi: Any): ...
    def result_processor(self, dialect: Any, coltype: Any) -> None: ...

class AsyncpgJSONIndexType(sqltypes.JSON.JSONIndexType):
    def get_dbapi_type(self, dbapi: Any) -> None: ...

class AsyncpgJSONIntIndexType(sqltypes.JSON.JSONIntIndexType):
    def get_dbapi_type(self, dbapi: Any): ...

class AsyncpgJSONStrIndexType(sqltypes.JSON.JSONStrIndexType):
    def get_dbapi_type(self, dbapi: Any): ...

class AsyncpgJSONPathType(json.JSONPathType):
    def bind_processor(self, dialect: Any): ...

class AsyncpgUUID(UUID):
    def get_dbapi_type(self, dbapi: Any): ...
    def bind_processor(self, dialect: Any): ...
    def result_processor(self, dialect: Any, coltype: Any): ...

class AsyncpgNumeric(sqltypes.Numeric):
    def bind_processor(self, dialect: Any) -> None: ...
    def result_processor(self, dialect: Any, coltype: Any): ...

class AsyncpgREGCLASS(REGCLASS):
    def get_dbapi_type(self, dbapi: Any): ...

class AsyncpgOID(OID):
    def get_dbapi_type(self, dbapi: Any): ...

class PGExecutionContext_asyncpg(PGExecutionContext):
    def handle_dbapi_exception(self, e: Any) -> None: ...
    exclude_set_input_sizes: Any = ...
    def pre_exec(self) -> None: ...
    def create_server_side_cursor(self): ...

class PGCompiler_asyncpg(PGCompiler): ...
class PGIdentifierPreparer_asyncpg(PGIdentifierPreparer): ...

class AsyncAdapt_asyncpg_cursor:
    server_side: bool = ...
    description: Any = ...
    arraysize: int = ...
    rowcount: int = ...
    def __init__(self, adapt_connection: Any) -> None: ...
    def close(self) -> None: ...
    def execute(
        self, operation: Any, parameters: Optional[Any] = ...
    ) -> None: ...
    def executemany(self, operation: Any, seq_of_parameters: Any): ...
    def setinputsizes(self, *inputsizes: Any) -> None: ...
    def __iter__(self) -> Any: ...
    def fetchone(self): ...
    def fetchmany(self, size: Optional[Any] = ...): ...
    def fetchall(self): ...

class AsyncAdapt_asyncpg_ss_cursor(AsyncAdapt_asyncpg_cursor):
    server_side: bool = ...
    def __init__(self, adapt_connection: Any) -> None: ...
    def close(self) -> None: ...
    def __aiter__(self): ...
    async def __anext__(self) -> None: ...
    def fetchone(self): ...
    def fetchmany(self, size: Optional[Any] = ...): ...
    def fetchall(self): ...
    def executemany(self, operation: Any, seq_of_parameters: Any) -> None: ...

class AsyncAdapt_asyncpg_connection:
    await_: Any = ...
    dbapi: Any = ...
    isolation_level: str = ...
    readonly: bool = ...
    deferrable: bool = ...
    def __init__(
        self,
        dbapi: Any,
        connection: Any,
        prepared_statement_cache_size: int = ...,
    ) -> None: ...
    @property
    def autocommit(self): ...
    @autocommit.setter
    def autocommit(self, value: Any) -> None: ...
    def set_isolation_level(self, level: Any) -> None: ...
    def cursor(self, server_side: bool = ...): ...
    def rollback(self) -> None: ...
    def commit(self) -> None: ...
    def close(self) -> None: ...

class AsyncAdaptFallback_asyncpg_connection(AsyncAdapt_asyncpg_connection):
    await_: Any = ...

class AsyncAdapt_asyncpg_dbapi:
    asyncpg: Any = ...
    paramstyle: str = ...
    def __init__(self, asyncpg: Any) -> None: ...
    def connect(self, *arg: Any, **kw: Any): ...
    class Error(Exception): ...
    class Warning(Exception): ...
    class InterfaceError(Error): ...
    class DatabaseError(Error): ...
    class InternalError(DatabaseError): ...
    class OperationalError(DatabaseError): ...
    class ProgrammingError(DatabaseError): ...
    class IntegrityError(DatabaseError): ...
    class DataError(DatabaseError): ...
    class NotSupportedError(DatabaseError): ...
    class InternalServerError(InternalError): ...
    class InvalidCachedStatementError(NotSupportedError):
        def __init__(self, message: Any) -> None: ...
    def Binary(self, value: Any): ...
    STRING: Any = ...
    TIMESTAMP: Any = ...
    TIMESTAMP_W_TZ: Any = ...
    TIME: Any = ...
    DATE: Any = ...
    INTERVAL: Any = ...
    NUMBER: Any = ...
    FLOAT: Any = ...
    BOOLEAN: Any = ...
    INTEGER: Any = ...
    BIGINTEGER: Any = ...
    BYTES: Any = ...
    DECIMAL: Any = ...
    JSON: Any = ...
    JSONB: Any = ...
    ENUM: Any = ...
    UUID: Any = ...
    BYTEA: Any = ...
    DATETIME: Any = ...
    BINARY: Any = ...

class PGDialect_asyncpg(PGDialect):
    driver: str = ...
    supports_unicode_statements: bool = ...
    supports_server_side_cursors: bool = ...
    supports_unicode_binds: bool = ...
    default_paramstyle: str = ...
    supports_sane_multi_rowcount: bool = ...
    execution_ctx_cls: Any = ...
    statement_compiler: Any = ...
    preparer: Any = ...
    use_setinputsizes: bool = ...
    use_native_uuid: bool = ...
    colspecs: Any = ...
    is_async: bool = ...
    @classmethod
    def dbapi(cls): ...
    def set_isolation_level(self, connection: Any, level: Any) -> None: ...
    def set_readonly(self, connection: Any, value: Any) -> None: ...
    def get_readonly(self, connection: Any): ...
    def set_deferrable(self, connection: Any, value: Any) -> None: ...
    def get_deferrable(self, connection: Any): ...
    def create_connect_args(self, url: Any): ...
    @classmethod
    def get_pool_class(cls, url: Any): ...
    def is_disconnect(self, e: Any, connection: Any, cursor: Any): ...
    def do_set_input_sizes(
        self, cursor: Any, list_of_tuples: Any, context: Any
    ) -> None: ...
    def on_connect(self): ...

dialect = PGDialect_asyncpg