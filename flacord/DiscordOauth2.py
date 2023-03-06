from flacord import scope

class DiscordOauth2Session:
    def __init__(self, app):
        self.app = app
        self.base_url = 'https://discord.com/api/v9'


    def Login(self,scope=scope.all()):
        '%20'.join(scope)
