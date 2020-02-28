from blockkit.attributes import TextAttr
from blockkit.generics import *


class MockSlackObject(SlackObject):
    block_id = TextAttr()
    action_id = TextAttr(required=False)


class TestSlackObject:
    def test(self):
        obj = MockSlackObject(block_id="1", action_id=None)
        assert obj["block_id"] == "1"
        assert "action_id" not in obj.keys()

    def test_name(self):
        obj = MockSlackObject(block_id="1", action_id=None)
        assert obj._attributes["block_id"].name == "block_id"
