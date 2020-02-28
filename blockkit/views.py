from typing import List

from .attributes import BooleanAttr, ListAttr, PlainTextAttr, TextAttr
from .blocks import Block
from .generics import SlackObject
from .objects import PlainText

__all__ = (
    "View",
    "HomeTabs",
    "Modal",
)


class View(SlackObject):
    """
    Base class for constructing Slack view surfaces.
    https://api.slack.com/reference/surfaces/views
    """

    #: Maps to the Slack object type
    view_type = None

    # Attributes
    type: str = TextAttr()
    blocks = ListAttr(SlackObject, max_length=100)
    private_metadata = TextAttr(max_length=3000, required=False)
    callback_id = TextAttr(max_length=255, required=False)
    external_id = TextAttr(required=False)

    def __init__(
        self,
        blocks: List[Block],
        private_metadata: str = None,
        callback_id: str = None,
        external_id: str = None,
        **view_attributes,
    ):
        """
        :param blocks: The block objects contained by the modal.
        :param private_metadata: An arbitrary string value for internal reference.
        :param callback_id: An identifier to recognize interactions and submissions of this particular view.
        :param external_id: A custom identifier that must be unique for all views on a per-team basis.
        :param view_attributes: Attributes specific to a particular view type.
        """

        super().__init__(
            type=self.view_type,
            blocks=blocks,
            private_metadata=private_metadata,
            callback_id=callback_id,
            external_id=external_id,
            **view_attributes,
        )


class HomeTabs(View):
    """
   Constructs a Slack home tabs view surface.
   https://api.slack.com/reference/surfaces/views
   """

    view_type = "home"


class Modal(View):
    """
    Constructs a Slack modal view surface.
    https://api.slack.com/reference/surfaces/views
    """

    view_type = "modal"
    title = PlainTextAttr(max_length=24)
    submit = PlainTextAttr(max_length=24, required=False)
    close = PlainTextAttr(max_length=24, required=False)
    clear_on_close = BooleanAttr(required=False)
    notify_on_close = BooleanAttr(required=False)

    def __init__(
        self,
        title: str,
        submit: str = None,
        close: str = None,
        clear_on_close: bool = False,
        notify_on_close: bool = False,
        **view_attributes,
    ):
        """
        :param title: The title to displayed on the modal.
        :param submit: The text to be displayed in the submit button.
        :param close: The text to be displayed in the close button.
        :param clear_on_close: When true, clicking on the close button will clear all views in a modal and close it.
        :param notify_on_close: Indicates whether Slack will send your request URL a `view_closed` event
            when a user clicks the close button.
        """
        super().__init__(
            title=PlainText(title),
            submit=PlainText(submit) if submit else None,
            close=PlainText(close) if clear_on_close else None,
            clear_on_close=clear_on_close,
            notify_on_close=notify_on_close,
            **view_attributes,
        )
