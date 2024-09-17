from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.TextField()

class Operations(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE, db_index=False)
    qty_change = models.PositiveIntegerField()
    data_created = models.DateField(auto_now_add=True)

class Authors(models.Model):
    first_name = models.TextField()
    middle_name = models.TextField(null=True)
    last_name = models.TextField()
    
class AuthorShips(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE, db_index=False)
    author = models.ForeignKey(Authors, on_delete=models.CASCADE, db_index=False)
    # seq_num is sorting order if one author repeates
    seq_num = models.PositiveIntegerField()