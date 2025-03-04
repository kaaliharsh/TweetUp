from django.apps import AppConfig


class TweetupConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "TweetUp"
    
    
    
# follow/unfollow feature code

class YourAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'your_app_name'

    def ready(self):
        import your_app_name.signals

