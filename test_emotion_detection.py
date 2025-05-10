from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        # Test with a sample text
        text = "I am so happy that i got this course"
        result = emotion_detector(text)
        
        # Check if the result is a dictionary
        self.assertIsInstance(result, dict)
        
        # Check if the dominant emotion is in the result
        self.assertIn("dominant_emotion", result)
        
        # Check if the confidence score is a float
        self.assertIsInstance(result[result["dominant_emotion"]], float)

    def test_emotion_detection_joy(self):
        # Test with a sample text
        text = "I am glad this happened"
        result = emotion_detector(text)
        
        # Check if the dominant emotion is joy
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_emotion_detection_anger(self):
        # Test with a sample text
        text = "I am really mad about this"
        result = emotion_detector(text)
        
        # Check if the dominant emotion is anger
        self.assertEqual(result["dominant_emotion"], "anger")

    def test_emotion_detection_disgust(self):
        # Test with a sample text
        text = "I feel disgusted just hearing about this"
        result = emotion_detector(text)
        
        # Check if the dominant emotion is disgust
        self.assertEqual(result["dominant_emotion"], "disgust")

    def test_emotion_detection_sadness(self):
        # Test with a sample text
        text = "I am so sad about this"
        result = emotion_detector(text)
        
        # Check if the dominant emotion is sadness
        self.assertEqual(result["dominant_emotion"], "sadness")

    def test_emotion_detection_fear(self):
        # Test with a sample text
        text = "I am really afraid that this will happen"
        result = emotion_detector(text)
        # Check if the dominant emotion is fear
        self.assertEqual(result["dominant_emotion"], "fear")

if __name__ == "__main__":
    unittest.main()