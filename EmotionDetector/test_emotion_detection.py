import unittest

from emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        result1=emotion_detector("I am glad this happened")
        self.assertEqual(result1['dominant_emotion'], "Joy")