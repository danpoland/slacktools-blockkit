# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots['TestFixedDatePickerInput.test_fixed 1'] = {
    'block_id': 'test_block',
    'element': {
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
        'initial_date': '2020-01-01',
        'placeholder': {
            'text': 'placeholder',
            'type': 'plain_text'
        },
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

snapshots['TestFixedStaticSelectInput.test_fixed 1'] = {
    'block_id': 'test_block',
    'element': {
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

snapshots['TestFixedPlainTextInput.test_fixed 1'] = {
    'block_id': 'test_block',
    'element': {
        'action_id': 'test_action',
        'initial_value': 'initial_value',
        'max_length': 20,
        'min_length': 1,
        'multiline': False,
        'placeholder': {
            'text': 'placeholder',
            'type': 'plain_text'
        },
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

snapshots['TestFixedPlainTextInput.test_override[initial_value-override] 1'] = {
    'block_id': 'test_block',
    'element': {
        'action_id': 'test_action',
        'initial_value': 'override',
        'max_length': 20,
        'min_length': 1,
        'multiline': False,
        'placeholder': {
            'text': 'placeholder',
            'type': 'plain_text'
        },
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

snapshots['TestFixedPlainTextInput.test_override[multiline-True] 1'] = {
    'block_id': 'test_block',
    'element': {
        'action_id': 'test_action',
        'initial_value': 'initial_value',
        'max_length': 20,
        'min_length': 1,
        'multiline': True,
        'placeholder': {
            'text': 'placeholder',
            'type': 'plain_text'
        },
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

snapshots['TestFixedPlainTextInput.test_override[min_length-2] 1'] = {
    'block_id': 'test_block',
    'element': {
        'action_id': 'test_action',
        'initial_value': 'initial_value',
        'max_length': 20,
        'min_length': 2,
        'multiline': False,
        'placeholder': {
            'text': 'placeholder',
            'type': 'plain_text'
        },
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

snapshots['TestFixedPlainTextInput.test_override[max_length-3] 1'] = {
    'block_id': 'test_block',
    'element': {
        'action_id': 'test_action',
        'initial_value': 'initial_value',
        'max_length': 3,
        'min_length': 1,
        'multiline': False,
        'placeholder': {
            'text': 'placeholder',
            'type': 'plain_text'
        },
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

snapshots['TestFixedPlainTextInput.test_override[placeholder-override] 1'] = {
    'block_id': 'test_block',
    'element': {
        'action_id': 'test_action',
        'initial_value': 'initial_value',
        'max_length': 20,
        'min_length': 1,
        'multiline': False,
        'placeholder': {
            'text': 'override',
            'type': 'plain_text'
        },
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

snapshots['TestFixedInputMixin.test_fixed 1'] = {
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

snapshots['TestFixedInputMixin.test_override 1'] = {
    'block_id': 'override',
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

snapshots['TestFixedDatePickerInput.test_override[placeholder-override] 1'] = {
    'block_id': 'test_block',
    'element': {
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
        'initial_date': '2020-01-01',
        'placeholder': {
            'text': 'override',
            'type': 'plain_text'
        },
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

snapshots['TestFixedDatePickerInput.test_override[initial_date-2019-01-01] 1'] = {
    'block_id': 'test_block',
    'element': {
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
        'initial_date': '2019-01-01',
        'placeholder': {
            'text': 'placeholder',
            'type': 'plain_text'
        },
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

snapshots['TestFixedDatePickerInput.test_override[confirm-value2] 1'] = {
    'block_id': 'test_block',
    'element': {
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
        'initial_date': '2020-01-01',
        'placeholder': {
            'text': 'placeholder',
            'type': 'plain_text'
        },
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

snapshots['TestFixedConversationsSelectInput.test_fixed 1'] = {
    'block_id': 'test_block',
    'element': {
        'action_id': 'test_action',
        'initial_conversation': '1',
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

snapshots['TestFixedStaticSelectInput.test_override[options-value0] 1'] = {
    'block_id': 'test_block',
    'element': {
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
                    'text': 'override',
                    'type': 'plain_text'
                },
                'value': 'override'
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

snapshots['TestFixedStaticSelectInput.test_override[initial_option-value1] 1'] = {
    'block_id': 'test_block',
    'element': {
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
        'initial_option': {
            'text': {
                'text': 'override',
                'type': 'plain_text'
            },
            'value': 'override'
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

snapshots['TestFixedStaticSelectInput.test_override[placeholder-override] 1'] = {
    'block_id': 'test_block',
    'element': {
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
            'text': 'override',
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

snapshots['TestFixedStaticSelectInput.test_override[confirm-value3] 1'] = {
    'block_id': 'test_block',
    'element': {
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

snapshots['TestFixedButton.test_fixed 1'] = {
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
    'style': 'primary',
    'text': {
        'text': 'text',
        'type': 'plain_text'
    },
    'type': 'button',
    'value': 'None'
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
    'style': 'primary',
    'text': {
        'text': 'text',
        'type': 'plain_text'
    },
    'type': 'button',
    'value': 'None'
}

snapshots['TestFixedButton.test_override[text-override] 1'] = {
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
    'style': 'primary',
    'text': {
        'text': 'override',
        'type': 'plain_text'
    },
    'type': 'button',
    'value': 'None'
}

snapshots['TestFixedButton.test_override[value-override] 1'] = {
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
    'style': 'primary',
    'text': {
        'text': 'text',
        'type': 'plain_text'
    },
    'type': 'button',
    'value': 'override'
}

snapshots['TestFixedButton.test_override[confirm-value5] 1'] = {
    'action_id': 'action_id',
    'confirm': {
        'confirm': {
            'text': 'override',
            'type': 'plain_text'
        },
        'deny': {
            'text': 'override',
            'type': 'plain_text'
        },
        'text': {
            'text': 'Override',
            'type': 'plain_text'
        },
        'title': {
            'text': 'override',
            'type': 'plain_text'
        }
    },
    'style': 'primary',
    'text': {
        'text': 'text',
        'type': 'plain_text'
    },
    'type': 'button',
    'value': 'None'
}

snapshots['TestFixedButton.test_override[style-Styles.DANGER] 1'] = {
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
    'value': 'None'
}

snapshots['TestFixedButton.test_override[url-http://crispy.override] 1'] = {
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
    'style': 'primary',
    'text': {
        'text': 'text',
        'type': 'plain_text'
    },
    'type': 'button',
    'url': 'http://crispy.override',
    'value': 'None'
}
