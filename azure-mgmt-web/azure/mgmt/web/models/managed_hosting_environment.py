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

from .resource import Resource


class ManagedHostingEnvironment(Resource):
    """Description of a managed hosting environment.

    :param id: Resource Id
    :type id: str
    :param name: Resource Name
    :type name: str
    :param kind: Kind of resource
    :type kind: str
    :param location: Resource Location
    :type location: str
    :param type: Resource type
    :type type: str
    :param tags: Resource tags
    :type tags: dict
    :param managed_hosting_environment_name: Name of the managed hosting
     environment
    :type managed_hosting_environment_name: str
    :param managed_hosting_environment_location: Location of the managed
     hosting environment e.g. "West US"
    :type managed_hosting_environment_location: str
    :param status: Current status of the managed hosting environment.
     Possible values include: 'Preparing', 'Ready', 'Deleting'
    :type status: str or :class:`ManagedHostingEnvironmentStatus
     <azure.mgmt.web.models.ManagedHostingEnvironmentStatus>`
    :param virtual_network: Description of the managed hosting environment's
     virtual network
    :type virtual_network: :class:`VirtualNetworkProfile
     <azure.mgmt.web.models.VirtualNetworkProfile>`
    :param ipssl_address_count: Number of ip ssl addresses reserved for the
     managed hosting environment
    :type ipssl_address_count: int
    :param dns_suffix: DNS suffix of the managed hosting environment
    :type dns_suffix: str
    :param subscription_id: Subscription of the managed hosting environment
     (read only)
    :type subscription_id: str
    :param resource_group: Resource group of the managed hosting environment
     (read only)
    :type resource_group: str
    :param environment_is_healthy: True/false indicating whether the managed
     hosting environment is healthy
    :type environment_is_healthy: bool
    :param environment_status: Detailed message about with results of the
     last check of the managed hosting environment
    :type environment_status: str
    :param suspended: True/false indicating whether the managed hosting
     environment is suspended. The environment can be suspended e.g. when the
     management endpoint is no longer available
     (most likely because NSG blocked the incoming traffic)
    :type suspended: bool
    :param api_management_account: Resource id of the api management account
     associated with this managed hosting environment (read only)
    :type api_management_account: str
    """ 

    _validation = {
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'managed_hosting_environment_name': {'key': 'properties.name', 'type': 'str'},
        'managed_hosting_environment_location': {'key': 'properties.location', 'type': 'str'},
        'status': {'key': 'properties.status', 'type': 'ManagedHostingEnvironmentStatus'},
        'virtual_network': {'key': 'properties.virtualNetwork', 'type': 'VirtualNetworkProfile'},
        'ipssl_address_count': {'key': 'properties.ipsslAddressCount', 'type': 'int'},
        'dns_suffix': {'key': 'properties.dnsSuffix', 'type': 'str'},
        'subscription_id': {'key': 'properties.subscriptionId', 'type': 'str'},
        'resource_group': {'key': 'properties.resourceGroup', 'type': 'str'},
        'environment_is_healthy': {'key': 'properties.environmentIsHealthy', 'type': 'bool'},
        'environment_status': {'key': 'properties.environmentStatus', 'type': 'str'},
        'suspended': {'key': 'properties.suspended', 'type': 'bool'},
        'api_management_account': {'key': 'properties.apiManagementAccount', 'type': 'str'},
    }

    def __init__(self, location, id=None, name=None, kind=None, type=None, tags=None, managed_hosting_environment_name=None, managed_hosting_environment_location=None, status=None, virtual_network=None, ipssl_address_count=None, dns_suffix=None, subscription_id=None, resource_group=None, environment_is_healthy=None, environment_status=None, suspended=None, api_management_account=None):
        super(ManagedHostingEnvironment, self).__init__(id=id, name=name, kind=kind, location=location, type=type, tags=tags)
        self.managed_hosting_environment_name = managed_hosting_environment_name
        self.managed_hosting_environment_location = managed_hosting_environment_location
        self.status = status
        self.virtual_network = virtual_network
        self.ipssl_address_count = ipssl_address_count
        self.dns_suffix = dns_suffix
        self.subscription_id = subscription_id
        self.resource_group = resource_group
        self.environment_is_healthy = environment_is_healthy
        self.environment_status = environment_status
        self.suspended = suspended
        self.api_management_account = api_management_account
