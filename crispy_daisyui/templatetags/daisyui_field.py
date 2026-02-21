import re
from typing import ClassVar

from crispy_forms.utils import TEMPLATE_PACK, get_template_pack
from django import forms, template
from django.conf import settings
from django.template import Context, loader

from crispy_daisyui.daisyui import CSSContainer

register = template.Library()


@register.filter
def is_checkbox(field):
    return isinstance(field.field.widget, forms.CheckboxInput)


@register.filter
def is_toggle(field):
    return isinstance(field.field.widget, forms.CheckboxInput) and 'toggle' in field.field.widget.attrs.get('class', '')


@register.filter
def is_radioselect(field):
    return isinstance(field.field.widget, forms.RadioSelect)


@register.filter
def is_select(field):
    return isinstance(field.field.widget, forms.Select)


@register.filter
def is_checkboxselectmultiple(field):
    return isinstance(field.field.widget, forms.CheckboxSelectMultiple)


@register.simple_tag
def widget_attrs_tag(field, base_class="", error_class=""):
    """
    Returns flattened HTML attributes for a widget, as a safe string.

    Merges the template's base CSS class with the widget's own class (deduplicated),
    adds error classes when the field has errors, and includes dynamic attributes
    like disabled from BoundField.build_widget_attrs.

    Usage: {% widget_attrs_tag field "select w-full" "select-error" %}
    """
    from django.forms.utils import flatatt

    attrs = dict(field.field.widget.attrs)
    attrs.update(field.build_widget_attrs({}, field.field.widget))
    classes = base_class.split() + attrs.get("class", "").split()
    if error_class and field.errors:
        classes += error_class.split()
    if classes:
        attrs["class"] = " ".join(dict.fromkeys(classes))
    return flatatt(attrs)


def pairwise(iterable):
    """s -> (s0,s1), (s2,s3), (s4, s5), ..."""
    a = iter(iterable)
    return zip(a, a)


class CrispyDaisyUiFieldNode(template.Node):
    base_input = "input w-full"

    default_styles: ClassVar[dict] = {
        "text": base_input,
        "number": base_input,
        "radioselect": "radio",
        "email": base_input,
        "url": base_input,
        "password": base_input,
        "hidden": "",
        "multiplehidden": "",
        "file": "file-input w-full",
        "clearablefile": "file-input w-full",
        "textarea": "w-full",
        "date": base_input,
        "datetime": base_input,
        "time": base_input,
        "checkbox": "checkbox",
        "select": "select w-full",
        "nullbooleanselect": "",
        "selectmultiple": "",
        "checkboxselectmultiple": "checkbox",
        "multi": "",
        "splitdatetime": base_input,
        "splithiddendatetime": "",
        "selectdate": "",
        "error_border": "border-red-500",
        "toggle": "toggle",
    }

    default_container = CSSContainer(default_styles)

    def __init__(self, field, attrs):
        self.field = field
        self.attrs = attrs
        self.html5_required = "html5_required"

    def render(self, context):
        # Nodes are not threadsafe so we must store and look up our instance
        # variables in the current rendering context first
        if self not in context.render_context:
            context.render_context[self] = (
                template.Variable(self.field),
                self.attrs,
                template.Variable(self.html5_required),
            )

        field, attrs, html5_required = context.render_context[self]
        field = field.resolve(context)
        try:
            html5_required = html5_required.resolve(context)
        except template.VariableDoesNotExist:
            html5_required = False

        # If template pack has been overridden in FormHelper we can pick it from context
        template_pack = context.get("template_pack", TEMPLATE_PACK)

        # There are special django widgets that wrap actual widgets,
        # such as forms.widgets.MultiWidget, admin.widgets.RelatedFieldWidgetWrapper
        widgets = getattr(field.field.widget, "widgets", [getattr(field.field.widget, "widget", field.field.widget)])

        if isinstance(attrs, dict):
            attrs = [attrs] * len(widgets)

        converters = {}
        converters.update(getattr(settings, "CRISPY_CLASS_CONVERTERS", {}))

        for widget, attr in zip(widgets, attrs):
            class_name = widget.__class__.__name__.lower()
            class_name = converters.get(class_name, class_name)
            css_class = widget.attrs.get("class", "")
            if css_class:
                if css_class.find(class_name) == -1:
                    css_class += f" {class_name}"
            else:
                css_class = class_name

            # Added additional code for Tailwind if class has not been passed in via the tag in the template
            if template_pack == "daisyui" and '"class"' not in attr:
                css_container = context.get("css_container", self.default_container)
                if css_container:
                    css = " " + css_container.get_input_class(field)
                    css_class += css
                if field.errors:
                    error_border_class = css_container.error_border
                    css_class = re.sub(r"border-\S+", error_border_class, css_class)

            widget.attrs["class"] = css_class

            # HTML5 required attribute
            if html5_required and field.field.required and "required" not in widget.attrs and field.field.widget.__class__.__name__ != "RadioSelect":
                widget.attrs["required"] = "required"

            # classes passed in via the template are added here
            for attribute_name, attribute in attr.items():
                attribute_name = template.Variable(attribute_name).resolve(context)

                if attribute_name in widget.attrs:
                    widget.attrs[attribute_name] += " " + template.Variable(attribute).resolve(context)
                else:
                    widget.attrs[attribute_name] = template.Variable(attribute).resolve(context)

        return str(field)


@register.tag(name="daisyui_field")
def daisyui_field(parser, token):
    """
    {% daisyui_field field attrs %}
    """
    token = token.split_contents()
    field = token.pop(1)
    attrs = {}

    # We need to pop tag name, or pairwise would fail
    token.pop(0)
    for attribute_name, value in pairwise(token):
        attrs[attribute_name] = value

    return CrispyDaisyUiFieldNode(field, attrs)


@register.simple_tag
def checkbox_label_after():
    return getattr(settings, "CRISPY_DAISYUI_CHECKBOX_LABEL_AFTER", True)


@register.simple_tag()
def crispy_addon(field, append="", prepend="", form_show_labels=True):
    """
    Renders a form field using bootstrap's prepended or appended text::

        {% crispy_addon form.my_field prepend="$" append=".00" %}

    You can also just prepend or append like so

        {% crispy_addon form.my_field prepend="$" %}
        {% crispy_addon form.my_field append=".00" %}
    """
    if field:
        context = Context({"field": field, "form_show_errors": True, "form_show_labels": form_show_labels})
        template = loader.get_template(f"{get_template_pack()}/layout/prepended_appended_text.html")
        context["crispy_prepended_text"] = prepend
        context["crispy_appended_text"] = append

        if not prepend and not append:
            raise TypeError("Expected a prepend and/or append argument")

        context = context.flatten()

    return template.render(context)
