from .attributes import Attribute

__all__ = (
    "SlackObjectMeta",
    "SlackObject",
)


class SlackObjectMeta(type):
    """
    A meta-class that allows for the assignment of `attributes` to a `SlackObject`.
    """

    def __new__(mcs, name, bases, attrs, **kwargs):
        klass = super().__new__(mcs, name, bases, attrs, **kwargs)
        attributes = {}

        for key in attrs:
            attr = attrs[key]
            if issubclass(attr.__class__, Attribute):
                attr.name = key
                attributes[key] = attr

        parent_attributes = getattr(klass, "_attributes", None)

        if parent_attributes:
            klass._attributes = {**parent_attributes, **attributes}
        else:
            klass._attributes = attributes

        return klass


class SlackObject(dict, metaclass=SlackObjectMeta):
    """Base class for all Slack objects represented as dictionaries."""

    def __init__(self, **kwargs):
        validated = {}

        for name, attr in self._attributes.items():
            value = attr.validate(kwargs.get(name))
            if value is not None:
                validated[name] = value

        super().__init__(**validated)
