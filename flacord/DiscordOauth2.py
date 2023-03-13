from flacord import scope
from flask import request, session, redirect, current_app

class DiscordOauth2Session:
    def __init__(self, app):
        self.app = app
        self.base_url = 'https://discord.com/api/v9'
        self.oauth_url = self.base_url + '/oauth2/'
        self.get_token_url = self.oauth_url + '/token'

    def Login(self,scope=scope.all()):
        '%20'.join(scope)

    def callback():
        authorization_code = request.args.get("code")

        request_postdata = {'client_id': app.config['DISCORD_CLIENT_ID'], 'client_secret': app.config['DISCORD_CLIENT_SECRET'], 'grant_type': 'authorization_code', 'code': authorization_code, 'redirect_uri': app.config['DISCORD_REDIRECT_URI']}
        accesstoken_request = requests.post('https://discord.com/api/oauth2/token', data=request_postdata)

        responce_json = accesstoken_request.json()

        session['access_token'] = responce_json['access_token']
    
        return redirect(url_for(".loading"))
