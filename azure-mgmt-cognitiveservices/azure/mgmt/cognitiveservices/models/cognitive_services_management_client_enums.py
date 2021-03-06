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

from enum import Enum


class SkuName(Enum):

    f0 = "F0"
    s0 = "S0"
    s1 = "S1"
    s2 = "S2"
    s3 = "S3"
    s4 = "S4"


class SkuTier(Enum):

    free = "Free"
    standard = "Standard"
    premium = "Premium"


class Kind(Enum):

    computer_vision = "ComputerVision"
    emotion = "Emotion"
    face = "Face"
    luis = "LUIS"
    recommendations = "Recommendations"
    speech = "Speech"
    text_analytics = "TextAnalytics"
    web_lm = "WebLM"


class ProvisioningState(Enum):

    creating = "Creating"
    resolving_dns = "ResolvingDNS"
    succeeded = "Succeeded"
    failed = "Failed"


class KeyName(Enum):

    key1 = "Key1"
    key2 = "Key2"
