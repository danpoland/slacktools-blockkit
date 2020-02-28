# slacktools-blockkit

slacktools-blockkit provides an expressive interface for utilizing the Slack Block-kit UI framework.

#### Features:
* Build Slack UIs by composing classes instead of manually constructing dictionaries.
* Easily parse action payloads and modal submission payloads without manual dictionary traversal.
* Compose your own reusable blocks with fixed attributes and avoid magic string lookups when parsing interactive payloads.

#### Installation:
`pip install slacktools-blockkit`

#### Basic Usage:
```python
from blockkit import Message, blocks, elements, objects

message = Message(blocks=[
    blocks.Section(objects.MrkdwnText("*User Information: ")),
    blocks.Divider(),
    blocks.Section(
        objects.PlainText("John Doe"), 
        fields=[
            objects.MrkdwnText("Address:\n"),
            objects.PlainText("123 Street, City, 11111"),
            objects.MrkdwnText("Phone: \n"),
            objects.PlainText("111-111-1111")
        ]
    ),
    blocks.Actions(elements=[
        elements.Button(
            action_id="delete", 
            text="Delete User", 
            style=elements.Button.Styles.DANGER
        )
    ])
])
```


Parsing action payloads:
```python
from blockkit import elements


value = elements.Button.parse_value(action_payload["actions"][0])

```

#### Basic view submission payload parsing:
Define the view:
```python
from blockkit import blocks, views, objects


modal = views.Modal(
    title="User Data",
    blocks=[
        blocks.Section(objects.PlainText("Enter user information:")),
        blocks.PlainTextInput(label="Username", block_id="user_data", action_id="username")
    ]
)
```
Parse the response:
```python
from blockkit import blocks


value = blocks.PlainTextInput.parse(
    view_payload, 
    block_id="user_data", 
    action_id="username"
)
```

### Fixed blocks and view submission payload parsing:
Define the fixed block and view:
```python
from blockkit import blocks, views, objects
from blockkit.fixed_blocks import FixedPlainTextInput


class UsernameInput(FixedPlainTextInput):
    block_id = "user_data"
    action_id = "username"
    label = "Username"


modal = views.Modal(
    title="User Data",
    blocks=[
        blocks.Section(objects.PlainText("Enter user information:")),
        UsernameInput()
    ]
)
```
Parse the response:
```python
value = UsernameInput.parse(view_payload)
```
