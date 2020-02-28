import pytest

from blockkit.exceptions import ValidationError
from blockkit.objects import PlainText
from blockkit.views import *


class MockView(View):
    view_type = "test"


@pytest.fixture
def view_attributes():
    return {
        "blocks": [PlainText("text")],
        "private_metadata": '{"data": "OK"}',
        "callback_id": "callback_id",
        "external_id": "external_id",
    }


class TestView:
    def test(self, view_attributes, snapshot):
        snapshot.assert_match(MockView(**view_attributes))

    @pytest.mark.parametrize(
        "field, length",
        [("blocks", 100), ("private_metadata", 3000), ("callback_id", 255)],
    )
    def test_validate_length(self, view_attributes, field, length):
        view_attributes[field] = "x" * (length + 1)
        with pytest.raises(ValidationError):
            MockView(**view_attributes)

    def test_required_blocks(self, view_attributes):
        view_attributes["blocks"] = None
        with pytest.raises(ValidationError):
            MockView(**view_attributes)


class TestHomeTabs:
    def test(self, snapshot, view_attributes):
        snapshot.assert_match(HomeTabs(**view_attributes))


class TestModal:
    @pytest.fixture
    def attributes(self, view_attributes):
        return {
            "title": "title",
            "submit": "submit",
            "close": "close",
            "clear_on_close": True,
            "notify_on_close": False,
            **view_attributes,
        }

    def test(self, attributes, snapshot):
        snapshot.assert_match(Modal(**attributes))

    @pytest.mark.parametrize(
        "field, length", [("title", 24), ("submit", 24), ("close", 24)],
    )
    def test_validate_length(self, attributes, field, length):
        attributes[field] = "x" * (length + 1)
        with pytest.raises(ValidationError):
            Modal(**attributes)

    def test_required_title(self, attributes):
        attributes["title"] = None
        with pytest.raises(ValidationError):
            Modal(**attributes)
