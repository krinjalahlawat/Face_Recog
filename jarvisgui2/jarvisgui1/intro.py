import vlc
import pafy
url="https://youtu.be/d1POcWLQAes"
video=pafy.new(url)
best=video.getbest()
playurl=best.url
instance=vlc.Instance()
player=instance.media_player_new()
media=instance.media_new(playurl)
media.get_mrl()
player.set_media(media)
player.play()