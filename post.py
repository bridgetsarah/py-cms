# 
# Global Variables
title = 'title'                                                
slug = 'slug'                                                  
category = 'category'                                          
user = 'user'                                                  
status = 'status'                                              
created = 'created'                                           
modified = 'modified'                                           

#Post functions

def post():
    title = 'Goodbye Windows - Hello Linux!'                          # Title of post
    slug = 'Goodbye_windows_hello_linux'                              # Slug of post
    category = 'OS, Windows, Linux,'                                  # Category of post
    user = 'Bridgetsarah'                                             # Author of post
    status = 'Published'                                              # Status of post
    created = '01/02/2019'                                            # Created post date
    modified = '14/02/2019'                                           # Post last modified
    return(title, slug, category, user, status, created, modified)
post_data = post()                                         
print (post())

# Post Category (Dictionary?)