# Model Schema of post


model = ('model')
user = ('user')
post = ('post')
category = ('category')
status = ('status')


title = model.title()
slug = model.slugField()
category = model.ForiegnKey (category)
author = model.author.ForiegnKey (user)
status = model.status
created = model.created
modified = model.modified


# Post functions

def post_functions():
    class post_functions():
        post.function.title = title ('title')                     # Title of post
        post.function.slug = slug ('slug')                        # Slug of post
        post.function.category = category ('category')            # Category of post
        post.function.author = author ('')                        # Author of post
        post.function.status = status ('')                        # Status of post
        post.function.created = created ('')                      # Created post date
        post.function.modified = modified ('')                    # Post last modified
        return (text)
        print(post_functions)







    #class post_functions_status(status,):
    #post.function.status.edit = ('edit')
    #post.function.status.approval = ('approval')
    #post.function.status.published = ('published')
    #post.function.status.archived = ('archived')
    #return post_functions_status
    #print(post_functions_status)