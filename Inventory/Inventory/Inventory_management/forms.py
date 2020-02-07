from django import forms
from .models import *

# Forms here
class DesktopForm(forms.ModelForm):
	class Meta:
		model = Desktop
		fields = ('type', 'price', 'status', 'issues')
	pass

class LaptopForm(forms.ModelForm):
	class Meta:
		model = Laptop
		fields = ('type', 'price', 'status', 'issues')
	pass


class MobileForm(forms.ModelForm):
	class Meta:
		model = Mobile
		fields = ('type', 'price', 'status', 'issues')
	pass