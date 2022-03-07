from core.errorfactory import DataIntegrityErrors, UserErrors


class InvalidDataIDError(DataIntegrityErrors):
    ...


class UserDoesNotExistError(UserErrors):
    ...
