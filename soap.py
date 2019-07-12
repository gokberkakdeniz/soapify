import spotipy
import click
import os
from lib.gatherer import Gatherer 

@click.command()
@click.argument("text",)
@click.option("--where", "-w", default="both", type=click.Choice(["artist", "song", "both"]), help="Where to filter")
@click.option("--username", "-u", default=os.environ.get("SPOTIFY_USERNAME"), help="Spotify username")
@click.option("--client-id", "-id", default=os.environ.get("SPOTIFY_CLIENT_ID"), help="Spotify API client id")
@click.option("--client-secret", "-secret", default=os.environ.get("SPOTIFY_CLIENT_SECRET"), help="Spotify client secret")
def main(text, where, username, client_id, client_secret):
    """Filter your all Spotify playlists"""
    try:
        gatherer = Gatherer(username, client_id, client_secret)
        for playlist in gatherer.get_own_playlists():
            print("> " + playlist["name"])
            for track in gatherer.get_tracks(playlist):
                info = track["artist"] + " - " + track["name"]
                if (where == "artist" and text in track["artist"]) or (where == "song" and text in track["name"]) or (where == "both" and text in info):
                    print(info)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()

    