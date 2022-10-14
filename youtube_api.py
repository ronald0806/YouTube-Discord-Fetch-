from apiclient.discovery import build

API_KEY = 'AIzaSyCvxKwdX2AS5LCEUpRlfmxY77V_JQFL11E'

URL = 'https://www.googleapis.com/youtube/v3/videos?id=7lCDEYXw3mM&key=' +API_KEY + '&part=snippet,contentDetails,statistics,status'

youtube = build('youtube', 'v3', developerKey=API_KEY)


print(type(youtube))