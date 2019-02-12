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
    district = models.ForeignKey('system.District', on_delete=models.PROTECT, null=True)
    assembly_constituency_name = models.ForeignKey('system.AssemblyConstituencyName', on_delete=models.PROTECT,
                                                   null=True)
    user_type = models.CharField(max_length=40, choices=USER_TYPE_CHOICES_TUPLE, null=True)


class PoliticianDetail(models.Model):
    detail_of = models.ForeignKey(Authuser, blank=False, on_delete=models.CASCADE)
    any_post = models.CharField(max_length=50, blank=True, null=True)
    associate_with_party = models.ForeignKey('system.Party', on_delete=models.PROTECT)
    education = models.CharField(max_length=100, choices=EDUCATION_CHOICES_TUPLE,
                                 verbose_name='आप की शैक्षिक योय्गता : *', null=True)
    source_of_income = models.CharField(max_length=60, choices=INCOME_SOURCE_CHOICES,
                                        verbose_name='आय का जरिया  (Income Source)', blank=True, null=True)
    good_thoughts = models.TextField(verbose_name='३ अच्छे सोच *')
    limitation = models.TextField(verbose_name='३ कमिया *')
    how_can_you_help = models.TextField(verbose_name='आप कैसे मदत कर सकते है ………………….. को मजबूत करने में *')
    why_people_like_you = models.TextField(verbose_name='आप ……………………. को क्यों पसंद करते है ? *')
    is_politics_effected_by_social_media = models.BooleanField(choices=BOOLEAN_CHOICES,
                                                               verbose_name='क्या भारत की राजनीती में सोशल मीडिया की बहुत प्रभावी भूमिका रही है ? *')
    social_media_information = models.CharField(choices=SOCIAL_MEDIA_INFORMATION_STATUS, max_length=50)
    number_of_people_influenced = models.IntegerField(
        verbose_name='आप के सोशल मिडिया पर कितने लोग आप की सोच से प्रभावित होते है *')
    something_about_you = models.TextField(blank=True, null=True,
                                           verbose_name='आप के मन में है कुछ और तो लिखे apne बारे में')
    fb_id = models.URLField()
    twitter_id = models.URLField(blank=True, null=True)
    instagram_id = models.URLField(blank=True, null=True)
    writter_description = models.TextField(verbose_name='क्या आप लेखक है ? तो ब्लॉग या वेब एड्रेस', blank=True,
                                           null=True)
    approx_supporter = models.IntegerField()
    writing_research_skills = models.CharField(choices=WRITING_RESEARCH_SKILLS_CHOICES_TUPLE, max_length=50)
    public_speaking_and_presentation_skills = models.CharField(choices=SPEAKING_PRESENTATION_SKILLS_CHOICES_TUPLE,
                                                               max_length=50)
    knowledge_of_social_media = models.TextField(blank=True, null=True)
    understanding_your_audience = models.IntegerField(blank=True, null=True)
    crisis_management_problem_solving = models.TextField()
    say_something_about_yourself = models.TextField()


class Supporter(models.Model):
    supporter_of = models.ForeignKey(Authuser, on_delete=models.PROTECT)
    name = models.CharField(max_length=60)
    phone_number = models.CharField(max_length=15)
    constituency_name = models.ForeignKey('system.AssemblyConstituencyName', on_delete=models.PROTECT)
