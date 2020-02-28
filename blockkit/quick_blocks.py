from .blocks import Section
from .messages import Message
from .objects import MrkdwnText

__all__ = ("MrkdwnTextSection", "SimpleMrkdwnMessage")


class SimpleMrkdwnMessage(Message):
    """Convenience class that constructs a block section with a single markdown message."""

    def __init__(self, text: str):
        """
        :param text: Mrkdwn string to display in a section..
        """
        super().__init__(blocks=[MrkdwnTextSection(text)])


class MrkdwnTextSection(Section):
    """Convenience class that builds a section with a single mrkdwn text element."""

    def __init__(self, text: str):
        """
        :param text: Mrkdwn text.
        """
        super().__init__(text_object=MrkdwnText(text))
