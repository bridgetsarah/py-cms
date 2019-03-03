# Model Schema of post


model = ('model')
user = ('user')
category = ('category')
status = ('status')

class post():
    status = (
        (1, "Needs Edit"),
        (2, "Needs Approval"),
        (3, "Publised"),
        (4, "Archived"),
    )

    title = model.title()
    slug = model.slugField()
    category = model.ForiegnKey (category)
    author = model.author.ForiegnKey (user)
    status = model.status
    created = model.created
    modified = model.modified

print(status)  