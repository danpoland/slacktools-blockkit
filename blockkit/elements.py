from enum import Enum
from typing import Any, Dict, List

from .attributes import *
from .exceptions import ValidationError
from .generics import SlackObject
from .objects import ConfirmationDialog, Option, OptionGroup, PlainText

__all__ = (
    "Element",
    "Image",
    "Input",
    "Button",
    "Checkboxes",
    "DatePicker",
    "PlainTextInput",
    "OverflowMenu",
    "RadioButtonGroup",
    "Select",
    "StaticSelect",
    "ConversationSelect",
    "UserSelect",
    "ChannelSelect",
    "MultiSelect",
    "StaticMultiSelect",
    "ConversationMultiSelect",
    "UserMultiSelect",
    "ChannelMultiSelect",
)


class Element(SlackObject):
    """Base class for Slack elements that are used in Slack blocks."""

    #: The `type` of element expected by Slack.
    element_type: str = None

    # Attributes
    type = TextAttr()

    def __init__(self, **object_attributes):
        """
        :param object_attributes: Attributes specific to a particular element.
        """
        super().__init__(type=self.element_type, **object_attributes)


class Image(Element):
    """
    Constructs a Image element for use by an input block object.
    https://api.slack.com/reference/block-kit/block-elements#static_select
    """

    element_type = "image"

    # Attributes
    image_url = UrlAttr()
    alt_text = TextAttr()

    def __init__(self, image_url: str, alt_text: str):
        """
        :param image_url: The URL of the image to be displayed.
        :param alt_text: A plain-text summary of the image. This should not contain any markup.
        """
        super().__init__(image_url=image_url, alt_text=alt_text)


class Input(Element):
    """Base class for input elements."""

    # Attributes
    action_id = TextAttr(max_length=255)

    def __init__(self, action_id: str, **input_attributes):
        """
        :param action_id: A unique identifier for the element.
        :param input_attributes: Attributes specific to a particular input element.
        """
        super().__init__(action_id=action_id, **input_attributes)

    @classmethod
    def parse_value(cls, action: Dict) -> Any:
        """
        Parses the value from an action block pulled from a view's state values.

        :param action: The action block.
        :return: The input values.
        """
        return action.get("value")


class Button(Input):
    """
    Constructs a Slack button block.
    https://api.slack.com/reference/block-kit/block-elements#button
    """

    class Styles(Enum):
        DEFAULT = None
        PRIMARY = "primary"
        DANGER = "danger"

    element_type = "button"

    # Attributes
    text = PlainTextAttr(max_length=75)
    value = TextAttr(max_length=2000, required=False)
    url = UrlAttr(max_length=3000, required=False)
    confirm = ObjectAttr(ConfirmationDialog, required=False)
    style = TextAttr(choices=[s.value for s in Styles], required=False)

    def __init__(
        self,
        action_id: str,
        text: str,
        value: str = None,
        url: str = None,
        confirm: ConfirmationDialog = None,
        style: Styles = Styles.DEFAULT,
    ):
        """
        :param action_id: A unique identifier for the button block.
        :param text: The text to display on the button.
        :param value: A value returned with the action.
        :param url:  A URL to load in the user's browser when the button is clicked.
        :param confirm: A confirm object that defines an optional confirmation dialog after the button is clicked.
        :param style: None (default), primary or danger.
        """
        super().__init__(
            action_id=action_id,
            text=PlainText(text),
            value=str(value),
            url=url,
            confirm=confirm,
            style=style.value,
        )


