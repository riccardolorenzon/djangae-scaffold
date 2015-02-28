from django.db import models
import scaffold.settings as settings

def PredictLanguage(message):
  return "English"

def GetSentiment(message):
    """
    TODO return true or false based on a predictive analysis using Google Prediction API
    :param message:
    :return:
    """
    return True

class BlogArticle(models.Model):
    title = models.CharField(max_length=60)
    text = models.TextField()
    blog_content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    sentiment = models.BooleanField()

    class Meta:
        get_latest_by = "created_on"
        ordering = ["-created_on"]

    def __unicode__(self):
        return self.title

    def setSentiment(self):
        self.sentiment = GetSentiment(self.blog_content)

class ImageBlogArticle(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    image = models.ImageField(upload_to='./')
    blogarticle = models.ForeignKey(BlogArticle)

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    user = models.CharField(max_length=50)
    name = models.CharField(max_length=42)
    email = models.EmailField(max_length=75)
    website = models.URLField(max_length=200, null=True, blank=True)
    text = models.TextField()
    content = models.TextField()
    blogarticles = models.ForeignKey(BlogArticle)

    def __unicode__(self):
        return self.text