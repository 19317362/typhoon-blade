# Copyright (c) 2017 Tencent Inc.
# All rights reserved.
#
# Author: Li Wenting <wentingli@tencent.com>
# Date:   February 22, 2017

"""
This module defines the global build target attributes,
such as bits: 32/64, profile: debug/release.

"""


# Global target attributes object
attributes = None


class TargetAttributes(object):
    """Build target attributes. """
    def __init__(self, options):
        self.options = options

    @property
    def bits(self):
        return int(self.options.m)

    @property
    def arch(self):
        if self.options.m == '32':
            return 'i386'
        else:
            return 'x86_64'

    def is_debug(self):
        return self.options.profile == 'debug'

