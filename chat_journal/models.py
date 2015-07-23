from django.db import models
from django.utils.functional import Promise
from django.utils.encoding import force_text
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.models import User

class Post(models.Model):
    body = models.TextField()
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)

    def as_json(self):
        return dict(pk=self.id, body=self.body, date=self.date.isoformat())
