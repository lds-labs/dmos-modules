#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The module file for dmos_l3_interface
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': '<support_group>'
}

DOCUMENTATION = """
---
module: dmos_l3_interface
version_added: 4.9
short_description: 'Manages <xxxx> attributes of <network_os> <resource>.'
description: 'Manages <xxxx> attributes of <network_os> <resource>'
author: Ansible Network Engineer
notes:
  - 'Tested against <network_os> <version>'
options:
  config:
    description: The provided configuration
    type: list
    elements: dict
    suboptions:
      name:
        description: The name of the interface
        type: str
        required: true
      description:
        description: A textual description of the interface
        type: str
      lower_layer_if:
        description: <1-4094> VLAN ID to be associated with this logical interface
        type: int
      vlan_link_detect:
        description: Enables/Disables the VLAN link detect
        type: bool
      vrf:
        description: Assign a VRF instance to the interface
        type: str
      ip_mtu:
        description: <68-9000> Control Plane IP Maximum Transmission Unit configuration
        type: int
      ipv4:
        description: IPv4 configuration
        type: dict
        suboptions:
          address:
            description: IPv4 address
            type: str
          secondary:
            description: Secondary IPv4 address
            type: list
            elements: str
      ipv6:
        description: IPv6 configuration
        type: dict
        suboptions:
          address:
            description: IPv6 address
            type: list
            elements: str
          enable:
            description: Enable IPv6 on interface
            type: bool
          nd_ra:
            description: Neighbor Discovery - Router Advertisement configuration
            type: dict
            suboptions:
              lifetime:
                description: <0-9000> IPv6 Router Advertisement lifetime configuration
                type: int
              max_interval:
                description: <4-1800> IPv6 Router Advertisement maximum interval configuration
                type: int
              min_interval:
                description: <3-1350> IPv6 Router Advertisement minimum interval configuration
                type: int
              mtu_suppress:
                description: Suppress MTU option from RA messages
                type: bool
              prefix:
                description: IPv6 prefix to be sent in RA messages
                type: list
                elements: dict
                suboptions:
                  ip:
                    description: IPv6 prefix
                    type: str
                    required: true
                  no_advertise:
                    description: Avoid advertising IPv6 prefix to hosts
                    type: bool
                  no_autoconfig:
                    description: Avoid using IPv6 prefix for autoconfiguration
                    type: bool
                  off_link:
                    description: Avoid using IPv6 prefix for on-link determination
                    type: bool
              suppress:
                description: Avoid sending IPv6 Router Advertisement from this interface
                type: bool
  state:
    description:
    - The state the configuration should be left in
    type: str
    choices:
    - merged
    - replaced
    - overridden
    - deleted
    default: merged
"""
EXAMPLES = """
# Using Present

<placeholder for the configuration example prior to module invocation>

- name: Configure L3 Interface
  dmos_l3_interface:
    config:
      - name: test
        description: Hello World
        ip_mtu: 1280
        lower_layer_if: 1
        vlan_link_detect: true
        ipv4:
          address: 192.168.2.1/24
          secondary:
            - 192.168.1.1/24
        ipv6:
          address:
            - 2018::01/64
            - 2019::02/64
          enable: true
          nd_ra:
            lifetime: 700
            max_interval: 600
            min_interval: 198
            mtu_suppress: true
            prefix:
              - ip: 2018::/64
                no_advertise: false
                no_autoconfig: true
                off_link: false

<placeholder for the configuration example after module invocation>


"""
RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The resulting configuration model invocation.
  returned: when changed
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['command 1', 'command 2', 'command 3']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.network.dmos.argspec.l3_interface.l3_interface import L3_interfaceArgs
from ansible.module_utils.network.dmos.config.l3_interface.l3_interface import L3_interface


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=L3_interfaceArgs.argument_spec,
                           supports_check_mode=True)

    result = L3_interface(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()