# coding: utf-8

"""
    PartSearch Api

    Search for products and retrieve details and pricing.  # noqa: E501

    OpenAPI spec version: v3
    Contact: api.support@digikey.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SortParameters(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'sort_option': 'SortOption',
        'direction': 'SortDirection',
        'sort_parameter_id': 'int'
    }

    attribute_map = {
        'sort_option': 'SortOption',
        'direction': 'Direction',
        'sort_parameter_id': 'SortParameterId'
    }

    def __init__(self, sort_option=None, direction=None, sort_parameter_id=None):  # noqa: E501
        """SortParameters - a model defined in Swagger"""  # noqa: E501

        self._sort_option = None
        self._direction = None
        self._sort_parameter_id = None
        self.discriminator = None

        self.sort_option = sort_option
        self.direction = direction
        if sort_parameter_id is not None:
            self.sort_parameter_id = sort_parameter_id

    @property
    def sort_option(self):
        """Gets the sort_option of this SortParameters.  # noqa: E501


        :return: The sort_option of this SortParameters.  # noqa: E501
        :rtype: SortOption
        """
        return self._sort_option

    @sort_option.setter
    def sort_option(self, sort_option):
        """Sets the sort_option of this SortParameters.


        :param sort_option: The sort_option of this SortParameters.  # noqa: E501
        :type: SortOption
        """
        if sort_option is None:
            raise ValueError("Invalid value for `sort_option`, must not be `None`")  # noqa: E501

        self._sort_option = sort_option

    @property
    def direction(self):
        """Gets the direction of this SortParameters.  # noqa: E501


        :return: The direction of this SortParameters.  # noqa: E501
        :rtype: SortDirection
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this SortParameters.


        :param direction: The direction of this SortParameters.  # noqa: E501
        :type: SortDirection
        """
        if direction is None:
            raise ValueError("Invalid value for `direction`, must not be `None`")  # noqa: E501

        self._direction = direction

    @property
    def sort_parameter_id(self):
        """Gets the sort_parameter_id of this SortParameters.  # noqa: E501

        The ParameterId of the parameter to sort on. The ParameterId can be found in the Search response. This is only used with SortByParameter.  # noqa: E501

        :return: The sort_parameter_id of this SortParameters.  # noqa: E501
        :rtype: int
        """
        return self._sort_parameter_id

    @sort_parameter_id.setter
    def sort_parameter_id(self, sort_parameter_id):
        """Sets the sort_parameter_id of this SortParameters.

        The ParameterId of the parameter to sort on. The ParameterId can be found in the Search response. This is only used with SortByParameter.  # noqa: E501

        :param sort_parameter_id: The sort_parameter_id of this SortParameters.  # noqa: E501
        :type: int
        """

        self._sort_parameter_id = sort_parameter_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(SortParameters, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SortParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
