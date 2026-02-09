from unittest.mock import Mock, patch

from django.test import SimpleTestCase
from requests import HTTPError

from .views import USD_KZT_FALLBACK_RATE, get_price_KZT


class GetPriceKZTTests(SimpleTestCase):
    @patch("app.views.requests.get")
    def test_returns_ceiled_rate_for_numeric_response(self, mock_get):
        response = Mock()
        response.text = "498.13"
        response.raise_for_status.return_value = None
        mock_get.return_value = response

        self.assertEqual(get_price_KZT(), 499)

    @patch("app.views.requests.get")
    def test_returns_fallback_for_non_numeric_response(self, mock_get):
        response = Mock()
        response.text = "<html><h1>503 Service Unavailable</h1></html>"
        response.raise_for_status.return_value = None
        mock_get.return_value = response

        self.assertEqual(get_price_KZT(), USD_KZT_FALLBACK_RATE)

    @patch("app.views.requests.get")
    def test_returns_fallback_for_http_error(self, mock_get):
        response = Mock()
        response.text = "Service unavailable"
        response.raise_for_status.side_effect = HTTPError("503 Server Error")
        mock_get.return_value = response

        self.assertEqual(get_price_KZT(), USD_KZT_FALLBACK_RATE)
