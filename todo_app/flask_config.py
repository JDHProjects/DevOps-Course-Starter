"""Flask configuration for app."""
import os

class Config:
    """Flask configuration for app."""
    def __init__(self):
        """Base configuration variables."""
        self.SECRET_KEY = os.environ.get('SECRET_KEY') # pylint: disable=invalid-name
        if not self.SECRET_KEY:
            raise ValueError("No SECRET_KEY set for Flask application."+
                             "Did you follow the setup instructions?")
