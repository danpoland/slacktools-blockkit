from blockkit.quick_blocks import *


class TestSimpleMrkdwnMessage:
    def test(self, snapshot):
        snapshot.assert_match(SimpleMrkdwnMessage("text"))


class TestMrkdwnTextSection:
    def test(self, snapshot):
        snapshot.assert_match(MrkdwnTextSection("text"))
