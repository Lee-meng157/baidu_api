import time
from codelab_adapter_client import AdapterNode

class EIMNode(AdapterNode):
    NODE_ID = "eim"
    DESCRIPTION = "Everything Is a Message"
    HELP_URL = "https://adapter.codelab.club/extension_guide/eim/"

    def __init__(self):
        super().__init__()

    def send_message_to_scratch(self, content):
        message = self.message_template()
        message["payload"]["content"] = content
        self.publish(message)

        while self._running:
            time.sleep(1)
