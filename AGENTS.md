# AGENTS.md

This file provides guidance to coding agents when working with code in this repository.

## Project Overview

crispy-daisyui is a DaisyUI template pack for Django Crispy Forms. It provides Tailwind CSS + DaisyUI styling for Django form rendering via the `|crispy` filter or `{% crispy %}` template tag.

## Development Commands

### Example / showroom demo app

The demo lives in `example/` (the Django project package inside it is named `showroom`).

```bash
cd example
make dev      # Run Tailwind watcher + Django server concurrently
make tw       # Watch Tailwind CSS compilation only (npx @tailwindcss/cli, static/input.css → static/output.css)
make django   # Run Django dev server only
```

Build the demo as a static site (the same command CI runs):

```bash
cd example
python manage.py build   # renders ShowroomView to example/build/index.html + copies static/
```

### Code Quality

Pre-commit hooks are configured for black, isort, and flake8:
```bash
pre-commit run --all-files
```

### Building & Publishing

Package metadata lives in `pyproject.toml` (setuptools backend; `crispy_daisyui/templates/**/*.html` is shipped via `[tool.setuptools.package-data]`). Publishing to PyPI happens automatically via `.github/workflows/publish.yml` when a release is created. `.github/workflows/pages.yml` builds `example/` on every push to `main` and deploys it to GitHub Pages.

## Architecture

### Core Package (`crispy_daisyui/`)

- **`daisyui.py`** - `CSSContainer` class managing DaisyUI CSS classes per widget type. Supports `+`/`-` operators for combining/removing classes.
- **`layout.py`** - Custom layout objects (`Submit`, `Reset`, `Button`, `Alert`) with default DaisyUI styling.
- **`templatetags/daisyui_filters.py`** - Template filters registered as `crispy`, `as_crispy_errors`, `as_crispy_field`, and `flatatt`.
- **`templatetags/daisyui_field.py`** - `CrispyDaisyUiFieldNode` and the `{% daisyui_field %}` tag for applying CSS classes to widgets, plus widget type detection filters (`is_checkbox`, `is_toggle`, `is_radioselect`, `is_select`, `is_checkboxselectmultiple`) and `crispy_addon`.
- **`templates/daisyui/`** - Templates for form/field rendering. `field.html` routes to the layout-specific templates in `templates/daisyui/layout/`.

### Example app (`example/`)

Demo Django app showcasing the template pack. Static-site generation is a plain management command (`showroom/management/commands/build.py`) that renders `ShowroomView` to `BUILD_DIR` and copies `static/` — django-bakery was removed in favour of this.
