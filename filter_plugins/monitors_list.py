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
            monitors_list.append(vs_name + '_http_monitor')
        elif https_monitor_select == 'ENABLED':
            monitors_list.append(vs_name + '_http_monitor')

        return monitors_list
