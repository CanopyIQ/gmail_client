# coding: utf-8

"""
    Gmail

    Access Gmail mailboxes including sending user email.

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import gmail_client
from gmail_client.rest import ApiException
from gmail_client.models.list_messages_response import ListMessagesResponse


class TestListMessagesResponse(unittest.TestCase):
    """ ListMessagesResponse unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testListMessagesResponse(self):
        """
        Test ListMessagesResponse
        """
        model = gmail_client.models.list_messages_response.ListMessagesResponse()


if __name__ == '__main__':
    unittest.main()