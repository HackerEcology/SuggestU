# from django.db import models
from mongoengine import *

class User(Document):
    # search history
    #keywords = ListField(EmbeddedDocumentField(Keyword))
    keywords = ListField()
    # user's collection
    collection = ListField()
    # history metadata
    user_id = StringField(max_length=200)
    last_search = DateTimeField(help_text='last searched')
    meta = {
        'indexes': [
            'user_id',
            ('last_search', '+user_id')
        ]
    }
