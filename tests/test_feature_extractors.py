import unittest
# from src.models.ecg_feature_extractor import ECGFeatureExtractor
# from src.models.ppg_feature_extractor import PPGFeatureExtractor
# from src.models.bcg_feature_extractor import BCGFeatureExtractor

class TestFeatureExtractors(unittest.TestCase):
    def test_dummy_ecg(self):
        # extractor = ECGFeatureExtractor()
        self.assertEqual(1, 1)

    def test_dummy_ppg(self):
        # extractor = PPGFeatureExtractor()
        self.assertEqual(1, 1)

    def test_dummy_bcg(self):
        # extractor = BCGFeatureExtractor()
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()
