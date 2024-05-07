import re
from markmoji import handlers 


class SoundCloudHandler(handlers.MarkmojiHandler):
    """
    Handler for an embedded SoundCloud sound.

    ### Parameters
    label (str)
    :    Unused as embedded sounds don't have alt text

    link (str)
    :    Link to the sound to embed
    """
    # Rainy cloud emoji, as cloud would be too easily confused with cloud storage
    emoji = "🌧️"

    example = "🌧️<https://soundcloud.com/moondrift/edge>"
    __author__ = "🦊"

    @property
    def html(self):
        return f"<iframe src='https://w.soundcloud.com/player/?url={self.link}'{self.html_params}>"


class YouTubeHandler(handlers.MarkmojiHandler):
    """
    Handler for an embedded YouTube video.

    ### Parameters
    label (str)
    :    Alt text for the embedded video

    link (str)
    :    Link to the video to embed
    """
    # The ol' YouTube play button
    emoji = "▶️"

    example = "▶️[They're taking the hobbits to Isengard!](https://www.youtube.com/watch?v=jfKfPfyJRdk)"
    __author__ = "🦊"

    @property
    def html(self):
        # Get video ID from link
        match = re.match("^.*((youtu.be\/)|(v\/)|(\/u\/\w\/)|(embed\/)|(watch\?))\??v?=?([^#&?]*).*", self.link)
        if match:
            video_id = match.groups()[-1]
        else:
            video_id = self.link

        return f"<iframe src='https://www.youtube.com/embed/{video_id}' title='{self.label}' class='youtube-embed' allowfullscreen{self.html_params}></iframe>"