from django import forms
from tasks.models import Task,TaskDetail
# django Form
class TaskForm(forms.Form):
    title = forms.CharField(max_length=250)
    description = forms.CharField(widget=forms.Textarea,label='task-description')
    due_date = forms.DateField(widget=forms.SelectDateWidget,label='Due-Date')
    assigned_to =forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=[])

    def __init__(self,*args, **kwargs):
        employees = kwargs.pop('employees',[])
        print(employees)
        super().__init__(*args, **kwargs)
        self.fields['assigned_to'].choices=[(emp.id, emp.name) for emp in employees]


class StyleFormMixin:
    '''Mixing to apply style to form fields'''
    defaul_classes= 'border-2 border-gray-300 w-full p-3 focus: outline-none focus: border-rose-500 focus: ring-rose-500 rounded-lg shadow-sm'

    def apply_style_widgets(self):
        for field_name, field in self.fields.items():
            if isinstance(field.widget,forms.TextInput):
                print("inside input")
                field.widget.attrs.update(
                    {
                    'class': self.defaul_classes,
                    'placeholder':f'Enter {field.label.lower()}'
                }
                )
            elif isinstance(field.widget,forms.Textarea):
                print("inside textarea")
                field.widget.attrs.update({
                    'class':f"{self.defaul_classes} resize-none",
                    'placeholder':f'Enter {field.label.lower()}',
                    'rows':5 
                })

            elif isinstance(field.widget,forms.SelectDateWidget):
                print("inside date")
                field.widget.attrs.update({
                    'class':'border-2 border-gray-300   p-3 focus: outline-none focus: border-rose-500 focus: ring-rose-500 rounded-lg shadow-sm'
                })

            elif isinstance(field.widget,forms.CheckboxSelectMultiple):
                print("inside checkbox")
                field.widget.attrs.update({
                    'class':'space-y-2' 

                })
            else:
                print("inside else")
                field.widget.attrs.update({
                    'class':self.defaul_classes 

                })


# django Model form:
class TaskModelForm( StyleFormMixin,forms.ModelForm):
    class Meta:
        model =Task
        fields = ['title', 'description', 'due_date', 'assigned_to']
        # exclude =['project','is_completed','create_at','update_at']
        '''manual widget using'''
        widgets ={
            'due_date':forms.SelectDateWidget,
            'assigned_to': forms.CheckboxSelectMultiple
        }
        # widgets = {
        #     'title': forms.TextInput(attrs={
        #         'class':'border-2 border-gray-300 w-full p-3 focus: outline-none focus: border-rose-500 focus: ring-rose-500 rounded-lg shadow-sm',
        #         'placeholder':'Enter the task title'

        #     }),
        #     'description': forms.Textarea(attrs={
        #         'class':'border-2 border-gray-300 w-full p-3 focus: outline-none focus: border-rose-500 focus: ring-rose-500 rounded-lg shadow-sm',
        #         'placeholder':'Description the task area',
        #         'rows':5


        #     }),
        #     'due_date': forms.SelectDateWidget(attrs={
        #          'class':'border-2 border-gray-300   p-3 focus: outline-none focus: border-rose-500 focus: ring-rose-500 rounded-lg shadow-sm',
                 

        #     }),
        #     'assigned_to': forms.CheckboxSelectMultiple(attrs={
        #          'class':'space-y-2 '

        #     }
        #     )
        # }
    '''Mixin using'''
    def __init__(self, *args,**kwarg):
        super().__init__(*args, **kwarg)
        self.apply_style_widgets()

# taskdetails modele

class TaskDetailModelForm(StyleFormMixin,forms.ModelForm):
    class Meta:
       model =TaskDetail
       fields =['priority','notes']

    def __init__(self, *args,**kwarg):
        super().__init__(*args, **kwarg)
        self.apply_style_widgets()

    

