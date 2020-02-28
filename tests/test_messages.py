from blockkit.messages import *


class TestMessage:
    def test(self, snapshot):
        snapshot.assert_match(Message(blocks=[{"block_id": "1"}]))
