# User functions
import email

def user_profile():
    username = 'bridgetsarah'
    password = 'null'
    email = 'post@devbk.me'
    website = 'http://www.devbk.me'
    return (username, email, website)


profile_data = user_profile()
print (user_profile())

# User profile / CRUD settings

def user_settings():
    create = 'create'                                         # Creates new user
    read = 'read'                                             # Reads userprofile
    update = 'update'                                         # Updates userprofile
    delete = 'delete'                                         # Deletes userprofile
    return (create, read, update, delete)

crudsettings = (user_settings())
print (user_settings())