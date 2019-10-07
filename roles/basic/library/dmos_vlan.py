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
The module file for dmos_vlan
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
module: dmos_vlan
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
      vlan_id:
        description: <1-4094> VLAN ID
        type: int
      name:
        description: Text name identifying the VLAN (max 32 chars).
        type: str
      interface:
        description: Statically add interfaces to VLANs and remove interfaces from VLANs
        type: str
      tagged:
        description: Set this interface as an tagged member
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

- name: Configure VLANs
  dmos_vlan:
    config:
      - name: Vlan-example
        vlan_id: 10
        interface: gigabit-ethernet-1/1/1
        tagged: 10
    state: merged

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
from ansible.module_utils.network.dmos.argspec.vlan.vlan import VlanArgs
from ansible.module_utils.network.dmos.config.vlan.vlan import Vlan


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=VlanArgs.argument_spec,
                           supports_check_mode=True)

    result = Vlan(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
