-include .env
export

.PHONY: tw django dev

tw:
	npx @tailwindcss/cli -i static/input.css -o static/output.css --watch

django:
	python manage.py runserver

dev:
	make -j 2 tw django
