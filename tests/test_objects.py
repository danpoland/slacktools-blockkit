import pytest

from blockkit.exceptions import ValidationError
from blockkit.objects import *


class TestPlainText:
    def test(self, snapshot):
        snapshot.assert_match(PlainText(text="text", emoji=True))

    def test_text_required(self):
        with pytest.raises(ValidationError):
            PlainText(text=None)


class TestMrkdwnText:
    def test(self, snapshot):
        snapshot.assert_match(MrkdwnText(text="*bold*", verbatim=True))

    def test_text_required(self):
        with pytest.raises(ValidationError):
            MrkdwnText(text=None)


class TestConfirmationDialog:
    @pytest.fixture
    def attributes(self):
        return {
            "title": "title",
            "text_object": PlainText("texts"),
            "confirm": "confirm",
            "deny": "deny",
        }

    def test(self, snapshot, attributes):
        snapshot.assert_match(ConfirmationDialog(**attributes))

    @pytest.mark.parametrize(
        "field, length", [("title", 100), ("confirm", 30), ("deny", 30)]
    )
    def test_validate_length(self, attributes, field, length):
        attributes[field] = "x" * (length + 1)
        with pytest.raises(ValidationError):
            ConfirmationDialog(**attributes)

    def test_validate_text_object(self, attributes):
        attributes["text_object"]["text"] = "x" * 301
        with pytest.raises(ValidationError):
            ConfirmationDialog(**attributes)

    @pytest.mark.parametrize("field", ["title", "confirm", "deny", "text_object"])
    def test_required(self, attributes, field):
        with pytest.raises(ValidationError):
            attributes[field] = None
            ConfirmationDialog(**attributes)


@pytest.fixture
def option_attributes():
    return {
        "text": "text",
        "value": "value",
        "description": "description",
        "url": "http://crispy.dev",
    }


class TestOption:
    def test(self, snapshot, option_attributes):
        snapshot.assert_match(Option(**option_attributes))

    @pytest.mark.parametrize(
        "field, length, value",
        [
            ("text", 75, None),
            ("value", 75, None),
            ("description", 75, None),
            ("url", 3000, f"http://{'c' * 3000}.dev"),
        ],
    )
    def test_validate_length(self, field, length, value, option_attributes):
        option_attributes[field] = "x" * (length + 1) if not value else value
        with pytest.raises(ValidationError):
            Option(**option_attributes)

    @pytest.mark.parametrize("field", ["text", "value"])
    def test_required(self, option_attributes, field):
        with pytest.raises(ValidationError):
            option_attributes[field] = None
            Option(**option_attributes)


class TestOptionGroup:
    @pytest.fixture
    def attributes(self, option_attributes):
        return {"label": "label", "options": [Option(**option_attributes)]}

    def test(self, snapshot, attributes):
        snapshot.assert_match(OptionGroup(**attributes))

    def test_validate_label(self, attributes):
        attributes["label"] = "x" * 76
        with pytest.raises(ValidationError):
            OptionGroup(**attributes)

    def test_validate_options(self, attributes, option_attributes):
        attributes["options"] = [Option(**option_attributes) for i in range(101)]
        with pytest.raises(ValidationError):
            OptionGroup(**attributes)

    @pytest.mark.parametrize("field", ["label", "options"])
    def test_required(self, attributes, field):
        attributes[field] = None
        with pytest.raises(ValidationError):
            OptionGroup(**attributes)
