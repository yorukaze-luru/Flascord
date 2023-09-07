
# Flascord: Discord OAuth2 Integration for Flask

Flascord is a Python library that simplifies the integration of Discord OAuth2 authentication into your Flask web applications.

## Installation

You can easily install Flascord using pip:

``` bash
pip install flascord
```

## Usage

1. Import the necessary classes from the library:

```python
from flascord import DiscordOauth2Session
```

2. Set up the required configuration in your Flask app:

```python
app.config['DISCORD_CLIENT_ID'] = 'your_client_id'
app.config['DISCORD_CLIENT_SECRET'] = 'your_client_secret'
app.config['DISCORD_REDIRECT_URI'] = 'your_redirect_uri'
app.config['DISCORD_BOT_TOKEN'] = 'your_bot_token'
```

3. Initialize the ` DiscordOauth2Session` instance:

```python
discord_oauth = DiscordOauth2Session(app)
```

4. Implement the necessary routes for OAuth2 authorization:

```python
@app.route("/login")
def login():
    return discord_oauth.login()

@app.route("/refresh")
def refresh():
    return discord_oauth.refresh()
    
@app.route("/callback/")
def callback():
    discord_oauth.callback()
    return redirect(url_for(".success"))

@app.route("/success")
def success():
    return "success"
```

## Contributing

If you encounter any issues or would like to contribute, please feel free to open an issue or pull request on the [GitHub repository](https://github.com/yorukaze-luru/Flascord).

## License

Flascord is released under the [MIT License](LICENSE).
```
