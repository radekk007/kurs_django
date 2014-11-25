from django.db import models
from django.contrib.auth.models import User
from shelf.models import BookItem

#from datetime import datetime.now as now  # nie wspiera stref czasowych (ootb)
from django.utils.timezone import now  # wspiera strefy czasowe OotB


class Rental(models.Model):
    who = models.ForeignKey(User)
    what = models.ForeignKey(BookItem)
    when = models.DateTimeField(auto_now_add=True)  # domyślnie nie pojawi się w formularzu
    returned = models.DateTimeField(null=True, blank=True)    # pojawi się w formularzu z domyślną wartością

    def __str__(self):
        return '' # zadanie domowe :)

