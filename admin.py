# configuration for admin page
from pylint.checkers.strings import get_access_path


self = ('self')
dashboard  = ('dashboard')
posts  = ('posts')
users  = ('users')

# Common base for all links 
    
class menu:
    def __init__(self, dashboard, posts, users):
        self.dashboard = dashboard
        self.posts = posts
        self.users = users
        menu.__repr__

print(menu)

# Get latest Posts                  #Parse articles through in xml





