from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
from django.db import models

#Model createas a database in your POSTGRESQL database
# Question table and Choice table inside the polls database.

class Question(models.Model): # Chapter-2 ADD THIS
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    #funny_column = models.CharField(max_length=10, null=True)

    def __str__(self): # Chapter-3 ADD THIS
            return self.question_text
 
    # def was_published_recently(self): # Chapter-3 ADD THIS
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def was_published_recently(self):  # Chapter-7 "Automated Testing" ADD THIS
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model): # Chapter-2 ADD THIS
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self): # Chapter-3 ADD THIS
        return self.choice_text
