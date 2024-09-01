# crispy-daisyui

A [`daisyUI`](https://daisyui.com) template pack for the wonderful [django-crispy-forms](https://github.com/django-crispy-forms/django-crispy-forms).

This repository is a fork of [`crispy-tailwind`](https://github.com/django-crispy-forms/crispy-tailwind) and has been modified just enough to suit my needs.
It works well for the most common forms elements.

## How to install

Install via pip:

```bash
pip install crispy-daisyui
```

You will need to update your project's settings file to add ``crispy_forms``
and ``crispy_daisyui`` to your project's ``INSTALLED_APPS`` setting. Also set
``daisyui`` as an allowed template pack and as the default template pack
for your project:

```python
INSTALLED_APPS = (
    ...
    "crispy_forms",
    "crispy_daisyui",
    ...
)

CRISPY_ALLOWED_TEMPLATE_PACKS = "daisyui"
CRISPY_TEMPLATE_PACK = "daisyui"
```

## How to use

Current functionality allows the ``|crispy`` filter to be used to style your
form. In your template:

1. Load the filter: ``{% load daisyui_filters %}``
2. Apply the crispy filter: ``{{ form|crispy }}``

We can also use the ``{% crispy %}`` tag to allow usage of crispy-forms'
``FormHelper`` and ``Layout``. In your template:

1. Load the crispy tag: ``{% load crispy_forms_tags %}``
2. Add ``FormHelper`` to your form and use crispy-forms to set-up your form
3. Use the crispy tag ``{% crispy form %}`` in your template
