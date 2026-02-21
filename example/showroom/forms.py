from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout, Submit
from django import forms


class Form1(forms.Form):
    name = forms.CharField(label='Name')
    email = forms.EmailField(label='Email')
    select = forms.ChoiceField(choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')])
    multi_select = forms.MultipleChoiceField(
        label='Multi-select',
        choices=[('1', 'Option One'), ('2', 'Option Two'), ('3', 'Option Three')],
        initial=['2'],
        help_text='Hold Ctrl/Cmd to select multiple options',
    )
    multi_select_no_initial = forms.MultipleChoiceField(
        label='Multi-select (no initial)',
        choices=[('a', 'Alpha'), ('b', 'Beta'), ('c', 'Gamma')],
        required=False,
        help_text='Optional field, no pre-selected values',
    )
    checkbox = forms.BooleanField(label='Checkbox')
    remember_me = forms.BooleanField(
        label='toggle field',
        widget=forms.CheckboxInput(attrs={'class': 'toggle'}),
    )
    radio = forms.ChoiceField(choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')], widget=forms.RadioSelect)
    textarea = forms.CharField(label='Textarea', widget=forms.Textarea)
    date = forms.DateField(label='Date', widget=forms.DateInput(attrs={'type': 'date'}))
    datetime = forms.DateTimeField(label='Datetime', widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    time = forms.TimeField(label='Time', widget=forms.TimeInput(attrs={'type': 'time'}))
    file = forms.FileField(label='File')
    image = forms.ImageField(label='Image')
    nullable_bool = forms.NullBooleanField(label='Nullable Bool')
    disabled_select = forms.ChoiceField(
        label='Disabled Select',
        choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')],
        initial='2',
        disabled=True,
    )
    disabled_text = forms.CharField(label='Disabled Text', initial='Read only', disabled=True)


class Form2(forms.Form):
    """Form using Field layout with css_class to demonstrate custom styling."""

    select = forms.ChoiceField(
        label='Styled Select',
        choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')],
    )
    checkbox = forms.BooleanField(label='Styled Checkbox', required=False)
    toggle = forms.BooleanField(
        label='Styled Toggle',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'toggle'}),
    )
    radio = forms.ChoiceField(
        label='Styled Radio',
        choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')],
        widget=forms.RadioSelect,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('select', css_class='select-primary'),
            Field('checkbox', css_class='checkbox-primary'),
            Field('toggle', css_class='toggle-primary'),
            Field('radio', css_class='radio-primary'),
            Submit('submit', 'Submit', css_class='w-full'),
        )
