# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots['TestPlainText.test 1'] = {
    'emoji': True,
    'text': 'text',
    'type': 'plain_text'
}

snapshots['TestMrkdwnText.test 1'] = {
    'text': '*bold*',
    'type': 'mrkdwn',
    'verbatim': True
}

snapshots['TestConfirmationDialog.test 1'] = {
    'confirm': {
        'text': 'confirm',
        'type': 'plain_text'
    },
    'deny': {
        'text': 'deny',
        'type': 'plain_text'
    },
    'text': {
        'text': 'texts',
        'type': 'plain_text'
    },
    'title': {
        'text': 'title',
        'type': 'plain_text'
    }
}

snapshots['TestOption.test 1'] = {
    'description': {
        'text': 'description',
        'type': 'plain_text'
    },
    'text': {
        'text': 'text',
        'type': 'plain_text'
    },
    'url': 'http://crispy.dev',
    'value': 'value'
}

snapshots['TestOptionGroup.test 1'] = {
    'label': {
        'text': 'label',
        'type': 'plain_text'
    },
    'options': [
        {
            'description': {
                'text': 'description',
                'type': 'plain_text'
            },
            'text': {
                'text': 'text',
                'type': 'plain_text'
            },
            'url': 'http://crispy.dev',
            'value': 'value'
        }
    ]
}
