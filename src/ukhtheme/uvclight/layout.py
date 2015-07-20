# -*- coding: utf-8 -*-

import uvclight
from . import get_template
from zope.interface import Interface
from ukhtheme.resources import maincss, mainjs, tune


class Layout(uvclight.Layout):
    uvclight.context(Interface)

    template = get_template('masterlayout.cpt')

    base = "/"

    def __call__(self, content, **ns):
        maincss.need()
        mainjs.need()
        tune.need()
        site = uvclight.getSite()
        self.title = getattr(site, 'title', 'UVCLight')
        if 'view' in ns:
            if hasattr(ns['view'], 'title'):
                self.title = getattr(ns['view'], 'title', u'UVCLight')
        return uvclight.Layout.__call__(self, content, **ns)
