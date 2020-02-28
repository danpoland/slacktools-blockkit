import pytest

from blockkit.objects import ConfirmationDialog, PlainText

__all__ = ("make_parse_block_args", "make_confirm")


@pytest.fixture
def make_parse_block_args():
    def _make_parse_block_args(action_data):
        state_values = {"test_block": {"test_action": action_data}}
        return {
            "state_values": state_values,
            "block_id": "test_block",
            "action_id": "test_action",
        }

    return _make_parse_block_args


@pytest.fixture
def make_confirm():
    def _make_confirm():
        return ConfirmationDialog(
            text_object=PlainText("text"),
            title="title",
            confirm="confirm",
            deny="deny",
        )

    return _make_confirm
