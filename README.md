# Bracket Voter
Submit 64 items of some topic, get them ranked by others, see composites

## Project Info
Built using:
* Python and FastAPI web framework
* PostgreSQL DB
* SQLAlchemy 2.0 ORM using async sessions
* Jinja2 HTML templates
* Bootstrap CSS

## Application Architecture
Similar to MVC or MVVM architecture patterns, maybe a hybrid of both.
Honestly, still trying to figure out if how I'm building this fits any pattern.
* Model: data_models, db
* View:  HTML/CSS templates, static files for presentation layer
* Controller: routes, services
* View Model:  view_models

