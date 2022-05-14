from django.db import models

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
