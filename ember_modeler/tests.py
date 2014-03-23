"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.db import models

from django.test import TestCase
from ember_modeler.ko import to_ember


class SimpleTest(TestCase):
    def test_basic_template(self):
        """
        Tests that a simple model is
        """
        class MyObject(models.Model):
            myNumber = models.IntegerField()
            myName = models.CharField()

        ember_string = to_ember(MyObject)

        self.assertEqual(ember_string,
                         ("App.Recipe = DS.Model.extend({\n"
                          "  title: DS.attr('string')\n"
                          "});"))
