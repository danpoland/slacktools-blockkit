import pytest

from blockkit import elements
from blockkit.blocks import *
from blockkit.exceptions import ValidationError
from blockkit.objects import Option, PlainText


class MockBlock(Block):
    block_type = "block_type"


class MockElement(elements.Element):
    element_type = "test"


class MockInput(Input):
    element_class = elements.PlainTextInput


class TestBlock:
    def test(self, snapshot):
        snapshot.assert_match(MockBlock(block_id="block_id", extra="value"))

    def test_validate_block_id(self):
        with pytest.raises(ValidationError):
            block_id = "x" * 256
            MockBlock(block_id=block_id)


class TestActions:
    def test(self, snapshot):
        snapshot.assert_match(Actions(block_id="block_id", elements=[MockElement()]))

    def test_validate_elements(self):
        with pytest.raises(ValidationError):
            Actions(elements=[MockElement() for i in range(6)])

    def test_elements_required(self):
        with pytest.raises(ValidationError):
            Actions(elements=None)


class TestContext:
    def test(self, snapshot):
        snapshot.assert_match(
            Context(block_id="block_id", elements=[PlainText("text")])
        )

    def test_validate_elements(self):
        with pytest.raises(ValidationError):
            Context(elements=[PlainText(str(i)) for i in range(11)])

    def test_elements_required(self):
        with pytest.raises(ValidationError):
            Context(elements=None)


class TestDivider:
    def test(self, snapshot):
        snapshot.assert_match(Divider(block_id="block_id"))


class TestFile:
    def test(self, snapshot):
        snapshot.assert_match(File(block_id="block_id", external_id="xid"))

    def test_invalid_source(self):
        with pytest.raises(ValidationError):
            File(block_id="block_id", external_id="xid", source="remotes")

    def test_external_id(self):
        with pytest.raises(ValidationError):
            File(external_id=None)


class TestImage:
    @pytest.fixture
    def attributes(self):
        return {
            "block_id": "block_id",
            "image_url": "https://image.url",
            "alt_text": "alt_text",
            "title": "title",
        }

    def test(self, attributes, snapshot):
        snapshot.assert_match(Image(**attributes))

    @pytest.mark.parametrize(
        "field, length", [("image_url", 3000), ("alt_text", 2000), ("title", 2000)]
    )
    def test_validate_length(self, attributes, field, length):
        attributes[field] = "x" * (length + 1)
        with pytest.raises(ValidationError):
            Image(**attributes)

    def test_image_url_required(self):
        with pytest.raises(ValidationError):
            Image(image_url=None, alt_text="alt_text")

    def test_alt_text_required(self):
        with pytest.raises(ValidationError):
            Image(image_url="http://crispy.dev", alt_text=None)


class TestSection:
    @pytest.fixture
    def attributes(self):
        return {
            "block_id": "block_id",
            "text_object": PlainText("text"),
            "accessory": MockElement(),
        }

    def test_text_object(self, attributes, snapshot):
        snapshot.assert_match(Section(**attributes))

    def test_fields(self, attributes, snapshot):
        del attributes["text_object"]
        attributes["fields"] = [PlainText("text")]
        snapshot.assert_match(Section(**attributes))

    def test_missing_text_object_or_fields(self, attributes):
        del attributes["text_object"]
        with pytest.raises(ValidationError):
            Section(**attributes)

    def test_validate_text_object(self, attributes):
        attributes["text_object"]["text"] = "x" * 3001
        with pytest.raises(ValidationError):
            Section(**attributes)

    def test_validate_fields(self, attributes):
        del attributes["text_object"]
        attributes["fields"] = [PlainText(str(i)) for i in range(11)]
        with pytest.raises(ValidationError):
            Section(**attributes)


@pytest.fixture
def input_attributes():
    return {
        "block_id": "block_id",
        "action_id": "action_id",
        "label": "label",
        "optional": True,
        "hint": "hint",
    }


class TestInput:
    def test(self, input_attributes, snapshot):
        snapshot.assert_match(MockInput(**input_attributes))

    @pytest.mark.parametrize("field, length", [("label", 2000), ("hint", 2000)])
    def test_validate_length(self, input_attributes, field, length):
        input_attributes[field] = "x" * (length + 1)
        with pytest.raises(ValidationError):
            MockInput(**input_attributes)

    def test_label_required(self, input_attributes):
        input_attributes["label"] = None
        with pytest.raises(ValidationError):
            MockInput(**input_attributes)

    def test_parse(self, make_parse_block_args):
        assert MockInput.parse(**make_parse_block_args({"value": "value"})) == "value"

    def test_parse_raise_exception_true(self, make_parse_block_args):
        kwargs = make_parse_block_args("value")
        kwargs["action_id"] = "wrong_action"
        with pytest.raises(KeyError):
            MockInput.parse(**kwargs, raise_exception=True)

    def test_parse_raise_exception_false(self, make_parse_block_args):
        kwargs = make_parse_block_args("value")
        kwargs["action_id"] = "wrong_action"
        assert MockInput.parse(**kwargs) is None


class TestPlainTextInput:
    def test(self, snapshot, input_attributes):
        snapshot.assert_match(PlainTextInput(**input_attributes))


class TestDatepickerInput:
    def test(self, snapshot, input_attributes):
        snapshot.assert_match(DatepickerInput(**input_attributes))


@pytest.fixture
def select_input_attributes(input_attributes):
    input_attributes["placeholder"] = "placeholder"
    return input_attributes


class TestStaticSelectInput:
    def test(self, snapshot, select_input_attributes):
        select_input_attributes["options"] = [Option("option", "option")]
        snapshot.assert_match(StaticSelectInput(**select_input_attributes))


class TestConversationsSelectInput:
    def test(self, snapshot, select_input_attributes):
        snapshot.assert_match(ConversationsSelectInput(**select_input_attributes))


class TestUsersSelectInput:
    def test(self, snapshot, select_input_attributes):
        snapshot.assert_match(UsersSelectInput(**select_input_attributes))


class TestChannelSelectInput:
    def test(self, snapshot, select_input_attributes):
        snapshot.assert_match(ChannelSelectInput(**select_input_attributes))


class TestStaticMultiSelectInput:
    def test(self, snapshot, select_input_attributes):
        select_input_attributes["options"] = [Option("option", "option")]
        snapshot.assert_match(StaticMultiSelectInput(**select_input_attributes))


class TestConversationsMultiSelectInput:
    def test(self, snapshot, select_input_attributes):
        snapshot.assert_match(ConversationsMultiSelectInput(**select_input_attributes))


class TestUsersSelectMultiInput:
    def test(self, snapshot, select_input_attributes):
        snapshot.assert_match(UsersSelectMultiInput(**select_input_attributes))


class TestChannelMultiSelectInput:
    def test(self, snapshot, select_input_attributes):
        snapshot.assert_match(ChannelMultiSelectInput(**select_input_attributes))
