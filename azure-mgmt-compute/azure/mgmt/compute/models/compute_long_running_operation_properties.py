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


class ComputeLongRunningOperationProperties(Model):
    """Compute-specific operation properties, including output.

    :param output: Operation output data (raw JSON)
    :type output: object
    """ 

    _attribute_map = {
        'output': {'key': 'output', 'type': 'object'},
    }

    def __init__(self, output=None):
        self.output = output
