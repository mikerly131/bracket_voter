# Bracket Voter
Submit 64 items of some topic, get them ranked by others bracket style, see composites ranking and scores for your topic lists.

## Project Info
Built using:
* Python and FastAPI web framework
* PostgreSQL DB
* SQLAlchemy 2.0 ORM using async sessions
* Jinja2 HTML templates
* Bootstrap CSS

## Application Architecture
Similar to MVC or MVVM architecture patterns, maybe a hybrid of both.
Honestly, still trying to figure out how I'm building this and if it fits any pattern.
* Model: data_models, db
* View:  HTML/CSS templates, static files for presentation layer
* Controller: routes, services
* View Model:  view_models

## About Rankings
Initial lists are ranked 1 to 64 by their creator
Composite Bracket: Winner is based of total count of winners from completed brackets. 
    Ties go to the higher ranked (ex. 1 beats 4)
Overall Score: Points awarded to list items for each win, fibonacci style (ex. win in round of 32 = 2pts)
    Score is averaged over number of brackets
