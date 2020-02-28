from typing import Any, Dict, List, Union

from . import elements as elms
from .attributes import *
from .exceptions import ValidationError
from .generics import SlackObject
from .objects import MrkdwnText, PlainText

__all__ = (
    "Block",
    "Actions",
    "Context",
    "Divider",
    "File",
    "Image",
    "Section",
    "Input",
    "PlainTextInput",
    "DatepickerInput",
    "StaticSelectInput",
    "ConversationsSelectInput",
    "UsersSelectInput",
    "ChannelSelectInput",
    "StaticMultiSelectInput",
    "ConversationsMultiSelectInput",
    "UsersSelectMultiInput",
    "ChannelMultiSelectInput",
)


class Block(SlackObject):
    """Base class for Slack blocks."""

    #: The type of block expected by Slack.
    block_type: str = None

    # Attributes
    type = TextAttr()
    block_id = TextAttr(max_length=255, required=False)

    def __init__(self, block_id: str = None, **object_attributes):
        """
        :param block_id: A unique string to identify the block.
        :param object_attributes: Attributes specific to a particular block.
        """
        super().__init__(type=self.block_type, block_id=block_id, **object_attributes)


class Actions(Block):
    """
    Constructs a Slack actions block object.
    https://api.slack.com/reference/block-kit/blocks#actions
    """

    block_type = "actions"

    # Attributes
    elements = ListAttr(elms.Element, max_length=5)

    def __init__(self, elements: List[elms.Element], **block_attributes):
        """
        :param elements: The element blocks to be contained by the action block.
        """
        super().__init__(elements=elements, **block_attributes)


class Context(Block):
    """
    Constructs a Slack context block object.
    https://api.slack.com/reference/block-kit/blocks#context
    """

    block_type = "context"

    # Attributes
    elements = ListAttr(elms.Image, PlainText, MrkdwnText, max_length=10)

    def __init__(
        self,
        elements: List[Union[elms.Image, PlainText, MrkdwnText]],
        **block_attributes,
    ):
        """
        :param elements: A list of Image/PlainText/MrkdwnText objects. Maximum number of items is 10.
        """
        super().__init__(elements=elements, **block_attributes)


class Divider(Block):
    """
    Constructs a Slack divider block.
    https://api.slack.com/reference/block-kit/blocks#divider
    """

    block_type = "divider"


class File(Block):
    """
    Constructs a Slack file block.
    https://api.slack.com/reference/block-kit/blocks#file
    """

    block_type = "file"

    # Attributes
    external_id = TextAttr()
    source = TextAttr(choices=["remote"])

    def __init__(self, external_id: str, source: str = "remote", **block_attributes):
        """
        :param external_id: The external unique ID for this file.
        :param source: At the moment, source will always be remote for a remote file.
        """
        super().__init__(external_id=external_id, source=source, **block_attributes)


class Image(Block):
    """
    Constructs a Slack image block.
    https://api.slack.com/reference/block-kit/blocks#image
    """

    block_type = "image"

    # Attributes
    image_url = UrlAttr(max_length=3000)
    alt_text = TextAttr(max_length=2000)
    title = PlainTextAttr(max_length=2000, required=False)

    def __init__(
        self, image_url: str, alt_text: str, title: str = None, **block_attributes
    ):
        """
        :param image_url: The URL of the image to be displayed. Maximum length for this field is 3000 characters.
        :param alt_text: A summary of the image. This should not contain any markup. Maximum length for this
            field is 2000 characters.
        :param title: An optional title for the image. Max length of 2000.
        :param block_id: A string acting as a unique identifier for a block.
        """
        super().__init__(
            image_url=image_url,
            alt_text=alt_text,
            title=PlainText(title) if title else None,
            **block_attributes,
        )


