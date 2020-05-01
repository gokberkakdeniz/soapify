#!/usr/bin/env python3

import spotipy
import click
import os
from soapify.gatherer import Gatherer 

@click.command()
@click.argument("text",)
@click.option("--where", "-w", default="both", type=click.Choice(["artist", "song", "both"]), help="Where to filter")
@click.option("--username", "-u", default=os.environ.get("SPOTIPY_USERNAME"), help="Spotify username")
@click.option("--client-id", "-id", default=os.environ.get("SPOTIPY_CLIENT_ID"), help="Spotify API client id")
@click.option("--client-secret", "-secret", default=os.environ.get("SPOTIPY_CLIENT_SECRET"), help="Spotify client secret")
@click.option("--case-sensitive", "-C", is_flag=True, help="Case sensitive search")
def main(text, where, username, client_id, client_secret, case_sensitive):
    """Filter your all Spotify playlists
        
        
        Note: You may use SPOTIPY_USERNAME, SPOTIPY_CLIENT_ID and  SPOTIPY_CLIENT_SECRET environment variables.
    """
    try:
        gatherer = Gatherer(username, client_id, client_secret)
        for playlist in gatherer.get_own_playlists():
            print("> " + playlist["name"])
            for track in gatherer.get_tracks(playlist):
                artist = track["artist"].lower() if not case_sensitive else track["artist"]
                name = track["name"].lower() if not case_sensitive else track["name"]
                text = text.lower() if not case_sensitive else text
                info = track["artist"] + " - " + track["name"]
                if (where == "artist" and text in artist) or (where == "song" and text in name) or (where == "both" and text in (info if case_sensitive else info.lower())):
                    print(info)
    except Exception as e:
        print("ERROR: " + str(e))


if __name__ == "__main__":
    main()
