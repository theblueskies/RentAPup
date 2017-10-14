.PHONY:
	dev

# Runs identity with the most recent identity build
dev:
	ENVIRONMENT=dev python manage.py runserver

prod:
	git push heroku master
