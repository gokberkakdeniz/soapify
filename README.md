# soapify - search on all spotify playlists
[![asciicast](https://asciinema.org/a/kGK0UooHleh4KBWPhvYalyEd0.svg)](https://asciinema.org/a/kGK0UooHleh4KBWPhvYalyEd0)

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

Note: `--username`, `--client-id`, and `--client-secret` are not required if environment variables (`SPOTIPY_USERNAME`, `SPOTIPY_CLIENT_ID`, and `SPOTIPY_CLIENT_SECRET`) are defined.