from blockkit.exceptions import BlockKitError


class TestBlockKitException:
    def test(self):
        e = BlockKitError("message")
        assert e.message == "message"
