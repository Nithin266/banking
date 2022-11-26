# from django import forms
# from django.core.validators import RegexValidator
#
# GENDER_CHOICES = (
#         (1, ('Male')),
#         (2, ('Female')),
#     )
# MRL_CHOICES = (
# (1, 'Debit Card'),
# (2, 'Credit Card'),
# (3, 'Cheque Book'),)
# class Valueform(forms.Form):
#     name = forms.CharField(max_length = 100)
#     gender = forms.ModelMultipleChoiceField(
#                                       choices = GENDER_CHOICES,
#                                       widget  = forms.CheckboxSelectMultiple(),
#                                       label   = 'Search')
#     phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
#     phone = forms.CharField(validators=[phone_regex], max_length=17)
#     district = forms.ChoiceField(choices = (('1','Trivandrum'),('2','Kollam'),('3','Pathanamthitta'),('4','Alappuzha'),('5','Kottayam'),
#                                           ('6','Idukki'),('7','Ernakulam'),('8','Thrissur'),('9','Palakkad'),('10','Malappuram'),('11','Kozhikkode'),
#                                           ('12','Wayanad'),('13','Kannur'),('14','Kasargod')))
#     branches = forms.ChoiceField(choices = (('1','Padmanabhapuram'),('2','Shanmugham'),('3','Krishnapuram'),('4','Thangasheri'),('5','Adoor'),
#                                           ('6','Cherthala'),('7','Munnar'),('8','Aluva'),('9','Edappally'),('10','Guruvayur'),('11','Tirur'),
#                                           ('12','Manjeri'),('13','Mananchira'),('14','Thamarasseri'),('14','Kalpetta'),('14','Mananthavady')
#                                         ,('14','Thalassery'),('14','Koothuparamba'),('14','Manjesuaram')))
#     account_type= forms.ChoiceField(choices = (('1','Saving'),('2','Current'),('3','NRI'),('4','Fixed'),('5','Demat')))
#     ngo = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
#                                 choices=MRL_CHOICES)
