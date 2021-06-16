from fastapi.testclient import TestClient
from os import getenv
from app.main import app
from app.api.submission import Submission, submission_text
from unittest import TestCase
from requests import get, post
import unittest
import requests


host_url = 'http://127.0.0.1:8000/submission/text'
var = {"SubmissionID": 2,
               "StoryId": 1,
               "Pages": {"1": 
                        {"URL": "https://github.com/Lambda-School-Labs/story-squad-ds/blob/main/app/tests/test_bucket/Photo 3102 pg1.jpg",
                         "Checksum": "f40b27bb12afbe4cfb1a12cda42ed4e0a976e0b6b3c01dc229abeab7a114b1f5107328b3ee18c41bc2f1af9c96b7d3b9ae1b16c7007003d60c392a831ac10c4f"
                        },
                         "2": {
                         "URL": "https://github.com/Lambda-School-Labs/story-squad-ds/blob/main/app/tests/test_bucket/Photo 3102 pg2.jpg",
                        "Checksum": "3edee3286bb91e71fb8be7dac05fc12e37595643ccd67126810a03ded91e06adc80f19033d68a3fdbdf38296b9a376df272d78a7fb2281864c5d41fc079ef837"
                        }
                }
               }


class TestSubmission(unittest.TestCase):

    host_url = 'http://127.0.0.1:8000/submission/text'

    @classmethod
    def setUpSubmission(cls):
        """
        This is where the API URL will go.
        """
        # This is where the API URL will go
        cls.host_url = 'http://127.0.0.1:8000/submission/text'
        # Correct data and checksum
        
        var = {"SubmissionID": 123456,
               "StoryId": 2,
               "Pages": {"1": 
                        {"URL": "https://github.com/Lambda-School-Labs/story-squad-ds/blob/main/app/tests/test_bucket/Photo 3102 pg1.jpg",
                         "Checksum": "f40b27bb12afbe4cfb1a12cda42ed4e0a976e0b6b3c01dc229abeab7a114b1f5107328b3ee18c41bc2f1af9c96b7d3b9ae1b16c7007003d60c392a831ac10c4f"
                        },
                         "2": {
                         "URL": "https://github.com/Lambda-School-Labs/story-squad-ds/blob/main/app/tests/test_bucket/Photo 3102 pg2.jpg",
                        "Checksum": "3edee3286bb91e71fb8be7dac05fc12e37595643ccd67126810a03ded91e06adc80f19033d68a3fdbdf38296b9a376df272d78a7fb2281864c5d41fc079ef837"
                        }
                }
               }
        cls.sub1 = submission_text(var)
  
    
    # class TestSubmission(TestCase):
    def test_submission_text(self):
        response_code = requests.post(host_url, data=var)
        assert response_code.status_code == 200

    def test_submission_illustration(self):
        pass
