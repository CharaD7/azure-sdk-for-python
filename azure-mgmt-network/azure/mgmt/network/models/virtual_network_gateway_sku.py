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


class VirtualNetworkGatewaySku(Model):
    """VirtualNetworkGatewaySku details.

    :param name: Gateway sku name -Basic/HighPerformance/Standard. Possible
     values include: 'Basic', 'HighPerformance', 'Standard'
    :type name: str or :class:`VirtualNetworkGatewaySkuName
     <azure.mgmt.network.models.VirtualNetworkGatewaySkuName>`
    :param tier: Gateway sku tier -Basic/HighPerformance/Standard. Possible
     values include: 'Basic', 'HighPerformance', 'Standard'
    :type tier: str or :class:`VirtualNetworkGatewaySkuTier
     <azure.mgmt.network.models.VirtualNetworkGatewaySkuTier>`
    :param capacity: The capacity
    :type capacity: int
    """ 

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'tier': {'key': 'tier', 'type': 'str'},
        'capacity': {'key': 'capacity', 'type': 'int'},
    }

    def __init__(self, name=None, tier=None, capacity=None):
        self.name = name
        self.tier = tier
        self.capacity = capacity
