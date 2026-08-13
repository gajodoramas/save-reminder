"""

Save Reminder

Text-to-speech module: A wrapper around 'pyttsx3' lib to provide text-to-speech capabilities.
"""

# Standard imports
import pyttsx3


class TextToSpeech:
    """A wrapper around 'pyttsx3' lib to provide text-to-speech capabilities."""
    _MALE_VOICE_INDEX = 0
    _FEMALE_VOICE_INDEX = 1
    _RATE_PROPERTY_KEY = "rate"
    _VOLUME_PROPERTY_KEY = "volume"
    _VOICE_PROPERTY_KEY = "voice"
    _VOICES_PROPERTY_KEY = "voices"

    def __init__(self):
        self._engine = pyttsx3.init()

    def _set_voice(self, voice_id: str):
        self._engine.setProperty(self._VOICE_PROPERTY_KEY, voice_id)

    def _get_voice(self):
        return self._engine.getProperty(self._VOICE_PROPERTY_KEY)

    def _get_voices(self):
        return self._engine.getProperty(self._VOICES_PROPERTY_KEY)

    def _get_voices_ids(self):
        return [voice.id for voice in self._get_voices()]

    def play(self, text: str):
        """Convert text to speech and play it.

        Args:
            text (str): Text to convert to speech.
        """
        print(text)
        self._engine.say(text)
        self._engine.runAndWait()

    def set_rate(self, rate: int):
        """Set the voice rate.

        Args:
            rate (int): Speaking rate (typically 0–250).
        """
        self._engine.setProperty(self._RATE_PROPERTY_KEY, rate)

    def get_rate(self) -> int:
        """Get the current voice rate.

        Returns:
            int: Current speaking rate.
        """
        return self._engine.getProperty(self._RATE_PROPERTY_KEY)

    def set_volume(self, volume: float):
        """Set the audio volume.

        Args:
            volume (float): Volume level between 0.0 and 1.0.
        """
        self._engine.setProperty(self._VOLUME_PROPERTY_KEY, volume)

    def get_volume(self) -> float:
        """Get the current audio volume.

        Returns:
            float: Current volume level between 0.0 and 1.0.
        """
        return self._engine.getProperty(self._VOLUME_PROPERTY_KEY)

    def set_male_voice(self):
        """Select the male voice."""
        return self._set_voice(
            self._get_voices_ids()[self._MALE_VOICE_INDEX])

    def set_female_voice(self):
        """Select the female voice."""
        return self._set_voice(
            self._get_voices_ids()[self._FEMALE_VOICE_INDEX])
