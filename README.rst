===============
crispy-daisyui
===============

A `daisyUI`_ template pack for the wonderful django-crispy-forms_.

This repository is a fork of `crispy-daisyui`_ and has been modified just enough to suit my needs.
It works well for the most common forms elements.

**WARNING**

This project is still in its early stages of development. Any contributions to
the package would be very welcomed.

Currently the template pack allows the use of the ``|crispy`` filter to style
your form. Here is an example image.

How to install
--------------

Install via pip. ::

    pip install crispy-daisyui

You will need to update your project's settings file to add ``crispy_forms``
and ``crispy_daisyui`` to your project's ``INSTALLED_APPS`` setting. Also set
``daisyui`` as an allowed template pack and as the default template pack
for your project::

    INSTALLED_APPS = (
        ...
        "crispy_forms",
        "crispy_daisyui",
        ...
    )

    CRISPY_ALLOWED_TEMPLATE_PACKS = "daisyui"

    CRISPY_TEMPLATE_PACK = "daisyui"

How to use
----------

This project is still in its early stages.

Current functionality allows the ``|crispy`` filter to be used to style your
form. In your template:

1. Load the filter: ``{% load daisyui_filters %}``
2. Apply the crispy filter: ``{{ form|crispy }}``

We can also use the ``{% crispy %}`` tag to allow usage of crispy-forms'
``FormHelper`` and ``Layout``. In your template:

1. Load the crispy tag: ``{% load crispy_forms_tags %}``
2. Add ``FormHelper`` to your form and use crispy-forms to set-up your form
3. Use the crispy tag ``{% crispy form %}`` in your template

.. _daisyUI: https://daisyui.com
.. _crispy-tailwind: https://github.com/django-crispy-forms/crispy-tailwind
.. _django-crispy-forms: https://github.com/django-crispy-forms/django-crispy-forms