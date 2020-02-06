from mongoengine import *


class Developer(Document):
    name = StringField()
    github_username: StringField()
    bio = StringField()
    avatar_url = StringField()
    techs = ListField(StringField())
