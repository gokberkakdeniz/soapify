import spotipy
import soapify.auth

class Gatherer():
    def __init__(self, username, client_id, client_secret):
        if username == None or client_id == None or client_secret == None:
            raise Exception("Username, Client ID and Client Secret are required!")
        
        self.username = username
        token = soapify.auth.get_token(username=username,
                                client_id=client_id, 
                                client_secret=client_secret, 
                                redirect_uri="http://localhost:1337",
                                scope="playlist-read-private")
        if token == None:
            raise Exception("Could not get token!")
        self.sp = spotipy.Spotify(auth=token)

    def get_own_playlists(self):
        return [playlist for playlist in self.sp.current_user_playlists()["items"] if playlist["owner"]["id"] == self.username]

    def get_tracks(self, playlist):
        track_list=[]
                    
        results = self.sp.user_playlist(self.username, playlist['id'], fields="tracks,next")['tracks']

        while True:
            for item in results["items"]:
                track_list.append({"artist": item['track']['artists'][0]['name'], "name": item['track']['name']})
            if not results["next"]: 
                break
            results = self.sp.next(results)
        return track_list
