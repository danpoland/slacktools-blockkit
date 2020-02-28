import pytest

from blockkit.elements import *
from blockkit.exceptions import ValidationError
from blockkit.objects import Option, OptionGroup


class MockElement(Element):
    element_type = "test"


class MockInput(Input):
    element_type = "test_input"


class MockSelect(Select):
    element_type = "select"


class MockMultiSelect(MultiSelect):
    element_type = "multiselect"


class TestElement:
    def test_success(self, snapshot):
        snapshot.assert_match(MockElement())


class TestButton:
    @pytest.fixture
    def attributes(self, make_confirm):
        return {
            "action_id": "action_id",
            "text": "text",
            "value": "value",
            "url": "http://crispy.dev",
            "confirm": make_confirm(),
            "style": Button.Styles.DANGER,
        }

    def test(self, snapshot, attributes):
        snapshot.assert_match(Button(**attributes))

    @pytest.mark.parametrize(
        "field, length",
        [("action_id", 255), ("text", 75), ("value", 2000), ("url", 3000)],
    )
    def test_validate_length(self, attributes, field, length):
        attributes[field] = "x" * (length + 1)
        with pytest.raises(ValidationError):
            Button(**attributes)

    @pytest.mark.parametrize("field", ["action_id", "text"])
    def test_required(self, attributes, field):
        attributes[field] = None
        with pytest.raises(ValidationError):
            Button(**attributes)


class TestImage:
    @pytest.fixture
    def attributes(self):
        return {"image_url": "http://crispy.dev", "alt_text": "alt_text"}

    def test_success(self, snapshot, attributes):
        snapshot.assert_match(Image(**attributes))

    @pytest.mark.parametrize("field", ["alt_text", "image_url"])
    def test_required(self, attributes, field):
        attributes[field] = None
        with pytest.raises(ValidationError):
            Image(**attributes)


class TestInput:
    def test(self, snapshot):
        snapshot.assert_match(MockInput(action_id="action_id"))

    def test_validate(self,):
        with pytest.raises(ValidationError):
            MockInput(action_id="x" * 256)

    def test_required_action_id(self):
        with pytest.raises(ValidationError):
            MockInput(action_id=None)

    def test_parse_valuer(self):
        assert MockInput.parse_value({"value": "value"}) == "value"


class TestCheckboxes:
    def test(self, snapshot, make_confirm):
        snapshot.assert_match(
            Checkboxes(
                action_id="action_id",
                options=[Option(text="text", value="value")],
                initial_options=[Option(text="text", value="value")],
                confirm=make_confirm(),
            )
        )

    def test_required_options(self):
        with pytest.raises(ValidationError):
            Checkboxes(action_id="action_id", options=None)

    def test_parse_value(self):
        assert Checkboxes.parse_value(
            {
                "selected_options": [
                    {
                        "text": {"type": "plain_text", "text": "1", "emoji": True},
                        "value": "1",
                    },
                    {
                        "text": {"type": "plain_text", "text": "3", "emoji": True},
                        "value": "3",
                    },
                ]
            }
        ) == ["1", "3"]


class TestDatePicker:
    def test(self, snapshot, make_confirm):
        snapshot.assert_match(
            DatePicker(
                action_id="action_id",
                placeholder="placeholder",
                initial_date="2020-01-01",
                confirm=make_confirm(),
            )
        )

    def test_parse_value(self):
        assert DatePicker.parse_value({"selected_date": "value"}) == "value"


class TestPlainTextInput:
    @pytest.fixture
    def attributes(self):
        return {
            "action_id": "action_id",
            "placeholder": "placeholder",
            "initial_value": "initial_value",
            "multiline": True,
            "min_length": 1,
            "max_length": 2,
        }

    def test(self, snapshot, attributes):
        snapshot.assert_match(PlainTextInput(**attributes))

    def test_validate_placeholder(self, attributes):
        with pytest.raises(ValidationError):
            attributes["placeholder"] = "x" * 151
            PlainTextInput(**attributes)

    def test_validate_min_length(self, attributes):
        with pytest.raises(ValidationError):
            attributes["min_length"] = 3001
            PlainTextInput(**attributes)

    def test_parse_value(self):
        assert PlainTextInput.parse_value({"value": "value"}) == "value"


