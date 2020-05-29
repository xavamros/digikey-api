# coding: utf-8

"""
    PartSearch Api

    Search for products and retrieve details and pricing.  # noqa: E501

    OpenAPI spec version: v3
    Contact: api.support@digikey.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import digikey.v3.productinformation
from digikey.v3.productinformation.api.part_search_api import PartSearchApi  # noqa: E501
from digikey.v3.productinformation.rest import ApiException


class TestPartSearchApi(unittest.TestCase):
    """PartSearchApi unit test stubs"""

    def setUp(self):
        self.api = digikey.v3.productinformation.api.part_search_api.PartSearchApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_products_digi_key_part_number_digi_reel_pricing_get(self):
        """Test case for products_digi_key_part_number_digi_reel_pricing_get

        Calculate the DigiReel pricing for the given DigiKeyPartNumber and RequestedQuantity  # noqa: E501
        """
        pass

    def test_products_digi_key_part_number_get(self):
        """Test case for products_digi_key_part_number_get

        Retrieve detailed product information including real time pricing and availability.  # noqa: E501
        """
        pass

    def test_products_keyword_post(self):
        """Test case for products_keyword_post

        KeywordSearch can search for any product in the Digi-Key catalog.  # noqa: E501
        """
        pass

    def test_products_manufacturer_product_details_post(self):
        """Test case for products_manufacturer_product_details_post

        Create list of ProductDetails from the matches of the requested manufacturer product name.  # noqa: E501
        """
        pass

    def test_products_part_number_with_suggested_products_get(self):
        """Test case for products_part_number_with_suggested_products_get

        Retrieve detailed product information and two suggested products  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
