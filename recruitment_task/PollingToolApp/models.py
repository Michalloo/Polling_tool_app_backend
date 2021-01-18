from django.db import models


class Response(models.Model):
    answer = models.CharField(max_length=150)


def return_answer(self):
    return self.answer