class TestOverflowMenu:
    @pytest.fixture
    def attributes(self, make_confirm):
        return {
            "action_id": "action_id",
            "options": [
                Option(text="text", value="value"),
                Option(text="text", value="value"),
            ],
            "confirm": make_confirm(),
        }

    def test(self, snapshot, attributes):
        snapshot.assert_match(OverflowMenu(**attributes))

    def test_validate_options(self, attributes):
        with pytest.raises(ValidationError):
            attributes["options"] = [
                Option(text="text", value="value") for i in range(6)
            ]
            OverflowMenu(**attributes)

    @pytest.mark.parametrize("field", ["options"])
    def test_required(self, attributes, field):
        attributes[field] = None
        with pytest.raises(ValidationError):
            OverflowMenu(**attributes)

    def test_parse_value(self):
        assert (
            OverflowMenu.parse_value(
                {
                    "selected_option": {
                        "text": {"type": "plain_text", "text": "2", "emoji": True},
                        "value": "2",
                    }
                }
            )
            == "2"
        )


class TestRadioButtonGroup:
    @pytest.fixture
    def attributes(self, make_confirm):
        return {
            "action_id": "action_id",
            "options": [
                Option(text="text", value="value"),
                Option(text="text", value="value"),
            ],
            "initial_option": Option(text="text", value="value"),
            "confirm": make_confirm(),
        }

    def test(self, snapshot, attributes):
        snapshot.assert_match(RadioButtonGroup(**attributes))

    @pytest.mark.parametrize("field", ["options"])
    def test_required(self, attributes, field):
        attributes[field] = None
        with pytest.raises(ValidationError):
            RadioButtonGroup(**attributes)

    def test_parse_value(self):
        assert (
            RadioButtonGroup.parse_value(
                {
                    "selected_option": {
                        "text": {"type": "plain_text", "text": "3", "emoji": True},
                        "value": "3",
                    }
                }
            )
            == "3"
        )


@pytest.fixture
def select_attributes(make_confirm):
    return {
        "action_id": "action_id",
        "placeholder": "placeholder",
        "confirm": make_confirm(),
    }


class TestSelect:
    def test(self, snapshot, select_attributes):
        snapshot.assert_match(MockSelect(**select_attributes))

    def test_validate_placeholder(self, select_attributes):
        with pytest.raises(ValidationError):
            select_attributes["placeholder"] = "x" * 151
            MockSelect(**select_attributes)

    def test_required_placeholder(self, select_attributes):
        with pytest.raises(ValidationError):
            select_attributes["placeholder"] = None
            MockSelect(**select_attributes)


class TestStaticSelect:
    @pytest.fixture
    def attributes(self, make_confirm, select_attributes):
        return {
            **select_attributes,
            "initial_option": Option(text="text", value="value"),
        }

    def test_options(self, snapshot, attributes):
        attributes["options"] = [Option(text="text", value="value")]
        snapshot.assert_match(StaticSelect(**attributes))

    def test_option_groups(self, snapshot, attributes):
        attributes["option_groups"] = [
            OptionGroup(label="label", options=[Option(text="text", value="value")])
        ]
        snapshot.assert_match(StaticSelect(**attributes))

    def test_validate_options_or_options_group(self, attributes):
        attributes["options"] = [Option(text="text", value="value")]
        attributes["option_groups"] = [
            OptionGroup(label="label", options=[Option(text="text", value="value")])
        ]
        with pytest.raises(ValidationError):
            StaticSelect(**attributes)

    @pytest.mark.parametrize(
        "field, length", [("options", 100), ("option_groups", 100),],
    )
    def test_validate_length(self, attributes, field, length):
        attributes[field] = "x" * (length + 1)
        with pytest.raises(ValidationError):
            StaticSelect(**attributes)

    def test_parse_value(self):
        value = "option_1"
        assert StaticSelect.parse_value({"selected_option": {"value": value}}) == value

    def test_parse_value__nothing_selected(self):
        assert StaticSelect.parse_value({}) is None