class Checkboxes(Input):
    """
    Constructs a Slack checkbox group block.
    https://api.slack.com/reference/block-kit/block-elements#checkboxes
    """

    element_type = "checkboxes"

    # Attributes
    options = ListAttr(Option)
    initial_options = ListAttr(Option, required=False)
    confirm = ObjectAttr(ConfirmationDialog, required=False)

    def __init__(
        self,
        action_id: str,
        options: List[Option],
        initial_options: List[Option] = None,
        confirm: ConfirmationDialog = None,
    ):
        """
        :param options: A list of Option objects.
        :param initial_options: A list of Option objects. These options will be selected
            when the checkbox group initially loads.
        :param confirm: A confirm object that defines an optional ConfirmationDialog that
            appears after clicking one of the checkboxes in this element.
        """
        super().__init__(
            action_id,
            options=options,
            initial_options=initial_options,
            confirm=confirm,
        )

    @classmethod
    def parse_value(cls, action) -> Any:
        if options := action.get("selected_options"):
            return [option["value"] for option in options]


class DatePicker(Input):
    """
    Constructs a Slack datepicker element.
    https://api.slack.com/reference/block-kit/block-elements#datepicker
    """

    element_type = "datepicker"

    # Attributes
    placeholder = PlainTextAttr(max_length=150, required=False)
    initial_date = DateAttr(required=False)
    confirm = ObjectAttr(ConfirmationDialog, required=False)

    def __init__(
        self,
        action_id: str,
        placeholder: str = None,
        initial_date: str = None,
        confirm: ConfirmationDialog = None,
        **input_attributes,
    ):
        """
        :param placeholder: The placeholder text to display in the input element.
        :param initial_date: The initial date that is selected when the element is loaded (YYYY-MM-DD).
        :param confirm: A confirm object that defines an optional confirmation dialog that appears
            after a date is selected.
        """
        super().__init__(
            action_id=action_id,
            placeholder=PlainText(placeholder) if placeholder else None,
            initial_date=initial_date,
            confirm=confirm,
        )

    @classmethod
    def parse_value(cls, action) -> str:
        return action.get("selected_date")


class PlainTextInput(Input):
    """
    Constructs a slack plain text input element.
    https://api.slack.com/reference/block-kit/block-elements#input
    """

    element_type = "plain_text_input"

    # Attributes
    placeholder = PlainTextAttr(max_length=150, required=False)
    initial_value = TextAttr(required=False)
    multiline = BooleanAttr(required=False)
    min_length = IntegerAttr(max_size=3000, required=False)
    max_length = IntegerAttr(required=False)

    def __init__(
        self,
        action_id: str,
        placeholder: str = None,
        initial_value: str = None,
        multiline: bool = False,
        min_length: int = None,
        max_length: int = None,
    ):
        """
        :param placeholder: The placeholder text to display in the input element.
        :param initial_value: The initial value in the plain-text input when it is loaded.
        :param multiline: If the text input should allow multiple lines.
        :param min_length: The minimum length of input that the user must provide.
        :param max_length: The maximum length of input that the user can provide.
        """
        super().__init__(
            action_id=action_id,
            placeholder=PlainText(placeholder) if placeholder else None,
            initial_value=initial_value,
            multiline=multiline,
            min_length=min_length,
            max_length=max_length,
        )


class OverflowMenu(Input):
    """
    Constructs a slack overflow menu element.
    https://api.slack.com/reference/block-kit/block-elements#overflow
    """

    element_type = "overflow"

    # Attributes
    options = ListAttr(Option, max_length=5, min_length=2)
    confirm = ObjectAttr(ConfirmationDialog, required=False)

    def __init__(
        self, action_id: str, options: List[Option], confirm: ConfirmationDialog = None,
    ):
        """
        :param options:  A list of option objects to display in the menu. Maximum number
            of options is 5, minimum is 2.
        :param confirm: A confirm object that defines an optional ConfirmationDialog that
            appears after a menu item is selected.
        """
        super().__init__(action_id=action_id, options=options, confirm=confirm)

    @classmethod
    def parse_value(cls, action) -> Any:
        if option := action.get("selected_option"):
            return option["value"]


