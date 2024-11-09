from django import forms
from land.models import RealEstate

class RealEstateForm(forms.Form):
    address=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    price=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
    property_type=forms.ChoiceField(choices=RealEstate.property_option,widget=forms.Select(attrs={"class":"form-control form-select"}))
    number_of_bedrooms=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
    square_footage=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
    location=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    property_image=forms.ImageField()
    contact_details=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

class RealEstateUpdateForm(forms.ModelForm):
    class Meta:
        model=RealEstate
        fields="__all__"