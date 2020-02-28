from datetime import datetime
from typing import Any, List, Sized
from urllib.parse import urlparse

from .exceptions import ValidationError

___all__ = (
    "validate_type",
    "validate_max_length",
    "validate_min_length",
    "validate_max_size",
    "validate_min_size",
    "validate_http_url",
    "validate_date",
    "validate_choices",
)


def validate_type(value: Any, *types: Any):
    """Validates that the provided value is of one of the specified types."""
    if not any(isinstance(value, t) for t in types):
        raise ValidationError(f"{value} must be of one of the expected types: {types}")


def validate_max_length(value: Sized, length: int):
    """Validates that the provided value has a length less than the specified length."""
    if len(value) > length:
        raise ValidationError(f"{value} is greater than max length: {length}")


def validate_min_length(value: Sized, length: int):
    """Validates that the provided value has a length greater than the specified length."""
    if len(value) < length:
        raise ValidationError(f"{value} is less than min length: {length}")


def validate_max_size(value: int, size: int):
    """Validates that the provided value is less than the specified size."""
    if value > size:
        raise ValidationError(f"{value} is greater than max size: {size}")


def validate_min_size(value: int, size: int):
    """Validates that the provided value is greater than the specified size."""
    if value < size:
        raise ValidationError(f"{value} is less than min size: {size}")


def validate_http_url(value: str):
    """Validates that the provided value is in a HTTP url format."""
    parsed = urlparse(value)
    if parsed[0] not in ("http", "https") or len(parsed[1].split(".")) < 2:
        raise ValidationError(f"Expected valid HTTP URL, got: {value}")


def validate_date(value: str):
    """Validates that the provided string value in the date format yyyy-mm-dd."""
    try:
        datetime.strptime(value, "%Y-%m-%d")
    except ValueError:
        raise ValidationError(
            f"Expected string in date format yyyy-mm-dd, got {value}."
        )


def validate_choices(value: str, choices: List[str]):
    """Validates that the provided value is one of options in the provided choices."""
    if value not in choices:
        raise ValidationError(f"Invalid choice {value}. Valid values are: {choices}")
