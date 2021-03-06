# coding: utf-8

"""
    Gmail

    Access Gmail mailboxes including sending user email.

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class BatchModifyMessagesRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, add_label_ids=None, ids=None, remove_label_ids=None):
        """
        BatchModifyMessagesRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'add_label_ids': 'list[str]',
            'ids': 'list[str]',
            'remove_label_ids': 'list[str]'
        }

        self.attribute_map = {
            'add_label_ids': 'addLabelIds',
            'ids': 'ids',
            'remove_label_ids': 'removeLabelIds'
        }

        self._add_label_ids = add_label_ids
        self._ids = ids
        self._remove_label_ids = remove_label_ids

    @property
    def add_label_ids(self):
        """
        Gets the add_label_ids of this BatchModifyMessagesRequest.
        A list of label IDs to add to messages.

        :return: The add_label_ids of this BatchModifyMessagesRequest.
        :rtype: list[str]
        """
        return self._add_label_ids

    @add_label_ids.setter
    def add_label_ids(self, add_label_ids):
        """
        Sets the add_label_ids of this BatchModifyMessagesRequest.
        A list of label IDs to add to messages.

        :param add_label_ids: The add_label_ids of this BatchModifyMessagesRequest.
        :type: list[str]
        """

        self._add_label_ids = add_label_ids

    @property
    def ids(self):
        """
        Gets the ids of this BatchModifyMessagesRequest.
        The IDs of the messages to modify. There is a limit of 1000 ids per request.

        :return: The ids of this BatchModifyMessagesRequest.
        :rtype: list[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """
        Sets the ids of this BatchModifyMessagesRequest.
        The IDs of the messages to modify. There is a limit of 1000 ids per request.

        :param ids: The ids of this BatchModifyMessagesRequest.
        :type: list[str]
        """

        self._ids = ids

    @property
    def remove_label_ids(self):
        """
        Gets the remove_label_ids of this BatchModifyMessagesRequest.
        A list of label IDs to remove from messages.

        :return: The remove_label_ids of this BatchModifyMessagesRequest.
        :rtype: list[str]
        """
        return self._remove_label_ids

    @remove_label_ids.setter
    def remove_label_ids(self, remove_label_ids):
        """
        Sets the remove_label_ids of this BatchModifyMessagesRequest.
        A list of label IDs to remove from messages.

        :param remove_label_ids: The remove_label_ids of this BatchModifyMessagesRequest.
        :type: list[str]
        """

        self._remove_label_ids = remove_label_ids

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, BatchModifyMessagesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
