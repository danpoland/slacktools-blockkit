from .elements import Button
from .objects import ConfirmationDialog

__all__ = ("FixedButton",)


class FixedButton(Button):
    """
    Facilitates the definition of `Button` elements using fixed, referencable, attributes.
    """

    action_id: str = None
    text: str = None
    value: str = None
    url: str = None
    confirm: ConfirmationDialog = None
    style: Button.Styles = None

    def __init__(self, **kwargs):
        super().__init__(
            **{
                "action_id": self.action_id,
                "text": self.text,
                "value": self.value,
                "url": self.url,
                "confirm": self.confirm,
                "style": self.style,
                **kwargs,
            }
        )
