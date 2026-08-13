"""

Save Reminder

Save reminder module: Plays an audio alert at defined intervals.
"""

# Standard imports
from time import sleep

# Local imports
from text_to_speech import TextToSpeech


class SaveReminder:
    """Plays an audio alert at defined intervals."""

    def __init__(self, message: str, reminder_interval: int, voice_rate: int=100, volume: int=1):
        self._tts = TextToSpeech()
        self._tts.set_rate(voice_rate)
        self._tts.set_volume(volume)
        self._message = message
        self._reminder_interval = reminder_interval

    def start(self):
        """Start the reminder loop, playing the message at defined interval."""
        self._tts.play("Reminder started.")
        while True:
            sleep(self._reminder_interval)
            self._tts.play(self._message)


if __name__ == "__main__":
    SaveReminder(
        "Save the game.",
        reminder_interval=300,
        voice_rate=150,
        volume=0.5
    ).start()
