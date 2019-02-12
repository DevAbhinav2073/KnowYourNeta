# Generated by Django 2.1.5 on 2019-02-11 11:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
        ('authuser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PoliticianDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('any_post', models.CharField(blank=True, max_length=50, null=True)),
                ('education', models.CharField(max_length=100, verbose_name='आप की शैक्षिक योय्गता : *')),
                ('good_thoughts', models.TextField(verbose_name='३ अच्छे सोच *')),
                ('limitation', models.TextField(verbose_name='३ कमिया *')),
                ('how_can_you_help', models.TextField(verbose_name='आप कैसे मदत कर सकते है ………………….. को मजबूत करने में *')),
                ('why_people_like_you', models.TextField(verbose_name='आप ……………………. को क्यों पसंद करते है ? *')),
                ('is_politics_effected_by_social_media', models.BooleanField(choices=[(1, 'Yes'), (0, 'No')], verbose_name='क्या भारत की राजनीती में सोशल मीडिया की बहुत प्रभावी भूमिका रही है ? *')),
                ('social_media_information', models.CharField(choices=[('Basic', 'बेसिक'), ('Expert', 'एक्सपर्ट')], max_length=50)),
                ('number_of_people_influenced', models.IntegerField(verbose_name='आप के सोशल मिडिया पर कितने लोग आप की सोच से प्रभावित होते है *')),
                ('something_about_you', models.TextField(blank=True, null=True, verbose_name='आप के मन में है कुछ और तो लिखे apne बारे में')),
                ('fb_id', models.URLField()),
                ('twitter_id', models.URLField(blank=True, null=True)),
                ('instagram_id', models.URLField(blank=True, null=True)),
                ('writter_description', models.TextField(blank=True, null=True, verbose_name='क्या आप लेखक है ? तो ब्लॉग या वेब एड्रेस')),
                ('approx_supporter', models.IntegerField()),
                ('writing_research_skills', models.CharField(choices=[('Self', 'Self'), ('Agencies', 'Agencies')], max_length=50)),
                ('public_speaking_and_presentation_skills', models.CharField(choices=[('Poor', 'Poor'), ('Good', 'Good'), ('Best', 'Best')], max_length=50)),
                ('knowledge_of_social_media', models.TextField(blank=True, null=True)),
                ('understanding_your_audience', models.IntegerField(blank=True, null=True)),
                ('crisis_management_problem_solving', models.TextField()),
                ('say_something_about_yourself', models.TextField()),
                ('associate_with_party', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='system.Party')),
                ('detail_of', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Supporter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('phone_number', models.CharField(max_length=15)),
                ('supporter_of', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]