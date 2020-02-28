from typing import Dict, List

__all__ = ("Message",)


class Message(dict):
    """A base class constructing messages to be sent via Slack."""

    def __init__(self, blocks: List[Dict]):
        super().__init__(blocks=blocks)
