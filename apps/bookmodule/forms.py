# books/forms.py
from django import forms
from .models import Book   ,Student, Address,Product
from .models import Student2, Address2

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'edition']

    

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'address']


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['city']

class Student2Form(forms.ModelForm):
    class Meta:
        model = Student2
        fields = ['name', 'age', 'addresses']
        widgets = {
            'addresses': forms.CheckboxSelectMultiple()
        }


class Address2Form(forms.ModelForm):
    class Meta:
        model = Address2
        fields = ['city']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'image']