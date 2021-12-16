**General purpose personal website website which include admin dashboard and api**

This is a backend code + admin dashboard to kick start your personal website development. Rest api included for frontend to display the information.

Dependency requirements -

```
pip install django
pip install libsass django-compressor django-sass-processor
pip install django-widget-tweaks
pip install pillow
pip install django-imagekit
pip install django-cleanup
pip install djangorestframework
pip install django-cors-headers
pip install django-tinymce
```

If you want to use mysql instead of sqlite

```
pip install mysqlconfig (or)
pip install mysql-connector-python
```

Instruction -

1. Install necessary dependency.
2. Change settings.example.py to settings.py and include your own database config.
3. Run the server.

For UISetting -

Insert UI you want the ability to show or hide into the UISetting table. E.g About, Portfolio, Contact, etc...
