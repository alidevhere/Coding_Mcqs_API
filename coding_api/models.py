from django.db import models

# Create your models here.

class Topics(models.Model):
    topic_id = models.AutoField(primary_key=True,)
    topic_name = models.CharField(max_length=100,unique=True)
    #total_mcq = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.topic_name}'

class MCQ(models.Model):
    mcq_id = models.AutoField(primary_key=True)
    topic_id = models.ForeignKey(Topics,on_delete=models.CASCADE)
    statement = models.CharField(max_length=256)
    options = models.CharField(max_length=256,default='default options')
    correct_ans = models.CharField(max_length=1,null=False)

    def __str__(self):
        return f'{self.statement}'
    