class RadioButtonGroup(Input):
    """
    Constructs a slack radio button group element.
    https://api.slack.com/reference/block-kit/block-elements#radio
    """

    element_type = "radio_buttons"

    # Attributes
    options = ListAttr(Option)
    initial_option = ObjectAttr(Option, required=False)
    confirm = ObjectAttr(ConfirmationDialog, required=False)

    def __init__(
        self,
        action_id: str,
        options: List[Option],
        initial_option: Option = None,
        confirm: ConfirmationDialog = None,
    ):
        """
        :param options:  A list of option objects to display in the menu.
        :param initial_option: This option will be selected when the radio button group initially loads.
        :param confirm: A confirm object that defines an optional ConfirmationDialog that appears after
            clicking one of the radio buttons in this element.
        """
        super().__init__(
            action_id=action_id,
            options=options,
            initial_option=initial_option,
            confirm=confirm,
        )

    @classmethod
    def parse_value(cls, action):
        if option := action.get("selected_option"):
            return option["value"]


class Select(Input):
    """Base class for select input element classes."""

    # Attributes
    placeholder = PlainTextAttr(max_length=150)
    confirm = ObjectAttr(ConfirmationDialog, required=False)

    def __init__(
        self,
        action_id: str,
        placeholder: str = None,
        confirm: ConfirmationDialog = None,
        **select_attributes,
    ):
        """
        :param action_id: A unique identifier for the element.
        :param placeholder: The placeholder text to display in the input element.
        :param confirm: A confirm object that defines an optional confirmation dialog that appears after
            a menu item is selected.
        :param select_attributes: Attributes specific to a select input element.
        """
        super().__init__(
            action_id=action_id,
            placeholder=PlainText(placeholder) if placeholder else None,
            confirm=confirm,
            **select_attributes,
        )


class StaticSelect(Select):
    """
    Constructs a static select element for use by an input block object.
    https://api.slack.com/reference/block-kit/block-elements#static_select
    """

    element_type = "static_select"

    # Attributes
    options = ListAttr(Option, max_length=100, required=False)
    option_groups = ListAttr(OptionGroup, max_length=100, required=False)
    initial_option = ObjectAttr(Option, required=False)

    def __init__(
        self,
        options: List[Option] = None,
        option_groups: List[OptionGroup] = None,
        initial_option: Option = None,
        **select_attributes,
    ):
        """
        :param options: A List of option blocks.
        :param option_groups: A List of option group blocks.
        :param initial_option: The initial item to be pre-selected.
        """
        if options and option_groups or not options and not option_groups:
            raise ValidationError(
                "StaticSelect: One of options or option_groups must be specified."
            )
        super().__init__(
            options=options,
            option_groups=option_groups,
            initial_option=initial_option,
            **select_attributes,
        )

    @classmethod
    def parse_value(cls, action):
        if selected_option := action.get("selected_option"):
            return selected_option.get("value")


class ConversationSelect(Select):
    """
    Constructs a Slack conversation select element.
    https://api.slack.com/reference/block-kit/block-elements#conversation_select
    """

    element_type = "conversations_select"

    # Attributes
    initial_conversation = TextAttr(required=False)

    def __init__(self, initial_conversation: str = None, **select_attributes):
        """
        :param initial_conversation: The ID of any valid conversation to be pre-selected when the menu loads.
        """
        super().__init__(initial_conversation=initial_conversation, **select_attributes)

    @classmethod
    def parse_value(cls, action):
        return action.get("selected_conversation")


class ChannelSelect(Select):
    """
    Constructs a Slack channel select element.
    https://api.slack.com/reference/block-kit/block-elements#channel_select
    """

    element_type = "channels_select"

    # Attributes
    initial_channel = TextAttr(required=False)

    def __init__(
        self, initial_channel: str = None, **select_attributes,
    ):
        """
        :param initial_channel: The ID of any valid public channel to be pre-selected when the menu loads.
        """
        super().__init__(initial_channel=initial_channel, **select_attributes)

    @classmethod
    def parse_value(cls, action):
        return action.get("selected_channel")


class UserSelect(Select):
    """
    Constructs a Slack user select element.
    https://api.slack.com/reference/block-kit/block-elements#users_select
    """

    element_type = "users_select"

    # Attributes
    initial_user = TextAttr(required=False)

    def __init__(self, initial_user: str = None, **select_attributes):
        """
        :param initial_user: The user ID of any valid user to be pre-selected when the menu loads.
        """
        super().__init__(initial_user=initial_user, **select_attributes)

    @classmethod
    def parse_value(cls, action):
        return action.get("selected_user")


