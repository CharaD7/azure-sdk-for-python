# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ResourceMetricValue(Model):
    """Value of resource metric.

    :param time_stamp: Value timestamp
    :type time_stamp: str
    :param average: Value average
    :type average: float
    :param minimum: Value minimum
    :type minimum: float
    :param maximum: Value maximum
    :type maximum: float
    :param total: Value total
    :type total: float
    :param count: Value count
    :type count: float
    """ 

    _attribute_map = {
        'time_stamp': {'key': 'timeStamp', 'type': 'str'},
        'average': {'key': 'average', 'type': 'float'},
        'minimum': {'key': 'minimum', 'type': 'float'},
        'maximum': {'key': 'maximum', 'type': 'float'},
        'total': {'key': 'total', 'type': 'float'},
        'count': {'key': 'count', 'type': 'float'},
    }

    def __init__(self, time_stamp=None, average=None, minimum=None, maximum=None, total=None, count=None):
        self.time_stamp = time_stamp
        self.average = average
        self.minimum = minimum
        self.maximum = maximum
        self.total = total
        self.count = count
