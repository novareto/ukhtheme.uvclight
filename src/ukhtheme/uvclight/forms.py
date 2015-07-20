# -*- coding: utf-8 -*-

import uvclight

from . import IDGUVRequest
from cromlech.browser import ITemplate
from dolmen.forms.base import interfaces
from dolmen.forms.base.interfaces import IForm
from dolmen.forms.base.widgets import ActionWidget
from dolmen.forms.viewlet.interfaces import IInlineForm
from grokcore.component import adapter, implementer, adapts


class ActionWidget(ActionWidget):
    adapts(
        interfaces.IAction,
        interfaces.IFieldExtractionValueSetting,
        IDGUVRequest)

    def htmlClass(self):
        return "action btn btn-default"


#@adapter(IForm, IDGUVRequest)
#@implementer(ITemplate)
#def form_template(context, request):
#    """default template for the menu"""
#    return uvclight.get_template('form.cpt', __file__)


@adapter(IInlineForm, IDGUVRequest)
@implementer(ITemplate)
def form_template(context, request):
    """default template for the menu"""
    return uvclight.get_template('viewletform.cpt', __file__)
