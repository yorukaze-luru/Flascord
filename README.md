```markdown
# Flascord: Discord OAuth2 Integration for Flask

Flascord is a Python library that simplifies the integration of Discord OAuth2 authentication into your Flask web applications.

## Installation

You can easily install Flascord using pip:

```bash
pip install flascord
```

## Usage

1. Import the necessary classes from the library:

```python
from flascord import Flascord, login_required
```

2. Set up the required configuration in your Flask app:

```python
app.config['DISCORD_CLIENT_ID'] = 'your_client_id'
app.config['DISCORD_CLIENT_SECRET'] = 'your_client_secret'
app.config['DISCORD_REDIRECT_URI'] = 'your_redirect_uri'
```

3. Initialize the `Flascord` instance:

```python
flascord = Flascord(app)
```

4. Protect routes that require authentication using the `@login_required` decorator:

```python
@app.route('/profile')
@login_required
def profile():
    user_info = flascord.get_user_info()
    # Your code here to display the user's profile
```

5. Implement the necessary routes for OAuth2 authorization:

```python
@app.route('/login')
def login():
    return flascord.login()

@app.route('/logout')
def logout():
    return flascord.logout()

@app.route('/callback')
def callback():
    flascord.callback()
    return redirect(url_for('profile'))
```

## Contributing

If you encounter any issues or would like to contribute, please feel free to open an issue or pull request on the [GitHub repository](https://github.com/your-username/flascord).

## License

Flascord is released under the [MIT License](LICENSE).
```
