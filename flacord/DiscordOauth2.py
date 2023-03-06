from flacord import scope

class DiscordOauth2Session:
    def __init__(self, app):
        self.app = app
        self.base_url = 'https://discord.com/api/v9'
        self.oauth_url = self.base_url + '/oauth2/'
        self.get_token_url = self.oauth_url + '/token'

    def Login(self,scope=scope.all()):
        '%20'.join(scope)
