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
from gmail_client.models.batch_modify_messages_request import BatchModifyMessagesRequest


class TestBatchModifyMessagesRequest(unittest.TestCase):
    """ BatchModifyMessagesRequest unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testBatchModifyMessagesRequest(self):
        """
        Test BatchModifyMessagesRequest
        """
        model = gmail_client.models.batch_modify_messages_request.BatchModifyMessagesRequest()


if __name__ == '__main__':
    unittest.main()
