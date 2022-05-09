from core.errorfactory import (
    DataIntegrityErrors,
    DatabaseErrors,
    UserErrors,
    FileErrors,
)


class InvalidArgumentError(DataIntegrityErrors):
    ...


class InvalidDataIDError(DataIntegrityErrors):
    ...


class ResultUpdationError(DatabaseErrors):
    ...


class UserDoesNotExistError(UserErrors):
    ...


class FileInsertionError(FileErrors):
    ...
