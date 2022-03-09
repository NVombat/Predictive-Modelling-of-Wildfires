from core.errorfactory import DataIntegrityErrors, DatabaseErrors, UserErrors


class InvalidArgumentError(DataIntegrityErrors):
    ...


class InvalidDataIDError(DataIntegrityErrors):
    ...


class ResultUpdationError(DatabaseErrors):
    ...


class UserDoesNotExistError(UserErrors):
    ...