class Section(Block):
    """
    Constructs a section block.
    https://api.slack.com/reference/block-kit/blocks#section
    """

    block_type = "section"

    # Attributes
    text = TextObjectAttr(max_length=3000, required=False)
    fields = ListAttr(PlainText, MrkdwnText, max_length=10, required=False)
    accessory = ObjectAttr(elms.Element, required=False)

    def __init__(
        self,
        text_object: Union[PlainText, MrkdwnText] = None,
        fields: List[Union[PlainText, MrkdwnText]] = None,
        accessory: elms.Element = None,
        **block_attributes,
    ):
        """
        :param text_object: PlainText or MrkdwnText.
        :param fields: A list of PlainText or MrkdwnText objects that will be rendered in a compact
            format that allows for 2 columns of side-by-side text.
        :param accessory: A Slack element object.
        """
        if not text_object and not fields:
            raise ValidationError(
                "Section: At least one of text_object or fields is required."
            )
        super().__init__(
            text=text_object, fields=fields, accessory=accessory, **block_attributes,
        )


class Input(Block):
    """
    Base class for input blocks.
    https://api.slack.com/reference/block-kit/blocks#input
    """

    block_type = "input"
    #: The element class to be used with the input.
    element_class: elms.Element = None

    # Attributes
    label = PlainTextAttr(max_length=2000)
    element = ObjectAttr(elms.Element)
    hint = PlainTextAttr(max_length=2000, required=False)
    optional = BooleanAttr(required=False)

    def __init__(
        self,
        action_id: str,
        label: str,
        hint: str = None,
        optional: bool = False,
        block_id: str = None,
        **element_kwargs,
    ):
        """
        :param action_id: A unique identifier pass to the input element.
        :param label: The text to use as the input's label.
        :param hint: An optional hint that appears below an input element in a lighter grey.
        :param optional: A boolean that indicates whether the input element may be empty when a user submits the modal.
        :param element_kwargs: The kwargs to pass the input element used by the block.
        """
        super().__init__(
            block_id=block_id,
            element=self.element_class(action_id=action_id, **element_kwargs),
            label=PlainText(label),
            optional=optional,
            hint=PlainText(hint) if hint else None,
        )

    @classmethod
    def parse(
        cls,
        state_values: Dict,
        block_id: str,
        action_id: str,
        raise_exception: bool = False,
    ) -> Any:
        """
        Extracts the input value from the view state values object.

        :param state_values: The view state values returned from Slack.
        :param block_id: The block_id where the input is located.
        :param action_id: The action_id of the input.
        :param raise_exception: If a `KeyError` should be raised if the block/action does not exist in the state.
        :return: The input value or None if block/actions does not exist and raise_exception=False.
        """
        try:
            return cls.element_class.parse_value(state_values[block_id][action_id])
        except KeyError as err:
            if raise_exception:
                raise err
        return None


class PlainTextInput(Input):
    """Constructs a Slack plain text input block."""

    element_class = elms.PlainTextInput


class DatepickerInput(Input):
    """Constructs a Slack datepicker input block object."""

    element_class = elms.DatePicker


class StaticSelectInput(Input):
    """Constructs a Slack `static_select` block object."""

    element_class = elms.StaticSelect


class ConversationsSelectInput(Input):
    """
    This select menu will populate its options with a list of public and private channels,
    DMs, and MPIMs visible to the current user in the active workspace.
    """

    element_class = elms.ConversationSelect


class UsersSelectInput(Input):
    """
    This select menu will populate its options with a list of Slack users visible
    to the current user in the active workspace
    """

    element_class = elms.UserSelect


class ChannelSelectInput(Input):
    """
    This select menu will populate its options with a list of public channels visible to the
    current user in the active workspace.
    """

    element_class = elms.ChannelSelect


class StaticMultiSelectInput(Input):
    """Constructs a Slack `multi_static_select` block object."""

    element_class = elms.StaticMultiSelect


class ConversationsMultiSelectInput(Input):
    """
    This select menu will populate its options with a list of public and private channels,
    DMs, and MPIMs visible to the current user in the active workspace.
    """

    element_class = elms.ConversationMultiSelect


class UsersSelectMultiInput(Input):
    """
    This select menu will populate its options with a list of Slack users visible
    to the current user in the active workspace
    """

    element_class = elms.UserMultiSelect


class ChannelMultiSelectInput(Input):
    """
    This select menu will populate its options with a list of public channels visible to the
    current user in the active workspace.
    """

    element_class = elms.ChannelMultiSelect
