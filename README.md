django-ember-modeler
==============

**django-ember-modeler** attempts to make it easier to use Django models in your Ember applications.
It's currently only useful for prototyping, as it's missing a lot of function that would be
required for use in complex applications.

It's cloned from [django-knockout-modeller](https://github.com/Miserlou/django-knockout-modeler).

**django-ember-modeler** turns this:

```python
class MyObject(models.Model):
    myNumber = models.IntegerField()
    myName = models.CharField()
```

into this:

```javascript
App.MyObject = DS.Model.extend({
    "myNumber": 666,
    "myName": "Bob McChobb"
});
```

with just this!

```django
{{ MyObject|ember }}
```

Quick start
------------

0. Install django-ember-modeler

    ```python
    pip install git+git://git@github.com/Symmetric/django-ember-modeler
    ```

1. Add 'ember_modeler' to your INSTALLED_APPS setting like this:

    ```python
    INSTALLED_APPS = (
      ...
      'ember_modeler',
    )
    ```

2. Include Ember.js in your HTML:

4. Emberify your model:

    ```html   
    {% load ember %}
    <script>
        {{ MyObject|ember }}
    </script>
    ```

Issues
-------

This is currently a very basic implementation, but feel free to file an issue if you find bugs or
have suggestions for features (pull requests welcome).
