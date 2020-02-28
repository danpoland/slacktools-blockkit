from typing import List, Union

from .attributes import (
    BooleanAttr,
    ListAttr,
    PlainTextAttr,
    TextAttr,
    TextObjectAttr,
    UrlAttr,
)
from .generics import SlackObject

__all__ = (
    "PlainText",
    "MrkdwnText",
    "ConfirmationDialog",
    "Option",
    "OptionGroup",
)


class PlainText(SlackObject):
    """"
    Constructs a Slack plain text composition object.
    https://api.slack.com/reference/block-kit/composition-objects#text
    """

    type = TextAttr()
    text = TextAttr()
    emoji = BooleanAttr(required=False)

    def __init__(self, text: str, emoji: bool = None):
        """
        :param text: The text to be displayed.
        :param emoji: Indicates whether emojis in a text field should be escaped into the colon emoji format.
        """
        super().__init__(type="plain_text", text=text, emoji=emoji)


class MrkdwnText(SlackObject):
    """"
    Constructs a Slack markdown text composition object.
    https://api.slack.com/reference/block-kit/composition-objects#text
    """

    type = TextAttr()
    text = TextAttr()
    verbatim = BooleanAttr(required=False)

    def __init__(self, text: str, verbatim: bool = None):
        """
        :param text: Markdown text to be used in the message.
        :param verbatim: When set to false (as is default) URLs will be auto-converted into links,
            conversation names will be link-ified, and certain mentions will be automatically parsed.
            Using a value of true will skip any preprocessing of this nature, although you can still
            include manual parsing strings.
        """
        super().__init__(type="mrkdwn", text=text, verbatim=verbatim)


class ConfirmationDialog(SlackObject):
    """
    Constructs a confirmation dialog object used for view submits.
    https://api.slack.com/reference/block-kit/composition-objects#confirm
    """

    title = PlainTextAttr(max_length=100)
    text = TextObjectAttr(max_length=300)
    confirm = PlainTextAttr(max_length=30)
    deny = PlainTextAttr(max_length=30)

    def __init__(
        self,
        title: str,
        text_object: Union[PlainText, MrkdwnText],
        confirm: str,
        deny: str,
    ):
        """
        :param title: The title of the dialog.
        :param text_object: Defines the explanatory text.
        :param confirm: The text for the confirm button.
        :param deny: The text for the deny button.
        :return: The confirm block object as a dict.
        """
        super().__init__(
            title=PlainText(title),
            text=text_object,
            confirm=PlainText(confirm),
            deny=PlainText(deny),
        )


class Option(SlackObject):
    """
    Constructs a Slack option block for select elements.
    https://api.slack.com/reference/block-kit/composition-objects#option
    """

    text = PlainTextAttr(max_length=75)
    value = TextAttr(max_length=75)
    description = PlainTextAttr(max_length=75, required=False)
    url = UrlAttr(max_length=3000, required=False)

    def __init__(self, text: str, value: str, description: str = None, url: str = None):
        """
        :param text: The text to be displayed.
        :param value: The value of the selected item.
        :param description: Descriptive text shown below the text field beside the radio button.
        :param url: A URL to load in the user's browser when the option is clicked.
            The url attribute is only available in overflow menus.
        """
        super().__init__(
            text=PlainText(text),
            value=value,
            description=PlainText(description) if description else None,
            url=url,
        )


class OptionGroup(SlackObject):
    """
    Constructs a Slack option group block.
    https://api.slack.com/reference/block-kit/composition-objects#option_group
    """

    label = PlainTextAttr(max_length=75)
    options = ListAttr(Option, max_length=100)

    def __init__(self, label: str, options: List[Option]):
        """
        :param label: Defines the label shown above this group of options.
        :param options: A list of Option objects.
        """
        super().__init__(label=PlainText(label), options=options)
