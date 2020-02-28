import pytest

from blockkit.attributes import *
from blockkit.exceptions import ValidationError


class MockAttribute(Attribute):
    def _validate(self, value):
        return value


class TestAttribute:
    def test_required_false(self):
        attr = MockAttribute(required=False)
        assert attr.validate(None) is None

    def test_required_true_success(self):
        attr = MockAttribute(required=True)
        value = "value"
        assert attr.validate(value) == value

    def test_required_true_failure(self):
        attr = MockAttribute(required=True)
        with pytest.raises(ValidationError):
            attr.validate(None)


class TestIntegerAttr:
    @pytest.fixture
    def attr(self):
        return IntegerAttr(max_size=3, min_size=2)

    def test_success(self, attr):
        assert attr.validate(2) == 2

    def test_max_size_failure(self, attr):
        with pytest.raises(ValidationError):
            attr.validate(4)

    def test_min_size_failure(self, attr):
        with pytest.raises(ValidationError):
            attr.validate(1)

    def test_type_failure(self, attr):
        with pytest.raises(ValidationError):
            attr.validate("1")


class TestBooleanAttr:
    def test_success(self):
        attr = BooleanAttr()
        assert attr.validate(True) is True

    def test_type_failure(self):
        attr = BooleanAttr()
        with pytest.raises(ValidationError):
            assert attr.validate("false")


class TestTextAttr:
    def test_success(self):
        attr = TextAttr(max_length=4, choices=["test"])
        assert attr.validate("test") == "test"

    def test_max_length_failure(self):
        attr = TextAttr(max_length=4)
        with pytest.raises(ValidationError):
            attr.validate("tests")

    def test_choices_failure(self):
        attr = TextAttr(max_length=4, choices=["test"])
        with pytest.raises(ValidationError):
            attr.validate("tes")

    def test_max_length_choices_failure(self):
        with pytest.raises(ValidationError):
            TextAttr(max_length=1, choices=["test"])

    def test_type_failure(self):
        attr = TextAttr()
        with pytest.raises(ValidationError):
            attr.validate(1)


class TestUrlAttr:
    def test_success(self):
        attr = UrlAttr()
        value = "http://crispy.dev"
        assert attr.validate(value) == value

    def test_failure(self):
        attr = UrlAttr()
        with pytest.raises(ValidationError):
            attr.validate("crispy.dev")


class TestPlainTextAttr:
    def test_success(self):
        attr = PlainTextAttr()
        value = {"text": "test", "type": "plain_text"}
        assert attr.validate(value) == value

    def test_failure(self):
        attr = PlainTextAttr()
        value = {"text": "test", "type": "mrkdwn"}
        with pytest.raises(ValidationError):
            attr.validate(value)


class TestMrkdwnTextAttr:
    def test_success(self):
        attr = MrkdwnTextAttr()
        value = {"text": "test", "type": "mrkdwn"}
        assert attr.validate(value) == value

    def test_failure(self):
        attr = MrkdwnTextAttr()
        value = {"text": "test", "type": "plain_text"}
        with pytest.raises(ValidationError):
            attr.validate(value)


class TestListAttr:
    @pytest.fixture
    def attr(self):
        return ListAttr(str, max_length=2, min_length=2)

    def test_success(self, attr):
        assert attr.validate(["test", "testing"]) == ["test", "testing"]

    def test_max_length_failure(self, attr):
        attr = ListAttr(max_length=4)
        with pytest.raises(ValidationError):
            attr.validate(["test", "testing", "tester"])

    def test_min_length_failure(self, attr):
        attr = ListAttr(max_length=4)
        with pytest.raises(ValidationError):
            attr.validate(["test"])

    def test_objects_types_failure(self, attr):
        with pytest.raises(ValidationError):
            attr.validate(["test", 1])

    def test_type_failure(self, attr):
        with pytest.raises(ValidationError):
            attr.validate(1)


class TestObjectAttr:
    def test_success(self):
        attr = ObjectAttr(str, int)
        assert attr.validate("test") == "test"
        assert attr.validate(1) == 1

    def test_failure(self):
        attr = ObjectAttr(str)
        with pytest.raises(ValidationError):
            attr.validate(1)


class TestDateAttr:
    def test_success(self):
        attr = DateAttr()
        assert attr.validate("2020-01-01") == "2020-01-01"

    def test_failure(self):
        attr = DateAttr()
        with pytest.raises(ValidationError):
            attr.validate("01/01/2020")
