from django.db import models
#from account.models import Genie_Users

# Create your models here.


class Subjects(models.Model):
    """
    subjects = (
        ('MTH', 'Mathematics'),
        ('ENG', 'English'),
        ('PHY', 'Physics'),
        ('CHEM', 'Chemistry'),
        ('BIO', 'Biology'),
    )
    """
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=30)
    date_added = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('date_added')

    class Meta:
        db_table = "Subjects_tb"
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"



class TestLogs(models.Model):
    #userid = models.ForeignKey(Genie_Users, on_delete=models.CASCADE)
    total_score_gotten = models.CharField(max_length=10, blank=True, null=True)
    total_max_score = models.CharField(max_length=10, blank=True, null=True)
    date_taken = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return str(self.date_taken)


    class Meta:
        ordering = ('date_taken')

    class Meta:
        db_table = "testLog_tb"
        verbose_name = "Test Log"
        verbose_name_plural = "Test Logs"


class TestScripts(models.Model):
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    data = models.TextField()
    score = models.CharField(max_length=50)
    max_score = models.CharField(max_length=50)
    
    log = models.ForeignKey(TestLogs, on_delete=models.CASCADE)

    def calculatePercent(self):
        sc = TestScripts.objects.get(log=self.log, subject=self.subject)
        
        return (int(sc.score) / int(sc.log.total_max_score))

    percent = property(calculatePercent)
    
    class Meta:
        db_table = "testScripts_tb"
        verbose_name = "Test Script"
        verbose_name_plural = "Test Scripts"


