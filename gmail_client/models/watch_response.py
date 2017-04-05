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


class WatchResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, expiration=None, history_id=None):
        """
        WatchResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'expiration': 'str',
            'history_id': 'str'
        }

        self.attribute_map = {
            'expiration': 'expiration',
            'history_id': 'historyId'
        }

        self._expiration = expiration
        self._history_id = history_id

    @property
    def expiration(self):
        """
        Gets the expiration of this WatchResponse.
        When Gmail will stop sending notifications for mailbox updates (epoch millis). Call watch again before this time to renew the watch.

        :return: The expiration of this WatchResponse.
        :rtype: str
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        """
        Sets the expiration of this WatchResponse.
        When Gmail will stop sending notifications for mailbox updates (epoch millis). Call watch again before this time to renew the watch.

        :param expiration: The expiration of this WatchResponse.
        :type: str
        """

        self._expiration = expiration

    @property
    def history_id(self):
        """
        Gets the history_id of this WatchResponse.
        The ID of the mailbox's current history record.

        :return: The history_id of this WatchResponse.
        :rtype: str
        """
        return self._history_id

    @history_id.setter
    def history_id(self, history_id):
        """
        Sets the history_id of this WatchResponse.
        The ID of the mailbox's current history record.

        :param history_id: The history_id of this WatchResponse.
        :type: str
        """

        self._history_id = history_id

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
        if not isinstance(other, WatchResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other