# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots['TestElement.test_success 1'] = {
    'type': 'test'
}

snapshots['TestButton.test 1'] = {
    'action_id': 'action_id',
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

snapshots['TestImage.test_success 1'] = {
    'alt_text': 'alt_text',
    'image_url': 'http://crispy.dev',
    'type': 'image'
}

snapshots['TestInput.test 1'] = {
    'action_id': 'action_id',
    'type': 'test_input'
}

snapshots['TestCheckboxes.test 1'] = {
    'action_id': 'action_id',
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
    'initial_options': [
        {
            'text': {
                'text': 'text',
                'type': 'plain_text'
            },
            'value': 'value'
        }
    ],
    'options': [
        {
            'text': {
                'text': 'text',
                'type': 'plain_text'
            },
            'value': 'value'
        }
    ],
    'type': 'checkboxes'
}

snapshots['TestDatePicker.test 1'] = {
    'action_id': 'action_id',
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
    'initial_date': '2020-01-01',
    'placeholder': {
        'text': 'placeholder',
        'type': 'plain_text'
    },
    'type': 'datepicker'
}

snapshots['TestPlainTextInput.test 1'] = {
    'action_id': 'action_id',
    'initial_value': 'initial_value',
    'max_length': 2,
    'min_length': 1,
    'multiline': True,
    'placeholder': {
        'text': 'placeholder',
        'type': 'plain_text'
    },
    'type': 'plain_text_input'
}

snapshots['TestOverflowMenu.test 1'] = {
    'action_id': 'action_id',
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
    'options': [
        {
            'text': {
                'text': 'text',
                'type': 'plain_text'
            },
            'value': 'value'
        },
        {
            'text': {
                'text': 'text',
                'type': 'plain_text'
            },
            'value': 'value'
        }
    ],
    'type': 'overflow'
}

snapshots['TestRadioButtonGroup.test 1'] = {
    'action_id': 'action_id',
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
    'initial_option': {
        'text': {
            'text': 'text',
            'type': 'plain_text'
        },
        'value': 'value'
    },
    'options': [
        {
            'text': {
                'text': 'text',
                'type': 'plain_text'
            },
            'value': 'value'
        },
        {
            'text': {
                'text': 'text',
                'type': 'plain_text'
            },
            'value': 'value'
        }
    ],
    'type': 'radio_buttons'
}

snapshots['TestSelect.test 1'] = {
    'action_id': 'action_id',
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
    'placeholder': {
        'text': 'placeholder',
        'type': 'plain_text'
    },
    'type': 'select'
}

snapshots['TestStaticSelect.test_options 1'] = {
    'action_id': 'action_id',
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
    'initial_option': {
        'text': {
            'text': 'text',
            'type': 'plain_text'
        },
        'value': 'value'
    },
    'options': [
        {
            'text': {
                'text': 'text',
                'type': 'plain_text'
            },
            'value': 'value'
        }
    ],
    'placeholder': {
        'text': 'placeholder',
        'type': 'plain_text'
    },
    'type': 'static_select'
}

snapshots['TestStaticSelect.test_option_groups 1'] = {
    'action_id': 'action_id',
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
    'initial_option': {
        'text': {
            'text': 'text',
            'type': 'plain_text'
        },
        'value': 'value'
    },
    'option_groups': [
        {
            'label': {
                'text': 'label',
                'type': 'plain_text'
            },
            'options': [
                {
                    'text': {
                        'text': 'text',
                        'type': 'plain_text'
                    },
                    'value': 'value'
                }
            ]
        }
    ],
    'placeholder': {
        'text': 'placeholder',
        'type': 'plain_text'
    },
    'type': 'static_select'
}

snapshots['TestConversationSelect.test 1'] = {
    'action_id': 'action_id',
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
    'initial_conversation': '1',
    'placeholder': {
        'text': 'placeholder',
        'type': 'plain_text'
    },
    'type': 'conversations_select'
}

snapshots['TestChannelSelect.test 1'] = {
    'action_id': 'action_id',
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
    'initial_channel': '1',
    'placeholder': {
        'text': 'placeholder',
        'type': 'plain_text'
    },
    'type': 'channels_select'
}

snapshots['TestUserSelect.test 1'] = {
    'action_id': 'action_id',
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
    'initial_user': '1',
    'placeholder': {
        'text': 'placeholder',
        'type': 'plain_text'
    },
    'type': 'users_select'
}

snapshots['TestMultiSelect.test 1'] = {
    'action_id': 'action_id',
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
    'max_selected_items': 2,
    'placeholder': {
        'text': 'placeholder',
        'type': 'plain_text'
    },
    'type': 'multiselect'
}

snapshots['TestStaticMultiSelect.test_options 1'] = {
    'action_id': 'action_id',
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
    'max_selected_items': 2,
    'options': [
        {
            'text': {
                'text': 'text',
                'type': 'plain_text'
            },
            'value': 'value'
        }
    ],
    'placeholder': {
        'text': 'placeholder',
        'type': 'plain_text'
    },
    'type': 'multi_static_select'
}

snapshots['TestStaticMultiSelect.test_option_groups 1'] = {
    'action_id': 'action_id',
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
    'max_selected_items': 2,
    'option_groups': [
        {
            'label': {
                'text': 'label',
                'type': 'plain_text'
            },
            'options': [
                {
                    'text': {
                        'text': 'text',
                        'type': 'plain_text'
                    },
                    'value': 'value'
                }
            ]
        }
    ],
    'placeholder': {
        'text': 'placeholder',
        'type': 'plain_text'
    },
    'type': 'multi_static_select'
}

snapshots['TestConversationMultiSelect.test 1'] = {
    'action_id': 'action_id',
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
    'initial_conversations': [
        '1',
        '2'
    ],
    'max_selected_items': 2,
    'placeholder': {
        'text': 'placeholder',
        'type': 'plain_text'
    },
    'type': 'multi_conversations_select'
}

snapshots['TestUserMultiSelect.test 1'] = {
    'action_id': 'action_id',
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
    'initial_users': [
        '1',
        '2'
    ],
    'max_selected_items': 2,
    'placeholder': {
        'text': 'placeholder',
        'type': 'plain_text'
    },
    'type': 'multi_users_select'
}

snapshots['TestChannelMultiSelect.test 1'] = {
    'action_id': 'action_id',
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
    'initial_channels': [
        '1',
        '2'
    ],
    'max_selected_items': 2,
    'placeholder': {
        'text': 'placeholder',
        'type': 'plain_text'
    },
    'type': 'multi_channels_select'
}
