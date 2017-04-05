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


class ImapSettings(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, auto_expunge=None, enabled=None, expunge_behavior=None, max_folder_size=None):
        """
        ImapSettings - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'auto_expunge': 'bool',
            'enabled': 'bool',
            'expunge_behavior': 'str',
            'max_folder_size': 'int'
        }

        self.attribute_map = {
            'auto_expunge': 'autoExpunge',
            'enabled': 'enabled',
            'expunge_behavior': 'expungeBehavior',
            'max_folder_size': 'maxFolderSize'
        }

        self._auto_expunge = auto_expunge
        self._enabled = enabled
        self._expunge_behavior = expunge_behavior
        self._max_folder_size = max_folder_size

    @property
    def auto_expunge(self):
        """
        Gets the auto_expunge of this ImapSettings.
        If this value is true, Gmail will immediately expunge a message when it is marked as deleted in IMAP. Otherwise, Gmail will wait for an update from the client before expunging messages marked as deleted.

        :return: The auto_expunge of this ImapSettings.
        :rtype: bool
        """
        return self._auto_expunge

    @auto_expunge.setter
    def auto_expunge(self, auto_expunge):
        """
        Sets the auto_expunge of this ImapSettings.
        If this value is true, Gmail will immediately expunge a message when it is marked as deleted in IMAP. Otherwise, Gmail will wait for an update from the client before expunging messages marked as deleted.

        :param auto_expunge: The auto_expunge of this ImapSettings.
        :type: bool
        """

        self._auto_expunge = auto_expunge

    @property
    def enabled(self):
        """
        Gets the enabled of this ImapSettings.
        Whether IMAP is enabled for the account.

        :return: The enabled of this ImapSettings.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this ImapSettings.
        Whether IMAP is enabled for the account.

        :param enabled: The enabled of this ImapSettings.
        :type: bool
        """

        self._enabled = enabled

    @property
    def expunge_behavior(self):
        """
        Gets the expunge_behavior of this ImapSettings.
        The action that will be executed on a message when it is marked as deleted and expunged from the last visible IMAP folder.

        :return: The expunge_behavior of this ImapSettings.
        :rtype: str
        """
        return self._expunge_behavior

    @expunge_behavior.setter
    def expunge_behavior(self, expunge_behavior):
        """
        Sets the expunge_behavior of this ImapSettings.
        The action that will be executed on a message when it is marked as deleted and expunged from the last visible IMAP folder.

        :param expunge_behavior: The expunge_behavior of this ImapSettings.
        :type: str
        """
        allowed_values = ["archive", "deleteForever", "expungeBehaviorUnspecified", "trash"]
        if expunge_behavior not in allowed_values:
            raise ValueError(
                "Invalid value for `expunge_behavior` ({0}), must be one of {1}"
                .format(expunge_behavior, allowed_values)
            )

        self._expunge_behavior = expunge_behavior

    @property
    def max_folder_size(self):
        """
        Gets the max_folder_size of this ImapSettings.
        An optional limit on the number of messages that an IMAP folder may contain. Legal values are 0, 1000, 2000, 5000 or 10000. A value of zero is interpreted to mean that there is no limit.

        :return: The max_folder_size of this ImapSettings.
        :rtype: int
        """
        return self._max_folder_size

    @max_folder_size.setter
    def max_folder_size(self, max_folder_size):
        """
        Sets the max_folder_size of this ImapSettings.
        An optional limit on the number of messages that an IMAP folder may contain. Legal values are 0, 1000, 2000, 5000 or 10000. A value of zero is interpreted to mean that there is no limit.

        :param max_folder_size: The max_folder_size of this ImapSettings.
        :type: int
        """

        self._max_folder_size = max_folder_size

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
        if not isinstance(other, ImapSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
