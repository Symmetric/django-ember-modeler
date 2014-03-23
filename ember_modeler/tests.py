"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.db import models

from django.test import TestCase
from ember_modeler.modeler import to_ember, to_ember_model


class SimpleTest(TestCase):
    def test_basic_template(self):
        """
        Tests that a simple model is
        """
        class MyObject(models.Model):
            my_number = models.IntegerField()
            my_string = models.CharField()

        ember_model_string = to_ember_model(MyObject)

        self.assertEqual(ember_model_string,
                         ("App.MyObject = DS.Model.extend({\n"
                          "    my_number: DS.attr('number'),\n"
                          "    my_string: DS.attr('string')\n"
                          "});"))