class MultiSelect(Select):
    """Base class for multi-select classes."""

    # Attributes
    max_selected_items = IntegerAttr(min_size=1, required=False)

    def __init__(
        self, max_selected_items: int = None, **select_attributes,
    ):
        """
        :param max_selected_items: Specifies the maximum number of items that can be
            selected in the menu. Minimum number is 1.
        :param select_attributes:  Attributes specific to a multi-select input element.
        """
        super().__init__(
            max_selected_items=max_selected_items, **select_attributes,
        )


class StaticMultiSelect(MultiSelect):
    """
    Constructs a multi-select element with static options for use by an input block object.
    """

    element_type = "multi_static_select"

    # Attributes
    options = ListAttr(Option, max_length=100, required=False)
    option_groups = ListAttr(OptionGroup, max_length=100, required=False)
    initial_option = ObjectAttr(Option, required=False)

    def __init__(
        self,
        options: List[Option] = None,
        option_groups: List[OptionGroup] = None,
        initial_options: Option = None,
        **select_attributes,
    ):
        """
        :param options: A list of Option objects. Max length of 100. If option_groups is specified,
            this field should not be.
        :param option_groups: A list of OptionGroup objects. Max length of 100. If options is specified,
            this field should not be.
        :param initial_options: These options will be selected when the menu initially loads.
        """
        if options and option_groups or not options and not option_groups:
            raise ValidationError(
                "StaticMultiSelect: One of options or option_groups can be specified."
            )
        super().__init__(
            options=options,
            option_groups=option_groups,
            initial_options=initial_options,
            **select_attributes,
        )

    @classmethod
    def parse_value(cls, action):
        if options := action.get("selected_options"):
            return [option["value"] for option in options]


class ConversationMultiSelect(MultiSelect):
    """
    Constructs a multi-select element with pre-populated conversation options for use by an input block object.
    https://api.slack.com/reference/block-kit/block-elements#conversation_multi_select
    """

    element_type = "multi_conversations_select"

    # Attributes
    initial_conversations = ListAttr(str, required=False)

    def __init__(
        self, initial_conversations: List[str] = None, **select_attributes,
    ):
        """
        :param initial_conversations: A list of one or more IDs of any valid conversations
            to be pre-selected when the menu loads.
        """
        super().__init__(
            initial_conversations=initial_conversations, **select_attributes
        )

    @classmethod
    def parse_value(cls, action):
        return action.get("selected_conversations")


class UserMultiSelect(MultiSelect):
    """
    Constructs a multi-select element with pre-populated user options for use by an input block object.
    https://api.slack.com/reference/block-kit/block-elements#users_multi_select
    """

    element_type = "multi_users_select"

    # Attributes
    initial_users = ListAttr(str, required=False)

    def __init__(self, initial_users: List[str] = None, **select_attributes):
        """
        :param initial_users: A list of user IDs of any valid users to be pre-selected when the menu loads.
        """
        super().__init__(
            initial_users=initial_users, **select_attributes,
        )

    @classmethod
    def parse_value(cls, action):
        return action.get("selected_users")


class ChannelMultiSelect(MultiSelect):
    """
    Constructs a multi-select element with pre-populated channel options for use by an input block object.
    https://api.slack.com/reference/block-kit/block-elements#channel_multi_select
    """

    element_type = "multi_channels_select"

    # Attributes
    initial_channels = ListAttr(str, required=False)

    def __init__(self, initial_channels: List[str] = None, **select_attributes):
        """
        :param initial_channels: A list of user IDs of any valid users to be pre-selected when the menu loads.
        """
        super().__init__(
            initial_channels=initial_channels, **select_attributes,
        )

    @classmethod
    def parse_value(cls, action):
        return action.get("selected_channels")
