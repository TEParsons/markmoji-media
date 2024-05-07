from markmoji.tests import BaseHandlerTests
from markmoji_media.handlers import SoundCloudHandler, YouTubeHandler


class TestSoundCloudHandler(BaseHandlerTests):
    handler = SoundCloudHandler


class TestYouTubeHandler(BaseHandlerTests):
    handler = YouTubeHandler
