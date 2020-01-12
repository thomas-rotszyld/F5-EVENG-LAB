#!/usr/bin/python
import copy

class FilterModule(object):
    def filters(self):
        return {
            'monitors_list': self.monitors_list
        }

    def monitors_list(self, dummy_variable, http_monitor_select, https_monitor_select, vs_name):
        monitors_list = []
        if http_monitor_select == 'ENABLED':
            http_monitor = {'http_monitor_enabled': True, 'http_monitor_name': vs_name + '_http_monitor'}
        else:
            http_monitor = {'http_monitor_enabled': False, 'http_monitor_name': None}

        monitors_list.append(http_monitor)

        if https_monitor_select == 'ENABLED':
            https_monitor = {'https_monitor_enabled': True, 'https_monitor_name': vs_name + '_https_monitor'}
        else:
            https_monitor = {'https_monitor_enabled': False, 'https_monitor_name': None}

        monitors_list.append(https_monitor)   

        return monitors_list
