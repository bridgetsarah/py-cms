# Menu Py (defining links / views)

# Main administration Menu

def menu():
    dashboard = '/dashboard'
    posts = '/posts'
    user ='/user'
    return (dashboard, posts, user)
menudata = (menu())    
print (menu())

# Sub menu for post options

def sub_menu_posts():
    create_post = 'create post'
    view_post = 'view post'
    update_post = 'update post'
    delete_post = 'delete post'
    return (create_post, view_post, update_post, delete_post)
sub_menu_data = (sub_menu_posts())   
print(sub_menu_posts())   

# Sub menu for user options

def sub_menu_user():
    create_user = 'create user'
    view_user = 'view user'
    update_user = 'update user'
    delete_user = 'delete user'
sub_menu_user_data = (sub_menu_user())
print(sub_menu_user())
