from django import forms

class Form1(forms.Form):
    name = forms.CharField(label='Name')
    email = forms.EmailField(label='Email')
    select = forms.ChoiceField(choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')])
    multi_select = forms.MultipleChoiceField(
        label='Multi-select',
        choices=[('1', 'Option One'), ('2', 'Option Two'), ('3', 'Option Three')],
        initial=['2'],
        help_text='Hold Ctrl/Cmd to select multiple options'
    )
    multi_select_no_initial = forms.MultipleChoiceField(
        label='Multi-select (no initial)',
        choices=[('a', 'Alpha'), ('b', 'Beta'), ('c', 'Gamma')],
        required=False,
        help_text='Optional field, no pre-selected values'
    )
    checkbox = forms.BooleanField(label='Checkbox')
    remember_me = forms.BooleanField(
        label='toggle field',
        widget=forms.CheckboxInput(attrs={'class': 'toggle'})
    )
    radio = forms.ChoiceField(choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')], widget=forms.RadioSelect)
    textarea = forms.CharField(label='Textarea', widget=forms.Textarea)
    date = forms.DateField(label='Date')
    datetime = forms.DateTimeField(label='Datetime')
    time = forms.TimeField(label='Time')
    file = forms.FileField(label='File')
    image = forms.ImageField(label='Image')

