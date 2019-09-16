#!/usr/bin/python

import json

from ansible.module_utils.basic import AnsibleModule

from ansible.module_utils.dmos import dmos_argument_spec
from ansible.module_utils.dmos import check_args
from ansible.module_utils.dmos import get_diff, edit_config
from ansible.module_utils.dmos import validate_ip, is_v4


def parse_commands(module, warnings):
    commands = []
    state_prefix = '' if module.params['state'] == 'present' else 'no '

    if module.params['syslog'] != None:
        if validate_ip(module.params['syslog']):
            command = '{0}log syslog {1}'.format(
                state_prefix, module.params['syslog'])
            commands.append(command)
        else:
            warnings.append('Invalid ip format')

    if module.params['severity'] != None:
        commands.append(
            '{0}log severity {1}'.format(state_prefix, module.params['severity']))

    return commands


def main():
    """ main entry point for module execution
    """
    backup_spec = dict(
        filename=dict(),
        dir_path=dict(type='path')
    )
    argument_spec = dict(
        src=dict(type='path'),
        syslog=dict(type='str'),
        severity=dict(choices=['alert', 'critical', 'emergency',
                              'error', 'informational', 'notice', 'warning']),
        state=dict(choices=['absent', 'present'], default='present')
    )

    argument_spec.update(dmos_argument_spec)

    module = AnsibleModule(argument_spec=argument_spec,
                           supports_check_mode=True)

    result = {'changed': False}

    warnings = list()
    check_args(module, warnings)

    candidates = parse_commands(module, warnings)

    result['warnings'] = warnings
    if candidates:
        candidate = get_diff(module=module, candidates=candidates)

        if candidate:
            result['changes'] = candidate

            if not module.check_mode:
                response = edit_config(module=module, candidate=candidate)
                result['response'] = response['response']

            result['changed'] = True

    module.exit_json(**result)


if __name__ == '__main__':
    main()
