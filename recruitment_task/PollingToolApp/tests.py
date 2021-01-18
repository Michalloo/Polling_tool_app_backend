from django.test import TestCase
from PollingToolApp import Response
import pytest

# Create your tests here.


class AnswerTestCase(TestCase):
    def test_model_response(self):
        test_object = Response.objects.create(answer="Very nice web application")
        assert len(test_object.answer) > 150
