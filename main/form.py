from django import forms

class CreateNewList(forms.Form):
    
    name = forms.CharField(label = "Name", max_length = 200)
    # label is optional, label is the name that will get placed as a name of the field(blank field which need to be filled) in the webpage

    # if we don't pass label, then it will get the name of the (field specified for database, example - check field)
    # require = False, make the checkbox field to be ticked optional
    check = forms.BooleanField(required = False)
    # check = forms.BooleanField(label = "check")


## Not of any use, don't know why it is not working or why we cannot use simple forms for creating items in the todolist 
# class NewItem(forms.Form):
#     item = forms.CharField(max_length = 300)
#     check = forms.BooleanField(required = False)