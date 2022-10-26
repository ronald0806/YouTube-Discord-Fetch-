def get_link(message):
    '''
    <a id="video-title" class="yt-simple-endpoint style-scope ytd-video-renderer" title="FBI Serves MyPillow CEO Mike Lindell With Search Warrant" aria-label="FBI Serves MyPillow CEO Mike Lindell With Search Warrant by MSNBC 20 hours ago 5 minutes, 34 seconds 175,607 views" href="/watch?v=umqKdAIpu-Q">
            <yt-icon id="inline-title-icon" class="style-scope ytd-video-renderer" hidden=""><!--css-build:shady--></yt-icon>
            <yt-formatted-string class="style-scope ytd-video-renderer" aria-label="FBI Serves MyPillow CEO Mike Lindell With Search Warrant by MSNBC 20 hours ago 5 minutes, 34 seconds 175,607 views">FBI Serves MyPillow CEO Mike Lindell With Search Warrant</yt-formatted-string>
          </a>   
    '''

    # download page
    # find this tag
    # format string youtube.com/href .. .
    # return that link