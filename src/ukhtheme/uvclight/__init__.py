# -*- coding: utf-8 -*-

import uvclight
import os
import ukhtheme.resources
from uvc.themes.btwidgets import IBootstrapRequest


class IDGUVRequest(IBootstrapRequest):
    pass


def get_template(name):
    return uvclight.get_template(name, ukhtheme.resources.__file__)
