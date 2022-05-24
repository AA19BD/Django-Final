import sys
import os
sys.path.append(os.getcwd())
from utils.constants import JOURNAL_TYPE_BULLET
from django.db import models
from utils.constants import JOURNAL_TYPE


class BookJournalBase(models.Model):
    name=models.CharField(max_length=250,null=True,blank=True)
    price=models.IntegerField(default=0)
    description=models.TextField(null=True,blank=True)
    created_at=models.DateField(auto_now_add=True)

    class Meta:
        ordering=['-created_at']
        abstract=True

class Book(BookJournalBase):
    num_pages=models.IntegerField(default=0)
    genre=models.CharField(max_length=250,null=True,blank=True)

    class Meta:
        verbose_name='Book'
        verbose_name_plural="Books"

class Journal(BookJournalBase):
    type=models.SmallIntegerField(choices=JOURNAL_TYPE,default=JOURNAL_TYPE_BULLET)
    publisher=models.CharField(max_length=250,null=True,blank=True)

    class Meta:
        verbose_name = 'Journal'
        verbose_name_plural = "Journals"