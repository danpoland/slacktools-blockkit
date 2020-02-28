__all__ = ("BlockKitError", "ValidationError")


class BlockKitError(Exception):
    """Base exception class for the blockkit package."""

    def __init__(self, message: str):
        self.message = message
        super(BlockKitError, self).__init__(message)


class ValidationError(BlockKitError):
    """Base class for validation exceptions."""

    pass
