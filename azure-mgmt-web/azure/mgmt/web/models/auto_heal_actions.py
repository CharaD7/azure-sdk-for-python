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


class AutoHealActions(Model):
    """AutoHealActions - Describes the actions which can be
    taken by the auto-heal module when a rule is triggered.

    :param action_type: ActionType - predefined action to be taken. Possible
     values include: 'Recycle', 'LogEvent', 'CustomAction'
    :type action_type: str or :class:`AutoHealActionType
     <azure.mgmt.web.models.AutoHealActionType>`
    :param custom_action: CustomAction - custom action to be taken
    :type custom_action: :class:`AutoHealCustomAction
     <azure.mgmt.web.models.AutoHealCustomAction>`
    :param min_process_execution_time: MinProcessExecutionTime - minimum time
     the process must execute
     before taking the action
    :type min_process_execution_time: str
    """ 

    _validation = {
        'action_type': {'required': True},
    }

    _attribute_map = {
        'action_type': {'key': 'actionType', 'type': 'AutoHealActionType'},
        'custom_action': {'key': 'customAction', 'type': 'AutoHealCustomAction'},
        'min_process_execution_time': {'key': 'minProcessExecutionTime', 'type': 'str'},
    }

    def __init__(self, action_type, custom_action=None, min_process_execution_time=None):
        self.action_type = action_type
        self.custom_action = custom_action
        self.min_process_execution_time = min_process_execution_time
