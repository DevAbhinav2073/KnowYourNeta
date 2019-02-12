USER_TYPE_POLITICIAN = 'Politician'
USER_TYPE_SUPPORTER = 'Supporter'

USER_TYPE_CHOICES_TUPLE = (
    (USER_TYPE_POLITICIAN, USER_TYPE_POLITICIAN),
    (USER_TYPE_SUPPORTER, USER_TYPE_SUPPORTER)
)

BOOLEAN_CHOICES = (
    (1, 'Yes'),
    (0, 'No')
)

SOCIAL_MEDIA_INFORMATION_STATUS = (
    ('Basic', 'बेसिक'),
    ('Expert', 'एक्सपर्ट')
)

WRITING_RESEARCH_SKILLS_CHOICES_TUPLE = (
    ('Self', 'Self'),
    ('Agencies', 'Agencies'),
)

SPEAKING_PRESENTATION_SKILLS_CHOICES_TUPLE = (
    ('Poor', 'Poor'),
    ('Good', 'Good'),
    ('Best', 'Best'),
)

EDUCATION_CHOICES_TUPLE = (
    (None, 'None'),
    ('<=10', ''),
    ('12', ''),
    ('Bachelor', ''),
    ('Masters', ''),
    ('Degree', ''),
)

INCOME_SOURCE_CHOICES = (
    ('Student', 'Student'),
    ('Private service class', 'Private service class'),
    ('Government service class', 'Government service class'),
    ('Business class', 'Business class'),
    ('Professional', 'Professional'),
    ('Retired', 'Retired'),

)
