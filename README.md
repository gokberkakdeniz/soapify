# soapify - search on all spotify playlists
    λ py soap.py "Blue Foundation" --where artist
    > G1
    Blue Foundation - Shine
    > mutlak huzur
    > 404.genre_not_found.err
    > icrievrytiem
    Blue Foundation - Bonfires
    Blue Foundation - As I Moved On
    ...

## installation
    pip install soapify

## requirements
- python3
    - click
    - spotipy
## usage
    λ soapify --help
    -Usage: soapify [OPTIONS] TEXT

    Filter your all Spotify playlists

    Options:
    -w, --where [artist|song|both]  Where to filter
    -u, --username TEXT             Spotify username
    -id, --client-id TEXT           Spotify API client id
    -secret, --client-secret TEXT   Spotify client secret
    --help                          Show this message and exit.

Note: `--username`, `--client-id`, and `--client-secret` are not required if environment variables (`SPOTIFY_USERNAME`, `SPOTIFY_CLIENT_ID`, and `SPOTIFY_CLIENT_SECRET`) are defined.