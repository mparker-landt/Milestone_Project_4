# Milestone_Project_4

fixtures - collection of data that Django knows how to import into a database
migrations - way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema
static
templates - text document or a Python string marked-up using the Django template language
templatetags - allows us to to do some programming on the server before sending HTML to the client

admin - display your models in the Django admin panel
apps
contexts - Python functions that can be used to modify the context data passed to a template
forms - web forms and how they are handled in Django
models - A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you're storing. Generally, each model maps to a single database table
signals - Signals in Django are a notification system that allows certain “senders” to notify a set of “receivers” when certain actions take place
tests
urls - mapping between URL path expressions to Python functions (your views)
views - Python functions that takes http requests and returns http response, like HTML documents
webhook_handler
webhooks - Webhooks are HTTP endpoints that are triggered when an event occurs
widgets - A widget is Django's representation of an HTML input element. The widget handles the rendering of the HTML, and the extraction of data from a GET/POST