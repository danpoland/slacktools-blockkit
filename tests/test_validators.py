import pytest

from blockkit.validators import *


def test_validate_type_pass():
    validate_type("str", str)


def test_validate_type_failure():
    with pytest.raises(ValidationError):
        validate_type(1, str)


def test_validate_max_length_pass():
    validate_max_length([1], 1)


def test_validate_max_length_failure():
    with pytest.raises(ValidationError):
        validate_max_length([1, 2], 1)


def test_validate_min_length_pass():
    validate_min_length([1, 2], 2)


def test_validate_min_length_failure():
    with pytest.raises(ValidationError):
        validate_min_length([1], 2)


def test_validate_max_size_pass():
    validate_max_size(1, 1)


def test_validate_max_size_failure():
    with pytest.raises(ValidationError):
        validate_max_size(2, 1)


def test_validate_min_size_pass():
    validate_min_size(2, 2)


def test_validate_min_size_failure():
    with pytest.raises(ValidationError):
        validate_min_size(1, 2)


def test_validate_http_url_pass():
    validate_http_url("http://cripy.dev")


def test_validate_http_url_failure():
    with pytest.raises(ValidationError):
        validate_http_url("not a url")


def test_validate_date_pass():
    validate_date("2020-01-01")


def test_validate_date_failure():
    with pytest.raises(ValidationError):
        validate_date("01/01/2020")


def test_validate_choices_pass():
    validate_choices("test", ["test"])


def test_validate_choices_failure():
    with pytest.raises(ValidationError):
        validate_choices("test", ["choice"])
