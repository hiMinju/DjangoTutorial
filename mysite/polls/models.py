from django.db import models

# 1) models.py 파일에서 모델을 작성
# 2) makemigrations 명령어를 통해 변경 사항에 대한 migrations을 만듦
# 3) migrate 명령어를 통해 변경 사항을 DB에 적용

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    chocie_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.chocie_text