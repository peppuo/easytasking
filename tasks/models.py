from django.db import models
from django.contrib.auth.models import User
from django.db.models import F, Q


class Category(models.Model):
    cat_name = models.CharField(max_length=200)
    cat_description = models.TextField()
    cat_order = models.PositiveIntegerField()
    
    class Meta:
        ordering = ['cat_order', ]
    
    def __str__(self):
        return self.cat_name


class Importance(models.Model):
    imp_name = models.CharField(max_length=200)
    imp_description = models.TextField()
    imp_order = models.PositiveIntegerField()
    
    class Meta:
        ordering = ['imp_order', ]
    
    def __str__(self):
        return self.imp_name


class Status(models.Model):
    sta_name = models.CharField(max_length=200)
    sta_description = models.TextField()
    sta_order = models.PositiveIntegerField()

    class Meta:
        ordering = ['sta_order', ]

    def __str__(self):
        return self.sta_name


class Tasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tsk_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tsk_status = models.ForeignKey(Status, on_delete=models.CASCADE)
    tsk_importance = models.ForeignKey(Importance, on_delete=models.CASCADE)
    tsk_name = models.CharField(max_length=200)
    tsk_description = models.TextField()
    tsk_due_date = models.DateTimeField(blank=True, null=True)
    startdate = models.DateTimeField(blank=True, null=True)
    finishdate = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['tsk_due_date', ]
        constraints = [
            models.CheckConstraint(
                check=Q(startdate__lt=F('finishdate')),
                name='startdate_lt_finishdate',
            ),
        ]
    
    def __str__(self):
        return str((self.tsk_name, self.tsk_category, self.tsk_status))
