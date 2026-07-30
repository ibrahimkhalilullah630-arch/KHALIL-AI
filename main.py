from kivy.app import App
from kivy.lang import Builder
from ai import AI

Builder.load_file("design.kv")


class KhalilAI(App):

    def build(self):
        self.ai = AI()
        return Builder.load_file("design.kv")

    def send_message(self):
        message = self.root.ids.message.text.strip()

        if message == "":
            return

        reply = self.ai.reply(message)

        self.root.ids.chat.text += (
            f"\n\n👤 You: {message}\n🤖 AI: {reply}"
        )

        self.root.ids.message.text = ""


if __name__ == "__main__":
    KhalilAI().run()