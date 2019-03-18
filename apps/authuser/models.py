from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from apps.constants import USER_TYPE_CHOICES_TUPLE, BOOLEAN_CHOICES, SPEAKING_PRESENTATION_SKILLS_CHOICES_TUPLE, \
    WRITING_RESEARCH_SKILLS_CHOICES_TUPLE, SOCIAL_MEDIA_INFORMATION_STATUS, EDUCATION_CHOICES_TUPLE, \
    INCOME_SOURCE_CHOICES


class Authuser(AbstractUser):
    fathers_name = models.CharField(max_length=60, null=True)
    date_of_birth = models.DateField(null=True)
    address = models.CharField(max_length=100, null=True)
    party = models.ForeignKey('system.Party', on_delete=models.PROTECT, null=True)
    mobile_number = models.CharField(max_length=15, null=True)
    age = models.IntegerField(null=True)
    user_type = models.CharField(max_length=40, choices=USER_TYPE_CHOICES_TUPLE, null=True)
    constituency = models.ForeignKey('system.Constituency', on_delete=models.PROTECT, null=True)
    assembly_segment = models.ForeignKey('system.AssemblySegment', on_delete=models.CASCADE, blank=True, null=True)
    photo = models.ImageField(blank=True, null=True)


class PoliticianDetail(models.Model):
    detail_of = models.OneToOneField(Authuser, related_name='politician_detail', blank=False, on_delete=models.CASCADE)
    any_post = models.ForeignKey('system.Post', on_delete=models.PROTECT, blank=True, null=True)
    education = models.CharField(max_length=100, choices=EDUCATION_CHOICES_TUPLE,
                                 verbose_name='आप की शैक्षिक योय्गता :', null=True, blank=True)
    source_of_income = models.CharField(max_length=60, choices=INCOME_SOURCE_CHOICES,
                                        verbose_name='आय का जरिया  (Income Source)', blank=True, null=True)
    good_thoughts = models.TextField(verbose_name='३ अच्छे सोच *', blank=True, null=True)
    limitation = models.TextField(verbose_name='३ कमिया *', blank=True, null=True)
    how_can_you_help = models.TextField(verbose_name='आप कैसे मदत कर सकते है ………………….. को मजबूत करने में *', blank=True,
                                        null=True)
    why_people_like_you = models.TextField(verbose_name='आप ……………………. को क्यों पसंद करते है ? *', blank=True, null=True)
    is_politics_affected_by_social_media = models.BooleanField(choices=BOOLEAN_CHOICES,
                                                               verbose_name='क्या भारत की राजनीती में सोशल मीडिया की बहुत प्रभावी भूमिका रही है ? *',
                                                               blank=True, null=True)
    social_media_information = models.CharField(choices=SOCIAL_MEDIA_INFORMATION_STATUS, max_length=50, blank=True,
                                                null=True)
    number_of_people_influenced = models.IntegerField(
        verbose_name='आप के सोशल मिडिया पर कितने लोग आप की सोच से प्रभावित होते है *', blank=True, null=True)
    something_about_you = models.TextField(blank=True, null=True,
                                           verbose_name='आप के मन में है कुछ और तो लिखे apne बारे में')
    fb_id = models.URLField(null=True, blank=True)
    twitter_id = models.URLField(blank=True, null=True)
    instagram_id = models.URLField(blank=True, null=True)
    writter_description = models.TextField(verbose_name='क्या आप लेखक है ? तो ब्लॉग या वेब एड्रेस', blank=True,
                                           null=True)
    approx_supporter = models.IntegerField(blank=True, null=True)
    writing_research_skills = models.CharField(choices=WRITING_RESEARCH_SKILLS_CHOICES_TUPLE, max_length=50)
    public_speaking_and_presentation_skills = models.CharField(choices=SPEAKING_PRESENTATION_SKILLS_CHOICES_TUPLE,
                                                               max_length=50)
    knowledge_of_social_media = models.TextField(blank=True, null=True)
    understanding_your_audience = models.IntegerField(blank=True, null=True)
    crisis_management_problem_solving = models.TextField(blank=True, null=True)
    say_something_about_yourself = models.TextField(blank=True, null=True)


class Supporter(models.Model):
    supporter_of = models.ForeignKey(Authuser, on_delete=models.PROTECT)
    name = models.CharField(max_length=60)
    phone_number = models.CharField(max_length=15)
    constituency = models.ForeignKey('system.Constituency', on_delete=models.PROTECT, null=True)
    assembly_segment = models.ForeignKey('system.AssemblySegment', on_delete=models.PROTECT, null=True)
