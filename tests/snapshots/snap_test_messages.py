# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots['TestMessage.test 1'] = {
    'blocks': [
        {
            'block_id': '1'
        }
    ]
}
