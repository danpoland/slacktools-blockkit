# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots['TestView.test 1'] = {
    'blocks': [
        {
            'text': 'text',
            'type': 'plain_text'
        }
    ],
    'callback_id': 'callback_id',
    'external_id': 'external_id',
    'private_metadata': '{"data": "OK"}',
    'type': 'test'
}

snapshots['TestModal.test 1'] = {
    'blocks': [
        {
            'text': 'text',
            'type': 'plain_text'
        }
    ],
    'callback_id': 'callback_id',
    'clear_on_close': True,
    'close': {
        'text': 'close',
        'type': 'plain_text'
    },
    'external_id': 'external_id',
    'notify_on_close': False,
    'private_metadata': '{"data": "OK"}',
    'submit': {
        'text': 'submit',
        'type': 'plain_text'
    },
    'title': {
        'text': 'title',
        'type': 'plain_text'
    },
    'type': 'modal'
}

snapshots['TestHomeTabs.test 1'] = {
    'blocks': [
        {
            'text': 'text',
            'type': 'plain_text'
        }
    ],
    'callback_id': 'callback_id',
    'external_id': 'external_id',
    'private_metadata': '{"data": "OK"}',
    'type': 'home'
}
