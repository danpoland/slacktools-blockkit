from typing import Any, Dict, List

from .blocks import (
    ConversationsSelectInput,
    DatepickerInput,
    PlainTextInput,
    StaticSelectInput,
)
from .elements import Button
from .objects import ConfirmationDialog, Option, OptionGroup

__all__ = (
    "FixedButton",
    "FixedInputMixin",
    "FixedDatePickerInput",
    "FixedStaticSelectInput",
    "FixedPlainTextInput",
    "FixedConversationsSelectInput",
)


class FixedButton(Button):
    action_id = None
    text = None
    style = None
    confirm = None

    def __init__(self, **kwargs):
        super().__init__(
            **{
                "action_id": self.action_id,
                "text": self.text,
                "style": self.style,
                "confirm": self.confirm,
                **kwargs,
            }
        )


class FixedInputMixin:
    """
    A mixin class that adds the standard `Input` block attributes to fixed block input classes.
    Allows for any of the attributes to overridden when a new object is created.
    """

    block_id: str = None
    action_id: str = None
    label: str = None
    optional: bool = False
    hint: str = None

    def __init__(self, **kwargs):
        super().__init__(
            **{
                "block_id": self.block_id,
                "action_id": self.action_id,
                "label": self.label,
                "optional": self.optional,
                "hint": self.hint,
                **kwargs,
            },
        )

    @classmethod
    def parse(
        cls, state_values: Dict, block_id: str = None, action_id: str = None, **kwargs
    ) -> Any:
        """
        If possible uses the FixedInput's `block_id` and `action_id` for parsing input values.
        If `block_id` or `action_id` is None on the class and no value is provided to `parse`
        a TypeError will be thrown.

        :param state_values: The state values returned from Slack in a view submission payload.
        :param block_id: The block id where the input is located.
        :param action_id: The action id of the input.
        :param kwargs: Input implementation specific arguments.
        """
        b_id = block_id or cls.block_id
        a_id = action_id or cls.action_id

        if b_id is None:
            raise TypeError("Missing required argument: 'block_id'")
        if a_id is None:
            raise TypeError("Missing required argument: 'action_id'")

        return super().parse(
            state_values=state_values, block_id=b_id, action_id=a_id, **kwargs
        )


class FixedDatePickerInput(FixedInputMixin, DatepickerInput):
    """
    Facilitates the definition of `DatepickerInput` blocks using fixed, referencable, attributes.
    """

    placeholder: str = None
    initial_date: str = None
    confirm: ConfirmationDialog = None

    def __init__(self, **kwargs):
        super().__init__(
            **{
                "placeholder": self.placeholder,
                "initial_date": self.initial_date,
                "confirm": self.confirm,
                **kwargs,
            },
        )


class FixedStaticSelectInput(FixedInputMixin, StaticSelectInput):
    """
    Facilitates the definition of `StaticSelectInput` blocks using fixed, referencable, attributes.
    """

    options: List[Option] = None
    option_groups: List[OptionGroup] = None
    initial_option: Option = None
    placeholder: str = None
    confirm: ConfirmationDialog = None

    def __init__(self, **kwargs):
        super().__init__(
            **{
                "options": self.options,
                "option_groups": self.option_groups,
                "initial_option": self.initial_option,
                "placeholder": self.placeholder,
                "confirm": self.confirm,
                **kwargs,
            },
        )


class FixedPlainTextInput(FixedInputMixin, PlainTextInput):
    """
    Facilitates the definition of `PlainTextInput` blocks using fixed, referencable, attributes.
    """

    initial_value: str = None
    multiline: bool = True
    min_length: int = None
    max_length: int = None
    placeholder: str = None

    def __init__(self, **kwargs):
        super().__init__(
            **{
                "initial_value": self.initial_value,
                "multiline": self.multiline,
                "min_length": self.min_length,
                "max_length": self.max_length,
                "placeholder": self.placeholder,
                **kwargs,
            },
        )


class FixedConversationsSelectInput(FixedInputMixin, ConversationsSelectInput):
    """
    Facilitates the definition of `ConversationsSelectInput` blocks using fixed, referencable, attributes.
    """

    initial_conversation: str = None
    placeholder: str = None

    def __init__(self, **kwargs):
        super().__init__(
            **{
                "initial_conversation": self.initial_conversation,
                "placeholder": self.placeholder,
                **kwargs,
            }
        )
