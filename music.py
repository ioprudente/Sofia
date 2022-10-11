from netrc import netrc
import webbrowser as browser

def playlists(playlist):
    playlist  = 'https://open.spotify.com/track/2bw4WgXyXP90hIex7ur58y?si=cd18307f46504b6f'
    if playlist:
        browser.open(playlist)
    
    