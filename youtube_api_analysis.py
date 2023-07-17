import googleapiclient.discovery

channel_id = "UCvp09smPddXC9470E2xjwpA"
api_key = "AIzaSyAdRSL1-ebLhsN2pZsVXgFGrtcBYlsQDKE"
api_service_name = "youtube"
api_version = "v3"
youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = api_key)

def get_playlist_id():
    request = youtube.channels().list(part="contentDetails", id=channel_id)
    response = request.execute()

    for item in response["items"]:
        playlist_id = item["contentDetails"]["relatedPlaylists"]["uploads"]
    return(playlist_id)

def get_video_ids(playlist_id):
    video_id_list = []
    request = youtube.playlistItems().list(part="contentDetails", playlistId=playlist_id)
    response = request.execute()
    
    for item in response["items"]:
        video_id = item["contentDetails"]["videoId"]
        video_id_list.append(video_id)
    return(video_id_list)

def get_video_details(video_id_list):
    for video_id in video_id_list:
        request = youtube.videos().list(part="snippet,contentDetails,statistics",id=video_id)
        response = request.execute()
        print(response)
        


if __name__ == "__main__":
    playlist_id = get_playlist_id()
    video_id_list = get_video_ids(playlist_id)
    get_video_details(video_id_list)
