from django import forms


class FeedbackFrom(forms.Form):
   Name = forms.CharField(label="Enter the Name",
                               widget= forms.TextInput(
                                   attrs={
                                       'class':'forms_control',
                                       'placeholder':'yourName'
                                   }
                               ))



   Rating = forms.CharField(label="Enter Rating",
                          widget=forms.NumberInput(
                              attrs={
                                  'class': 'forms_control',
                                  'placeholder': 'your Rating'
                              }
                          ))



   Location = forms.CharField(label="Enter Location",
                          widget=forms.TextInput(
                              attrs={
                                  'class': 'forms_control',
                                  'placeholder': 'your Loaction'
                              }
                          ))



   Feedback = forms.CharField(label="Enter Feedback",
                          widget=forms.TextInput(
                              attrs={
                                  'class': 'forms_control',
                                  'placeholder': 'yourFEEDBACK'
                              }
                          ))


