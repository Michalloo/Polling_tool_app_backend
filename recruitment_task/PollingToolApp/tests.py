from django.test import SimpleTestCase
from PollingToolApp.models import Response
import pytest

class AnswerTestCase(SimpleTestCase):
    
    def test_model_length(self):
        test_object = Response(answer="Very nice web application")
        assert(len(test_object.answer)<150)
    
    def test_model_type(self):
        test_object = Response(answer="Very nice")
        assert(isinstance(test_object.answer,str))



        