class TestConversationSelect:
    def test(self, snapshot, select_attributes):
        snapshot.assert_match(
            ConversationSelect(initial_conversation="1", **select_attributes)
        )

    def test_parse_value(self):
        assert (
            ConversationSelect.parse_value({"selected_conversation": "value"})
            == "value"
        )


class TestChannelSelect:
    def test(self, snapshot, select_attributes):
        snapshot.assert_match(ChannelSelect(initial_channel="1", **select_attributes))

    def test_parse_value(self):
        assert ChannelSelect.parse_value({"selected_channel": "value"}) == "value"


class TestUserSelect:
    def test(self, snapshot, select_attributes):
        snapshot.assert_match(UserSelect(initial_user="1", **select_attributes))

    def test_parse_value(self):
        assert UserSelect.parse_value({"selected_user": "value"}) == "value"


@pytest.fixture
def multiselect_attributes(select_attributes):
    return {"max_selected_items": 2, **select_attributes}


class TestMultiSelect:
    def test(self, snapshot, multiselect_attributes):
        snapshot.assert_match(MockMultiSelect(**multiselect_attributes))

    def test_validate_max_selected_items(self, multiselect_attributes):
        with pytest.raises(ValidationError):
            multiselect_attributes["max_selected_items"] = 0
            MockMultiSelect(**multiselect_attributes)


class TestStaticMultiSelect:
    @pytest.fixture
    def attributes(self, make_confirm, multiselect_attributes):
        return {
            **multiselect_attributes,
            "initial_options": [Option(text="text", value="value")],
        }

    def test_options(self, snapshot, attributes):
        attributes["options"] = [Option(text="text", value="value")]
        snapshot.assert_match(StaticMultiSelect(**attributes))

    def test_option_groups(self, snapshot, attributes):
        attributes["option_groups"] = [
            OptionGroup(label="label", options=[Option(text="text", value="value")])
        ]
        snapshot.assert_match(StaticMultiSelect(**attributes))

    def test_validate_options_or_options_group(self, attributes):
        attributes["options"] = [Option(text="text", value="value")]
        attributes["option_groups"] = [
            OptionGroup(label="label", options=[Option(text="text", value="value")])
        ]
        with pytest.raises(ValidationError):
            StaticMultiSelect(**attributes)

    @pytest.mark.parametrize(
        "field, length", [("options", 100), ("option_groups", 100),],
    )
    def test_validate_length(self, attributes, field, length):
        attributes[field] = "x" * (length + 1)
        with pytest.raises(ValidationError):
            StaticMultiSelect(**attributes)

    def test_parse_value(self):
        # todo
        # assert StaticMultiSelect.parse_value({"selected_option": {"value": value}}) == value
        pass

    def test_parse_value__nothing_selected(self):
        # todo
        # assert StaticMultiSelect.parse_value({}) is None
        pass


class TestConversationMultiSelect:
    def test(self, snapshot, multiselect_attributes):
        snapshot.assert_match(
            ConversationMultiSelect(
                initial_conversations=["1", "2"], **multiselect_attributes
            )
        )

    def test_parse_value(self):
        assert ConversationMultiSelect.parse_value(
            {"selected_conversations": ["1", "2"]}
        ) == ["1", "2"]


class TestUserMultiSelect:
    def test(self, snapshot, multiselect_attributes):
        snapshot.assert_match(
            UserMultiSelect(initial_users=["1", "2"], **multiselect_attributes)
        )

    def test_parse_value(self):
        assert UserMultiSelect.parse_value({"selected_users": ["1", "2"]}) == ["1", "2"]


class TestChannelMultiSelect:
    def test(self, snapshot, multiselect_attributes):
        snapshot.assert_match(
            ChannelMultiSelect(initial_channels=["1", "2"], **multiselect_attributes)
        )

    def test_parse_value(self):
        assert ChannelMultiSelect.parse_value({"selected_channels": ["1", "2"]}) == [
            "1",
            "2",
        ]
