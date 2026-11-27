"""
Feature Extraction Module for Phishing URL Detection.
Extracts lexical, domain-derived, and SSL/security URL attributes.
"""

import ipaddress
import socket
import ssl
import urllib.parse
from datetime import datetime
from typing import Dict

import numpy as np
import tldextract


class URLFeatureExtractor:
    """Extract hybrid features from URLs for phishing detection."""

    def __init__(self):
        self.suspicious_keywords = [
            "login", "signin", "verify", "account", "update", "secure",
            "banking", "confirm", "suspend", "restore", "click", "submit",
            "password", "user", "admin", "authentication", "wallet", "paypal",
        ]
        self.trusted_tlds = ["com", "org", "net", "edu", "gov", "mil"]

    def extract_all_features(self, url: str) -> Dict[str, float]:
        """Return lexical, domain, and security features for a URL."""
        features = {}
        features.update(self._extract_lexical_features(url))
        features.update(self._extract_domain_features(url))
        features.update(self._extract_security_features(url))
        return features

    def _extract_lexical_features(self, url: str) -> Dict[str, float]:
        features = {}
        features["url_length"] = len(url)
        features["num_dots"] = url.count(".")
        features["num_hyphens"] = url.count("-")
        features["num_underscores"] = url.count("_")
        features["num_slashes"] = url.count("/")
        features["num_question_marks"] = url.count("?")
        features["num_ampersands"] = url.count("&")
        features["num_at_symbols"] = url.count("@")
        features["num_equals"] = url.count("=")

        special_chars = sum(url.count(c) for c in "!@#$%^&*()_+=[]{}|;:,<>?")
        features["special_char_ratio"] = special_chars / len(url) if url else 0
        num_digits = sum(c.isdigit() for c in url)
        features["digit_ratio"] = num_digits / len(url) if url else 0

        parsed = urllib.parse.urlparse(url)
        try:
            ipaddress.ip_address(parsed.hostname or "")
        except ValueError:
            features["has_ip_address"] = 0.0
        else:
            features["has_ip_address"] = 1.0

        url_lower = url.lower()
        features["num_suspicious_keywords"] = sum(
            1 for keyword in self.suspicious_keywords if keyword in url_lower
        )
        shortening_services = ["bit.ly", "tinyurl", "goo.gl", "t.co", "ow.ly"]
        features["is_shortened"] = (
            1.0 if any(service in url_lower for service in shortening_services) else 0.0
        )
        features["has_https"] = 1.0 if url_lower.startswith("https://") else 0.0

        try:
            features["has_port"] = 1.0 if parsed.port is not None else 0.0
        except ValueError:
            features["has_port"] = 0.0

        features["num_subdirectories"] = len([p for p in parsed.path.split("/") if p])
        hostname = parsed.netloc
        features["hostname_length"] = len(hostname)
        features["hostname_is_long"] = 1.0 if len(hostname) > 50 else 0.0
        features["has_double_slash"] = 1.0 if "//" in parsed.path else 0.0
        features["has_hyphen_in_domain"] = 1.0 if "-" in hostname else 0.0
        return features

    def _extract_domain_features(self, url: str) -> Dict[str, float]:
        features = {}
        try:
            extracted = tldextract.extract(url)
            domain = extracted.domain
            subdomain = extracted.subdomain
            tld = extracted.suffix

            features["domain_length"] = len(domain) if domain else 0
            features["num_subdomains"] = len([s for s in subdomain.split(".") if s])
            features["has_trusted_tld"] = 1.0 if tld in self.trusted_tlds else 0.0
            features["domain_has_digits"] = (
                1.0 if any(c.isdigit() for c in domain) else 0.0
            )
            features["domain_entropy"] = self._calculate_entropy(domain) if domain else 0.0

            # This is deliberately a mock value, not WHOIS registration data.
            features["domain_age_days"] = self._mock_domain_age(domain)
            features["is_new_domain"] = (
                1.0 if features["domain_age_days"] < 180 else 0.0
            )
        except Exception:
            features.update({
                "domain_length": 0,
                "num_subdomains": 0,
                "has_trusted_tld": 0.0,
                "domain_has_digits": 0.0,
                "domain_entropy": 0.0,
                "domain_age_days": 0,
                "is_new_domain": 1.0,
            })
        return features

    def _extract_security_features(self, url: str) -> Dict[str, float]:
        features = {}
        parsed = urllib.parse.urlparse(url)
        hostname = parsed.hostname or ""
        features["uses_https"] = 1.0 if parsed.scheme.lower() == "https" else 0.0
        features["has_valid_ssl"] = 0.0
        features["ssl_cert_age_days"] = 0

        if parsed.scheme.lower() == "https" and hostname:
            try:
                context = ssl.create_default_context()
                with socket.create_connection((hostname, parsed.port or 443), timeout=2) as sock:
                    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                        cert = ssock.getpeercert()
                        features["has_valid_ssl"] = 1.0
                        not_before = datetime.strptime(
                            cert["notBefore"], "%b %d %H:%M:%S %Y %Z"
                        )
                        features["ssl_cert_age_days"] = (
                            datetime.now() - not_before
                        ).days
            except (OSError, ssl.SSLError, KeyError, ValueError):
                # Network/certificate failures are represented as unavailable/false.
                features["has_valid_ssl"] = 0.0
                features["ssl_cert_age_days"] = 0
        return features

    @staticmethod
    def _calculate_entropy(text: str) -> float:
        if not text:
            return 0.0
        frequencies = {}
        for char in text:
            frequencies[char] = frequencies.get(char, 0) + 1
        length = len(text)
        return -sum(
            (count / length) * np.log2(count / length)
            for count in frequencies.values()
        )

    @staticmethod
    def _mock_domain_age(domain: str) -> int:
        """Return deterministic mock age; never treat this as real WHOIS data."""
        if not domain:
            return 0
        return (sum(ord(char) for char in domain) % 3650) + 1

    def get_feature_names(self) -> list:
        """Return feature names in extraction order."""
        return list(self.extract_all_features("http://example.com").keys())


if __name__ == "__main__":
    extractor = URLFeatureExtractor()
    examples = [
        "https://example.com",
        "http://192.0.2.1/login.php",
        "http://secure-banking-verify-account.example/update.html",
        "https://short.example/abc",
    ]
    for example in examples:
        values = extractor.extract_all_features(example)
        print(f"\nURL: {example}")
        print(f"Feature count: {len(values)}")
        for name, value in list(values.items())[:5]:
            print(f"  {name}: {value}")
