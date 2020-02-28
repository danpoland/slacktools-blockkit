import pytest

from blockkit.elements import Button
from blockkit.fixed_elements import *
from blockkit.objects import ConfirmationDialog, PlainText


class MockFixedButton(FixedButton):
    action_id = "test_action"
    text = "text"
    value = "value"
    url = "http://crispy.dev"
    confirm = ConfirmationDialog(
        text_object=PlainText("text"), title="title", confirm="confirm", deny="deny",
    )
    style = Button.Styles.DEFAULT


class TestFixedButton:
    def test_fixed(self, snapshot):
        snapshot.assert_match(MockFixedButton())

    @pytest.mark.parametrize(
        "field, value",
        [
            ("action_id", "override"),
            ("value", "override"),
            (
                "confirm",
                ConfirmationDialog(
                    text_object=PlainText("override"),
                    title="override",
                    confirm="confirm",
                    deny="deny",
                ),
            ),
            ("text", "override"),
            ("style", Button.Styles.DANGER),
        ],
    )
    def test_override(self, snapshot, field, value):
        snapshot.assert_match(MockFixedButton(**{field: value}))
