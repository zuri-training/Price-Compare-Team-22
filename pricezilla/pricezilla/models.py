from django.db import models
from django.conf import settings



class Feedback(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    feedback = models.TextField(max_length = 200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    product =models.ForeignKey(product, on_delete=models.CASCADE)

    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Feedback {} by {}'.format(self.feedback, self.name)