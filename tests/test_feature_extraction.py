"""Offline regression tests for URLFeatureExtractor."""

import sys
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

BACKEND_PATH = Path(__file__).resolve().parents[1] / "03_Source_Code" / "backend"
sys.path.insert(0, str(BACKEND_PATH))

import feature_extraction
from feature_extraction import URLFeatureExtractor


class URLFeatureExtractorTests(unittest.TestCase):
    def setUp(self):
        self.extractor = URLFeatureExtractor()

    def test_detects_valid_ipv4_host(self):
        features = self.extractor._extract_lexical_features("https://192.0.2.1/login")
        self.assertEqual(features["has_ip_address"], 1.0)

    def test_does_not_detect_ip_address_in_path(self):
        features = self.extractor._extract_lexical_features(
            "https://example.com/redirect/192.0.2.1"
        )
        self.assertEqual(features["has_ip_address"], 0.0)

    def test_rejects_invalid_ipv4_host(self):
        features = self.extractor._extract_lexical_features(
            "https://999.999.999.999/login"
        )
        self.assertEqual(features["has_ip_address"], 0.0)

    def test_detects_ipv6_host(self):
        features = self.extractor._extract_lexical_features(
            "https://[2001:db8::1]/"
        )
        self.assertEqual(features["has_ip_address"], 1.0)

    def test_empty_url_has_zero_ratios(self):
        features = self.extractor._extract_lexical_features("")
        self.assertEqual(features["special_char_ratio"], 0)
        self.assertEqual(features["digit_ratio"], 0)
        self.assertEqual(features["has_ip_address"], 0.0)

    def test_invalid_port_is_handled(self):
        features = self.extractor._extract_lexical_features(
            "https://example.com:invalid/"
        )
        self.assertEqual(features["has_port"], 0.0)

    def test_entropy_for_empty_uniform_and_binary_strings(self):
        self.assertEqual(self.extractor._calculate_entropy(""), 0.0)
        self.assertEqual(self.extractor._calculate_entropy("aaaa"), 0.0)
        self.assertAlmostEqual(self.extractor._calculate_entropy("ab"), 1.0)

    def test_domain_features_use_extracted_parts_and_mock_age(self):
        extracted = SimpleNamespace(domain="example", subdomain="www", suffix="com")
        with patch.object(feature_extraction.tldextract, "extract", return_value=extracted):
            features = self.extractor._extract_domain_features(
                "https://www.example.com"
            )

        self.assertEqual(features["domain_length"], 7)
        self.assertEqual(features["num_subdomains"], 1)
        self.assertEqual(features["has_trusted_tld"], 1.0)
        self.assertEqual(
            features["domain_age_days"], self.extractor._mock_domain_age("example")
        )

    def test_domain_extraction_failure_returns_documented_fallback(self):
        with patch.object(
            feature_extraction.tldextract, "extract", side_effect=RuntimeError("bad URL")
        ):
            features = self.extractor._extract_domain_features("not a URL")

        self.assertEqual(features["domain_length"], 0)
        self.assertEqual(features["domain_age_days"], 0)
        self.assertEqual(features["is_new_domain"], 1.0)

    def test_http_security_features_do_not_open_a_socket(self):
        with patch.object(feature_extraction.socket, "create_connection") as connect:
            features = self.extractor._extract_security_features("http://example.com")

        connect.assert_not_called()
        self.assertEqual(features["uses_https"], 0.0)
        self.assertEqual(features["has_valid_ssl"], 0.0)

    def test_https_connection_failure_is_reported_without_raising(self):
        with patch.object(
            feature_extraction.socket,
            "create_connection",
            side_effect=OSError("offline"),
        ):
            features = self.extractor._extract_security_features("https://example.com")

        self.assertEqual(features["uses_https"], 1.0)
        self.assertEqual(features["has_valid_ssl"], 0.0)
        self.assertEqual(features["ssl_cert_age_days"], 0)


if __name__ == "__main__":
    unittest.main()
