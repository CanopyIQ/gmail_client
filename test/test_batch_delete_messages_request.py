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
from gmail_client.models.batch_delete_messages_request import BatchDeleteMessagesRequest


class TestBatchDeleteMessagesRequest(unittest.TestCase):
    """ BatchDeleteMessagesRequest unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testBatchDeleteMessagesRequest(self):
        """
        Test BatchDeleteMessagesRequest
        """
        model = gmail_client.models.batch_delete_messages_request.BatchDeleteMessagesRequest()


if __name__ == '__main__':
    unittest.main()