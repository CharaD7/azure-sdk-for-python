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


class PoolSpecification(Model):
    """Specification for creating a new pool.

    :param display_name: The display name for the pool.
    :type display_name: str
    :param vm_size: The size of the virtual machines in the pool. All virtual
     machines in a pool are the same size.
    :type vm_size: str
    :param cloud_service_configuration: The cloud service configuration for
     the pool. This property and VirtualMachineConfiguration are mutually
     exclusive and one of the properties must be specified.
    :type cloud_service_configuration: :class:`CloudServiceConfiguration
     <azure.batch.models.CloudServiceConfiguration>`
    :param virtual_machine_configuration: The virtual machine configuration
     for the pool. This property and CloudServiceConfiguration are mutually
     exclusive and one of the properties must be specified.
    :type virtual_machine_configuration: :class:`VirtualMachineConfiguration
     <azure.batch.models.VirtualMachineConfiguration>`
    :param max_tasks_per_node: The maximum number of tasks that can run
     concurrently on a single compute node in the pool.
    :type max_tasks_per_node: int
    :param task_scheduling_policy: How tasks are distributed among compute
     nodes in the pool.
    :type task_scheduling_policy: :class:`TaskSchedulingPolicy
     <azure.batch.models.TaskSchedulingPolicy>`
    :param resize_timeout: The timeout for allocation of compute nodes to the
     pool.
    :type resize_timeout: timedelta
    :param target_dedicated: The desired number of compute nodes in the pool.
    :type target_dedicated: int
    :param enable_auto_scale: Whether the pool size should automatically
     adjust over time.
    :type enable_auto_scale: bool
    :param auto_scale_formula: The formula for the desired number of compute
     nodes in the pool.
    :type auto_scale_formula: str
    :param auto_scale_evaluation_interval: A time interval for the desired
     AutoScale evaluation period in the pool.
    :type auto_scale_evaluation_interval: timedelta
    :param enable_inter_node_communication: Whether the pool permits direct
     communication between nodes.
    :type enable_inter_node_communication: bool
    :param start_task: A task to run on each compute node as it joins the
     pool. The task runs when the node is added to the pool or when the node
     is restarted.
    :type start_task: :class:`StartTask <azure.batch.models.StartTask>`
    :param certificate_references: A list of certificates to be installed on
     each compute node in the pool.
    :type certificate_references: list of :class:`CertificateReference
     <azure.batch.models.CertificateReference>`
    :param application_package_references: The list of application packages
     to be installed on each compute node in the pool.
    :type application_package_references: list of
     :class:`ApplicationPackageReference
     <azure.batch.models.ApplicationPackageReference>`
    :param metadata: A list of name-value pairs associated with the pool as
     metadata.
    :type metadata: list of :class:`MetadataItem
     <azure.batch.models.MetadataItem>`
    """ 

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'vm_size': {'key': 'vmSize', 'type': 'str'},
        'cloud_service_configuration': {'key': 'cloudServiceConfiguration', 'type': 'CloudServiceConfiguration'},
        'virtual_machine_configuration': {'key': 'virtualMachineConfiguration', 'type': 'VirtualMachineConfiguration'},
        'max_tasks_per_node': {'key': 'maxTasksPerNode', 'type': 'int'},
        'task_scheduling_policy': {'key': 'taskSchedulingPolicy', 'type': 'TaskSchedulingPolicy'},
        'resize_timeout': {'key': 'resizeTimeout', 'type': 'duration'},
        'target_dedicated': {'key': 'targetDedicated', 'type': 'int'},
        'enable_auto_scale': {'key': 'enableAutoScale', 'type': 'bool'},
        'auto_scale_formula': {'key': 'autoScaleFormula', 'type': 'str'},
        'auto_scale_evaluation_interval': {'key': 'autoScaleEvaluationInterval', 'type': 'duration'},
        'enable_inter_node_communication': {'key': 'enableInterNodeCommunication', 'type': 'bool'},
        'start_task': {'key': 'startTask', 'type': 'StartTask'},
        'certificate_references': {'key': 'certificateReferences', 'type': '[CertificateReference]'},
        'application_package_references': {'key': 'applicationPackageReferences', 'type': '[ApplicationPackageReference]'},
        'metadata': {'key': 'metadata', 'type': '[MetadataItem]'},
    }

    def __init__(self, display_name=None, vm_size=None, cloud_service_configuration=None, virtual_machine_configuration=None, max_tasks_per_node=None, task_scheduling_policy=None, resize_timeout=None, target_dedicated=None, enable_auto_scale=None, auto_scale_formula=None, auto_scale_evaluation_interval=None, enable_inter_node_communication=None, start_task=None, certificate_references=None, application_package_references=None, metadata=None):
        self.display_name = display_name
        self.vm_size = vm_size
        self.cloud_service_configuration = cloud_service_configuration
        self.virtual_machine_configuration = virtual_machine_configuration
        self.max_tasks_per_node = max_tasks_per_node
        self.task_scheduling_policy = task_scheduling_policy
        self.resize_timeout = resize_timeout
        self.target_dedicated = target_dedicated
        self.enable_auto_scale = enable_auto_scale
        self.auto_scale_formula = auto_scale_formula
        self.auto_scale_evaluation_interval = auto_scale_evaluation_interval
        self.enable_inter_node_communication = enable_inter_node_communication
        self.start_task = start_task
        self.certificate_references = certificate_references
        self.application_package_references = application_package_references
        self.metadata = metadata
