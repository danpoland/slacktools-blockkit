# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots['TestBlock.test 1'] = {
    'block_id': 'block_id',
    'type': 'block_type'
}

snapshots['TestActions.test 1'] = {
    'block_id': 'block_id',
    'elements': [
        {
            'type': 'test'
        }
    ],
    'type': 'actions'
}

snapshots['TestContext.test 1'] = {
    'block_id': 'block_id',
    'elements': [
        {
            'text': 'text',
            'type': 'plain_text'
        }
    ],
    'type': 'context'
}

snapshots['TestDivider.test 1'] = {
    'block_id': 'block_id',
    'type': 'divider'
}

snapshots['TestFile.test 1'] = {
    'block_id': 'block_id',
    'external_id': 'xid',
    'source': 'remote',
    'type': 'file'
}

snapshots['TestImage.test 1'] = {
    'alt_text': 'alt_text',
    'block_id': 'block_id',
    'image_url': 'https://image.url',
    'title': {
        'text': 'title',
        'type': 'plain_text'
    },
    'type': 'image'
}

snapshots['TestSection.test_text_object 1'] = {
    'accessory': {
        'type': 'test'
    },
    'block_id': 'block_id',
    'text': {
        'text': 'text',
        'type': 'plain_text'
    },
    'type': 'section'
}

snapshots['TestSection.test_fields 1'] = {
    'accessory': {
        'type': 'test'
    },
    'block_id': 'block_id',
    'fields': [
        {
            'text': 'text',
            'type': 'plain_text'
        }
    ],
    'type': 'section'
}

snapshots['TestDatepickerInput.test 1'] = {
    'block_id': 'block_id',
    'element': {
        'action_id': 'action_id',
        'type': 'datepicker'
    },
    'hint': {
        'text': 'hint',
        'type': 'plain_text'
    },
    'label': {
        'text': 'label',
        'type': 'plain_text'
    },
    'optional': True,
    'type': 'input'
}

snapshots['TestStaticSelectInput.test 1'] = {
    'block_id': 'block_id',
    'element': {
        'action_id': 'action_id',
        'options': [
            {
                'text': {
                    'text': 'option',
                    'type': 'plain_text'
                },
                'value': 'option'
            }
        ],
        'placeholder': {
            'text': 'placeholder',
            'type': 'plain_text'
        },
        'type': 'static_select'
    },
    'hint': {
        'text': 'hint',
        'type': 'plain_text'
    },
    'label': {
        'text': 'label',
        'type': 'plain_text'
    },
    'optional': True,
    'type': 'input'
}

snapshots['TestConversationsSelectInput.test 1'] = {
    'block_id': 'block_id',
    'element': {
        'action_id': 'action_id',
        'placeholder': {
            'text': 'placeholder',
            'type': 'plain_text'
        },
        'type': 'conversations_select'
    },
    'hint': {
        'text': 'hint',
        'type': 'plain_text'
    },
    'label': {
        'text': 'label',
        'type': 'plain_text'
    },
    'optional': True,
    'type': 'input'
}

snapshots['TestUsersSelectInput.test 1'] = {
    'block_id': 'block_id',
    'element': {
        'action_id': 'action_id',
        'placeholder': {
            'text': 'placeholder',
            'type': 'plain_text'
        },
        'type': 'users_select'
    },
    'hint': {
        'text': 'hint',
        'type': 'plain_text'
    },
    'label': {
        'text': 'label',
        'type': 'plain_text'
    },
    'optional': True,
    'type': 'input'
}

snapshots['TestChannelSelectInput.test 1'] = {
    'block_id': 'block_id',
    'element': {
        'action_id': 'action_id',
        'placeholder': {
            'text': 'placeholder',
            'type': 'plain_text'
        },
        'type': 'channels_select'
    },
    'hint': {
        'text': 'hint',
        'type': 'plain_text'
    },
    'label': {
        'text': 'label',
        'type': 'plain_text'
    },
    'optional': True,
    'type': 'input'
}

snapshots['TestConversationsMultiSelectInput.test 1'] = {
    'block_id': 'block_id',
    'element': {
        'action_id': 'action_id',
        'placeholder': {
            'text': 'placeholder',
            'type': 'plain_text'
        },
        'type': 'multi_conversations_select'
    },
    'hint': {
        'text': 'hint',
        'type': 'plain_text'
    },
    'label': {
        'text': 'label',
        'type': 'plain_text'
    },
    'optional': True,
    'type': 'input'
}

snapshots['TestUsersSelectMultiInput.test 1'] = {
    'block_id': 'block_id',
    'element': {
        'action_id': 'action_id',
        'placeholder': {
            'text': 'placeholder',
            'type': 'plain_text'
        },
        'type': 'multi_users_select'
    },
    'hint': {
        'text': 'hint',
        'type': 'plain_text'
    },
    'label': {
        'text': 'label',
        'type': 'plain_text'
    },
    'optional': True,
    'type': 'input'
}

snapshots['TestChannelMultiSelectInput.test 1'] = {
    'block_id': 'block_id',
    'element': {
        'action_id': 'action_id',
        'placeholder': {
            'text': 'placeholder',
            'type': 'plain_text'
        },
        'type': 'multi_channels_select'
    },
    'hint': {
        'text': 'hint',
        'type': 'plain_text'
    },
    'label': {
        'text': 'label',
        'type': 'plain_text'
    },
    'optional': True,
    'type': 'input'
}

snapshots['TestStaticMultiSelectInput.test 1'] = {
    'block_id': 'block_id',
    'element': {
        'action_id': 'action_id',
        'options': [
            {
                'text': {
                    'text': 'option',
                    'type': 'plain_text'
                },
                'value': 'option'
            }
        ],
        'placeholder': {
            'text': 'placeholder',
            'type': 'plain_text'
        },
        'type': 'multi_static_select'
    },
    'hint': {
        'text': 'hint',
        'type': 'plain_text'
    },
    'label': {
        'text': 'label',
        'type': 'plain_text'
    },
    'optional': True,
    'type': 'input'
}

snapshots['TestInput.test 1'] = {
    'block_id': 'block_id',
    'element': {
        'action_id': 'action_id',
        'multiline': False,
        'type': 'plain_text_input'
    },
    'hint': {
        'text': 'hint',
        'type': 'plain_text'
    },
    'label': {
        'text': 'label',
        'type': 'plain_text'
    },
    'optional': True,
    'type': 'input'
}

snapshots['TestPlainTextInput.test 1'] = {
    'block_id': 'block_id',
    'element': {
        'action_id': 'action_id',
        'multiline': False,
        'type': 'plain_text_input'
    },
    'hint': {
        'text': 'hint',
        'type': 'plain_text'
    },
    'label': {
        'text': 'label',
        'type': 'plain_text'
    },
    'optional': True,
    'type': 'input'
}
