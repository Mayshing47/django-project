from django import forms
from .models import Hobby

class HobbyForm(forms.ModelForm):
    class Meta:
        model = Hobby
        fields = ['hobby']  # Removed 'name'

    def clean_hobby(self):
        hobby = self.cleaned_data.get("hobby")
        if len(hobby) < 3:
            raise forms.ValidationError("Hobby must be at least 3 characters long!")
        return hobby


# from django import forms # type: ignore
# from .models import Hobby

# # class HobbyForm(forms.Form):
# #     name = forms.CharField(label="Your Name", max_length=100)
# #     hobby = forms.CharField(label="Your Hobby", max_length=100)

# class HobbyForm(forms.ModelForm):
#     class Meta:
#         model = Hobby
#         fields = ['hobby']

#     # def clean_name(self):
#     #     name = self.cleaned_data.get("name")
       
#     #     return name
    
#     def clean_hobby(self):
#         hobby = self.cleaned_data.get("hobby")
#         if len(hobby) < 3:
#             raise forms.ValidationError("Hobby must be at least 3 characters long!")
#         return hobby

    # def clean_name(self):
    #     name = self.cleaned_data.get("name")
    #      # ✅ Check if the name already exists in the database
    #     if Hobby.objects.filter(name=name).exists():
    #         raise forms.ValidationError("This name is already used! Try another.")
    #     if len(name) < 3:
    #         raise forms.ValidationError("Name must be at least 3 characters long!")
    #     return name
    
