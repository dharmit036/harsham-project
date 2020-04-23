from django import forms
from .models import userdata
class userform(forms.ModelForm):
    class Meta(object):
        model=userdata
  #      fname=str(forms.CharField(label="Enter first name",max_length=50))
   #     lname=str(forms.CharField(label="Enter last name",max_length=50))
    #    email=str(forms.CharField(label="Enter email",max_length=50))
        fields=['firstname','lastname','email','mobile','carnumber','carmodel','lastservice','serviceintime','predictedtime']
        widgets={
                'firstname':forms.TextInput(
                     attrs={
                      'class':'form-control'
                    }),
                 'lastname':forms.TextInput(
                    attrs={
                     'class':'form-control'}),
                 'email':forms.TextInput(
                      attrs={ 
                       'class':'form-control' 
                    }),
                 'mobile':forms.TextInput(
                      attrs={ 
                       'class':'form-control' 
                    }),
                 'carnumber':forms.TextInput(
                      attrs={ 
                       'class':'form-control' 
                    }),
                 'carmodel':forms.TextInput(
                      attrs={ 
                       'class':'form-control' 
                    }),
 		'lastservice':forms.TextInput(
                      attrs={ 
                       'class':'form-control' 
                    }),
                'serviceintime':forms.TextInput(
                      attrs={ 
                       'class':'form-control' 
                    }),
                'predictedtime':forms.TextInput(
                      attrs={ 
                       'class':'form-control' 
                    }),
                
               }
