from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, TypeVar

from .validators import *

__all__ = (
    "Attribute",
    "IntegerAttr",
    "BooleanAttr",
    "TextAttr",
    "UrlAttr",
    "TextObjectAttr",
    "PlainTextAttr",
    "MrkdwnTextAttr",
    "ListAttr",
    "ObjectAttr",
    "DateAttr",
)

T = TypeVar("T")


@dataclass
class Attribute(ABC):
    """The base class for Slack object attributes."""

    #: The name of the attribute assigned to an object.
    name: str = None
    #: If a value must be supplied for the attribute.
    required: bool = True

    def validate(self, value: T = None) -> T:
        """
        :param value: The value to be validated.
        """
        if value is not None:
            return self._validate(value)
        elif self.required:
            raise ValidationError(f"{self.name} is a required attribute.")

    @abstractmethod
    def _validate(self, value: T) -> T:
        """
        Attribute specific validation.Raises `ValidationError` on validation failures.

        :return: None
        """
        pass


@dataclass
class IntegerAttr(Attribute):
    """Represents integer values."""

    max_size: int = None
    min_size: int = None

    def _validate(self, value: int) -> int:
        validate_type(value, int)
        if self.max_size:
            validate_max_size(value, self.max_size)
        if self.min_size:
            validate_min_size(value, self.min_size)
        return value


class BooleanAttr(Attribute):
    """Represents boolean attributes."""

    def _validate(self, value: bool) -> bool:
        validate_type(value, bool)
        return value


@dataclass
class TextAttr(Attribute):
    """Represents plain string values."""

    max_length: int = None
    choices: List[str] = None

    def __post_init__(self):
        if self.choices and self.max_length:
            for choice in self.choices:
                validate_max_length(choice, self.max_length)

    def _validate(self, value: str) -> str:
        validate_type(value, str)
        if self.max_length:
            validate_max_length(value, self.max_length)
        if self.choices:
            validate_choices(value, self.choices)
        return value


class UrlAttr(TextAttr):
    """Represents a HTTP URL attribute."""

    def _validate(self, value: str) -> str:
        super()._validate(value)
        validate_http_url(value)
        return value


class TextObjectAttr(TextAttr):
    """Base class for Slack text object attributes."""

    def _validate(self, value: Dict) -> Dict:
        super()._validate(value["text"])
        return value


class PlainTextAttr(TextObjectAttr):
    """An attribute representing Slack plain text objects."""

    def _validate(self, value: Dict) -> Dict:
        super()._validate(value)
        if obj_type := value.get("type") != "plain_text":
            raise ValidationError(f"Excepted `plain_text` type, got: {obj_type}")
        return value


class MrkdwnTextAttr(TextObjectAttr):
    """An attribute representing Slack mrkdwn text objects."""

    def _validate(self, value: Dict) -> Dict:
        super()._validate(value)
        if obj_type := value.get("type") != "mrkdwn":
            raise ValidationError(f"Excepted `mrkdwn` type, got: {obj_type}")
        return value


class ListAttr(Attribute):
    """Represents a list attributes that contains other Slack objects."""

    def __init__(
        self,
        *object_types: Any,
        max_length: int = None,
        min_length: int = None,
        **kwargs,
    ):
        """
        :param object_types: The object types the list attribute is permitted to hold.
        :param max_length: The maximum number of items allowed in the list.
        :param min_length: The minimum number of items allowed in the list.
        """
        super().__init__(**kwargs)
        self.object_types = object_types
        self.max_length = max_length
        self.min_length = min_length

    def _validate(self, value: List[Any]) -> List[Any]:
        validate_type(value, list)
        if self.max_length:
            validate_max_length(value, self.max_length)
        if self.min_length:
            validate_min_length(value, self.min_length)
        for item in value:
            validate_type(item, self.object_types)
        return value


class ObjectAttr(Attribute):
    """An attribute that represents one or more of the object types."""

    def __init__(self, *object_types, **kwargs):
        """
        :param object_types: One or more Slack objects that are allowed to be assigned to the attribute.
        """
        super().__init__(**kwargs)
        self.object_types = object_types

    def _validate(self, value: T) -> T:
        validate_type(value, *self.object_types)
        return value


class DateAttr(Attribute):
    """An attribute representing a date in the format YYYY-MM-DD."""

    def _validate(self, value: str) -> str:
        validate_date(value)
        return value
