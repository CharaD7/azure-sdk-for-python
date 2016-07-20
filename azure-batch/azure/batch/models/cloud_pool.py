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


class CloudPool(Model):
    """A pool in the Azure Batch service.

    :param id: A string that uniquely identifies the pool within the account.
     The id can contain any combination of alphanumeric characters including
     hyphens and underscores, and cannot contain more than 64 characters.
    :type id: str
    :param display_name: The display name for the pool.
    :type display_name: str
    :param url: The URL of the pool.
    :type url: str
    :param e_tag: The ETag of the pool.
    :type e_tag: str
    :param last_modified: The last modified time of the pool.
    :type last_modified: datetime
    :param creation_time: The creation time of the pool.
    :type creation_time: datetime
    :param state: The current state of the pool. Possible values include:
     'active', 'deleting', 'upgrading'
    :type state: str or :class:`PoolState <azure.batch.models.PoolState>`
    :param state_transition_time: The time at which the pool entered its
     current state.
    :type state_transition_time: datetime
    :param allocation_state: Whether the pool is resizing. Possible values
     include: 'steady', 'resizing', 'stopping'
    :type allocation_state: str or :class:`AllocationState
     <azure.batch.models.AllocationState>`
    :param allocation_state_transition_time: The time at which the pool
     entered its current allocation state.
    :type allocation_state_transition_time: datetime
    :param vm_size: The size of virtual machines in the pool. All virtual
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
    :param resize_timeout: The timeout for allocation of compute nodes to the
     pool. In a Get Pool operation, this is the timeout for the most recent
     resize operation. The default value is 10 minutes.
    :type resize_timeout: timedelta
    :param resize_error: Details of any error encountered while performing
     the last resize on the pool. This property is set only if an error
     occurred during the last pool resize, and only when the pool
     AllocationState is Steady.
    :type resize_error: :class:`ResizeError <azure.batch.models.ResizeError>`
    :param current_dedicated: The number of compute nodes currently in the
     pool.
    :type current_dedicated: int
    :param target_dedicated: The desired number of compute nodes in the pool.
     This property must have the default value if EnableAutoScale is true. It
     is required if EnableAutoScale is false.
    :type target_dedicated: int
    :param enable_auto_scale: Whether the pool size should automatically
     adjust over time. If true, the AutoScaleFormula property must be set. If
     false, the TargetDedicated property must be set.
    :type enable_auto_scale: bool
    :param auto_scale_formula: A formula for the desired number of compute
     nodes in the pool.
    :type auto_scale_formula: str
    :param auto_scale_evaluation_interval: A time interval for the desired
     AutoScale evaluation period in the pool.
    :type auto_scale_evaluation_interval: timedelta
    :param auto_scale_run: The results and errors from the last execution of
     the autoscale formula.
    :type auto_scale_run: :class:`AutoScaleRun
     <azure.batch.models.AutoScaleRun>`
    :param enable_inter_node_communication: Whether the pool permits direct
     communication between nodes.
    :type enable_inter_node_communication: bool
    :param start_task: A task specified to run on each compute node as it
     joins the pool.
    :type start_task: :class:`StartTask <azure.batch.models.StartTask>`
    :param certificate_references: The list of certificates to be installed
     on each compute node in the pool.
    :type certificate_references: list of :class:`CertificateReference
     <azure.batch.models.CertificateReference>`
    :param application_package_references: The list of application packages
     to be installed on each compute node in the pool.
    :type application_package_references: list of
     :class:`ApplicationPackageReference
     <azure.batch.models.ApplicationPackageReference>`
    :param max_tasks_per_node: The maximum number of tasks that can run
     concurrently on a single compute node in the pool.
    :type max_tasks_per_node: int
    :param task_scheduling_policy: How the Batch service distributes tasks
     between compute nodes in the pool.
    :type task_scheduling_policy: :class:`TaskSchedulingPolicy
     <azure.batch.models.TaskSchedulingPolicy>`
    :param metadata: A list of name-value pairs associated with the pool as
     metadata.
    :type metadata: list of :class:`MetadataItem
     <azure.batch.models.MetadataItem>`
    :param stats: Utilization and resource usage statistics for the entire
     lifetime of the pool.
    :type stats: :class:`PoolStatistics <azure.batch.models.PoolStatistics>`
    """ 

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'e_tag': {'key': 'eTag', 'type': 'str'},
        'last_modified': {'key': 'lastModified', 'type': 'iso-8601'},
        'creation_time': {'key': 'creationTime', 'type': 'iso-8601'},
        'state': {'key': 'state', 'type': 'PoolState'},
        'state_transition_time': {'key': 'stateTransitionTime', 'type': 'iso-8601'},
        'allocation_state': {'key': 'allocationState', 'type': 'AllocationState'},
        'allocation_state_transition_time': {'key': 'allocationStateTransitionTime', 'type': 'iso-8601'},
        'vm_size': {'key': 'vmSize', 'type': 'str'},
        'cloud_service_configuration': {'key': 'cloudServiceConfiguration', 'type': 'CloudServiceConfiguration'},
        'virtual_machine_configuration': {'key': 'virtualMachineConfiguration', 'type': 'VirtualMachineConfiguration'},
        'resize_timeout': {'key': 'resizeTimeout', 'type': 'duration'},
        'resize_error': {'key': 'resizeError', 'type': 'ResizeError'},
        'current_dedicated': {'key': 'currentDedicated', 'type': 'int'},
        'target_dedicated': {'key': 'targetDedicated', 'type': 'int'},
        'enable_auto_scale': {'key': 'enableAutoScale', 'type': 'bool'},
        'auto_scale_formula': {'key': 'autoScaleFormula', 'type': 'str'},
        'auto_scale_evaluation_interval': {'key': 'autoScaleEvaluationInterval', 'type': 'duration'},
        'auto_scale_run': {'key': 'autoScaleRun', 'type': 'AutoScaleRun'},
        'enable_inter_node_communication': {'key': 'enableInterNodeCommunication', 'type': 'bool'},
        'start_task': {'key': 'startTask', 'type': 'StartTask'},
        'certificate_references': {'key': 'certificateReferences', 'type': '[CertificateReference]'},
        'application_package_references': {'key': 'applicationPackageReferences', 'type': '[ApplicationPackageReference]'},
        'max_tasks_per_node': {'key': 'maxTasksPerNode', 'type': 'int'},
        'task_scheduling_policy': {'key': 'taskSchedulingPolicy', 'type': 'TaskSchedulingPolicy'},
        'metadata': {'key': 'metadata', 'type': '[MetadataItem]'},
        'stats': {'key': 'stats', 'type': 'PoolStatistics'},
    }

    def __init__(self, id=None, display_name=None, url=None, e_tag=None, last_modified=None, creation_time=None, state=None, state_transition_time=None, allocation_state=None, allocation_state_transition_time=None, vm_size=None, cloud_service_configuration=None, virtual_machine_configuration=None, resize_timeout=None, resize_error=None, current_dedicated=None, target_dedicated=None, enable_auto_scale=None, auto_scale_formula=None, auto_scale_evaluation_interval=None, auto_scale_run=None, enable_inter_node_communication=None, start_task=None, certificate_references=None, application_package_references=None, max_tasks_per_node=None, task_scheduling_policy=None, metadata=None, stats=None):
        self.id = id
        self.display_name = display_name
        self.url = url
        self.e_tag = e_tag
        self.last_modified = last_modified
        self.creation_time = creation_time
        self.state = state
        self.state_transition_time = state_transition_time
        self.allocation_state = allocation_state
        self.allocation_state_transition_time = allocation_state_transition_time
        self.vm_size = vm_size
        self.cloud_service_configuration = cloud_service_configuration
        self.virtual_machine_configuration = virtual_machine_configuration
        self.resize_timeout = resize_timeout
        self.resize_error = resize_error
        self.current_dedicated = current_dedicated
        self.target_dedicated = target_dedicated
        self.enable_auto_scale = enable_auto_scale
        self.auto_scale_formula = auto_scale_formula
        self.auto_scale_evaluation_interval = auto_scale_evaluation_interval
        self.auto_scale_run = auto_scale_run
        self.enable_inter_node_communication = enable_inter_node_communication
        self.start_task = start_task
        self.certificate_references = certificate_references
        self.application_package_references = application_package_references
        self.max_tasks_per_node = max_tasks_per_node
        self.task_scheduling_policy = task_scheduling_policy
        self.metadata = metadata
        self.stats = stats
