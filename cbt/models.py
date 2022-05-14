from django.db import models
from users.models import Users
# Create your models here.


class Questions(models.Model):

    index = models.CharField(
        max_length=50,
        null=False,
        blank=False,
    )
    
    
    option1 = models.CharField(max_length=255, blank=False, null=False)
    option2 = models.CharField(max_length=255, blank=False, null=False)
    option3 = models.CharField(max_length=255, blank=True, null=True)
    option4 = models.CharField(max_length=255, blank=True, null=True)
    
    correct = models.CharField(max_length=128)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def getData(self):
        res = {
            "id":self.id,
            "index": self.index,
            "options": {
                "1": self.option1,
                "2": self.option2,
                "3": self.option3,
                "4": self.option4,
            }
        }
        return res
        #retur}n f"{self.firstname} {self.surname}" + ' ' + (f"{self.othername[0].upper()}.","")[self.othername is None]
    
    data = property(getData)
    
    def isCorrect(self, answer):
        return answer == self.correct
    
    def __str__(self):
        return f"Question {self.index}"


    class Meta:
        ordering = ('created_at')

    class Meta:
        db_table = "Questions"
        verbose_name = "Question"
        verbose_name_plural = "Questions"


class TestLogs(models.Model):
    user = models.ForeignKey(to=Users, on_delete=models.CASCADE)
    
    obtained = models.CharField(max_length=10, blank=False, null=False)
    max_obtainable = models.CharField(max_length=10, blank=False, null=False)
    data = models.TextField(blank=False, null=False)
    
    def calculatePercent(self):
        
        return round(int(self.obtained) / int(self.max_obtainable), 2)

    percent = property(calculatePercent)
    
    
    date_taken = models.DateTimeField(auto_now_add=True, auto_now=False)
    
    def convertToJSON(self,data):
        return data.replace("'",'"').replace('True','true').replace('False','false')
    
    def getLog(self):
        return {
            "data": self.convertToJSON(self.data),
            "obtained": self.obtained,
            "obtainable": self.max_obtainable,
            "percentage": self.percent
        }
    
    def __str__(self):
        return f"{self.user.matric_number} | {round(self.percent*100,1)}%"
    
    class Meta:
        db_table = "testlogs"
        verbose_name = "Test Log"
        verbose_name_plural = "Test Logs"
