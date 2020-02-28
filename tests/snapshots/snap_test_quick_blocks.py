# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots['TestSimpleMrkdwnMessage.test 1'] = {
    'blocks': [
        {
            'text': {
                'text': 'text',
                'type': 'mrkdwn'
            },
            'type': 'section'
        }
    ]
}

snapshots['TestMrkdwnTextSection.test 1'] = {
    'text': {
        'text': 'text',
        'type': 'mrkdwn'
    },
    'type': 'section'
}
