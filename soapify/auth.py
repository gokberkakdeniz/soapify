import http.server
import spotipy.util
from spotipy.oauth2 import SpotifyOAuth
from urllib.parse import urlparse, parse_qs
from functools import partial
from multiprocessing.pool import ThreadPool
import webbrowser
from os import getenv

def get_token(username, client_id, client_secret, redirect_uri, scope):
    sp_oauth = SpotifyOAuth(username=username,
                            client_id=client_id, 
                            client_secret=client_secret, 
                            redirect_uri=redirect_uri,
                            scope=scope,
                            cache_path=getenv("HOME") + "/.cache/soapify-"+username)

    token_info = sp_oauth.get_cached_token()
    token = None
    if not token_info:
        auth_url = sp_oauth.get_authorize_url()
        webbrowser.open(auth_url)
        pool = ThreadPool(processes=1)
        code = pool.apply_async(CallbackServer).get().get_token()
        token_info = sp_oauth.get_access_token(code)
    if token_info:
        token = token_info['access_token']
    return token

class CallbackServer():
    port = 1337
    code = None
    handles = True
    
    class HTTPHandler(http.server.BaseHTTPRequestHandler):
        def __init__(self, request, client_address, server, outer):
            self.outer = outer
            return super().__init__(request, client_address, server)

        def log_request(self, code): 
            pass

        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            query = urlparse(self.path).query
            code = parse_qs(query).get("code")
            self.outer.code = code[0] if not code == None else ""
            self.wfile.write(bytes("Authorization successful. You can close this window.", "utf-8"))
    
    def __init__(self):
        httpd = http.server.HTTPServer(("", self.port), partial(self.HTTPHandler, outer=self))
        httpd.handle_request()

    def get_token(self):
        return self.code

