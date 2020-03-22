# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots['TestFixedButton.test_fixed 1'] = {
    'action_id': 'test_action',
    'confirm': {
        'confirm': {
            'text': 'confirm',
            'type': 'plain_text'
        },
        'deny': {
            'text': 'deny',
            'type': 'plain_text'
        },
        'text': {
            'text': 'text',
            'type': 'plain_text'
        },
        'title': {
            'text': 'title',
            'type': 'plain_text'
        }
    },
    'text': {
        'text': 'text',
        'type': 'plain_text'
    },
    'type': 'button',
    'url': 'http://crispy.dev',
    'value': 'value'
}

snapshots['TestFixedButton.test_override[action_id-override] 1'] = {
    'action_id': 'override',
    'confirm': {
        'confirm': {
            'text': 'confirm',
            'type': 'plain_text'
        },
        'deny': {
            'text': 'deny',
            'type': 'plain_text'
        },
        'text': {
            'text': 'text',
            'type': 'plain_text'
        },
        'title': {
            'text': 'title',
            'type': 'plain_text'
        }
    },
    'text': {
        'text': 'text',
        'type': 'plain_text'
    },
    'type': 'button',
    'url': 'http://crispy.dev',
    'value': 'value'
}

snapshots['TestFixedButton.test_override[value-override] 1'] = {
    'action_id': 'test_action',
    'confirm': {
        'confirm': {
            'text': 'confirm',
            'type': 'plain_text'
        },
        'deny': {
            'text': 'deny',
            'type': 'plain_text'
        },
        'text': {
            'text': 'text',
            'type': 'plain_text'
        },
        'title': {
            'text': 'title',
            'type': 'plain_text'
        }
    },
    'text': {
        'text': 'text',
        'type': 'plain_text'
    },
    'type': 'button',
    'url': 'http://crispy.dev',
    'value': 'override'
}

snapshots['TestFixedButton.test_override[confirm-value2] 1'] = {
    'action_id': 'test_action',
    'confirm': {
        'confirm': {
            'text': 'confirm',
            'type': 'plain_text'
        },
        'deny': {
            'text': 'deny',
            'type': 'plain_text'
        },
        'text': {
            'text': 'override',
            'type': 'plain_text'
        },
        'title': {
            'text': 'override',
            'type': 'plain_text'
        }
    },
    'text': {
        'text': 'text',
        'type': 'plain_text'
    },
    'type': 'button',
    'url': 'http://crispy.dev',
    'value': 'value'
}

snapshots['TestFixedButton.test_override[text-override] 1'] = {
    'action_id': 'test_action',
    'confirm': {
        'confirm': {
            'text': 'confirm',
            'type': 'plain_text'
        },
        'deny': {
            'text': 'deny',
            'type': 'plain_text'
        },
        'text': {
            'text': 'text',
            'type': 'plain_text'
        },
        'title': {
            'text': 'title',
            'type': 'plain_text'
        }
    },
    'text': {
        'text': 'override',
        'type': 'plain_text'
    },
    'type': 'button',
    'url': 'http://crispy.dev',
    'value': 'value'
}

snapshots['TestFixedButton.test_override[style-Styles.DANGER] 1'] = {
    'action_id': 'test_action',
    'confirm': {
        'confirm': {
            'text': 'confirm',
            'type': 'plain_text'
        },
        'deny': {
            'text': 'deny',
            'type': 'plain_text'
        },
        'text': {
            'text': 'text',
            'type': 'plain_text'
        },
        'title': {
            'text': 'title',
            'type': 'plain_text'
        }
    },
    'style': 'danger',
    'text': {
        'text': 'text',
        'type': 'plain_text'
    },
    'type': 'button',
    'url': 'http://crispy.dev',
    'value': 'value'
}
