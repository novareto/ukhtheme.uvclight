# -*- coding: utf-8 -*-
# Copyright (c) 2007-2013 NovaReto GmbH
# cklinger@novareto.de


import uvclight
from . import IDGUVRequest, get_template
from dolmen.message import receive
from dolmen.template import ITemplate
from grokcore.component import adapter, implementer
from uvc.content.interfaces import IContent
from uvc.design.canvas import menus, managers
from uvc.design.canvas.viewlets import MenuViewlet
from zope import interface


class Tabs(uvclight.ViewletManager):
    uvclight.name('tabs')
    uvclight.context(uvclight.Interface)
    uvclight.implements(managers.ITabs)


class Navigation(uvclight.ViewletManager):
    uvclight.name('navigation')
    uvclight.context(uvclight.Interface)


class PageTop(uvclight.ViewletManager):
    uvclight.name('pagetop')
    uvclight.context(uvclight.Interface)
    uvclight.implements(managers.IPageTop)


class Headers(uvclight.ViewletManager):
    uvclight.name('headers')
    uvclight.context(uvclight.Interface)
    uvclight.implements(managers.IHeaders)


class AboveContent(uvclight.ViewletManager):
    uvclight.name('above-body')
    uvclight.context(uvclight.Interface)
    uvclight.implements(managers.IAboveContent)


class BelowContent(uvclight.ViewletManager):
    uvclight.name('below-body')
    uvclight.context(uvclight.Interface)
    uvclight.implements(managers.IBelowContent)


class Footer(uvclight.ViewletManager):
    uvclight.name('footer')
    uvclight.context(uvclight.Interface)
    uvclight.implements(managers.IFooter)


class BGHeader(uvclight.Viewlet):
    uvclight.layer(IDGUVRequest)
    uvclight.viewletmanager(managers.IPageTop)
    uvclight.order(30)
    template = get_template('bgheader.cpt')
    
    def application_url(self):
        return self.view.application_url()


class ObjectActionMenuViewlet(MenuViewlet):
    uvclight.viewletmanager(managers.IAboveContent)
    uvclight.context(IContent)
    uvclight.order(10)
    menu = menus.ContextualActionsMenu
 

class AddMenuViewlet(MenuViewlet):
    uvclight.viewletmanager(managers.IAboveContent)
    uvclight.order(20)
    menu = menus.AddMenu


class GlobalMenuViewlet(MenuViewlet):
    uvclight.layer(IDGUVRequest)
    uvclight.viewletmanager(managers.IPageTop)
    uvclight.order(10)
    menu = menus.GlobalMenu

    
class PersonalMenuViewlet(MenuViewlet):
    uvclight.viewletmanager(managers.IPageTop)
    uvclight.order(20)
    menu = menus.PersonalMenu
    template = get_template('personalpreferencestemplate.cpt')

    name = u'Personal menu'

    def getFooter(self):
        menu = menus.FooterMenu(self.context, self.request, self.view)
        menu.update()
        return menu.entries

    def getPersonal(self):
        menu = menus.PersonalMenu(self.context, self.request, self.view)
        menu.update()
        return menu.entries


class DocumentActionsViewlet(MenuViewlet):
    uvclight.viewletmanager(managers.IAboveContent)
    uvclight.order(20)

    template = get_template('documentactionstemplate.cpt')
    name = u'Document actions'
    id = u'documentactionsviewlet'

    def update(self):
        self.menu = menus.DocumentActionsMenu(
            self.context, self.request, self.view)
        self.menu.update()


class NavigationMenuViewlet(MenuViewlet):
    uvclight.viewletmanager(Navigation)
    uvclight.order(30)
    menu = menus.NavigationMenu
    template = get_template('navigationtemplate.cpt')

    id = u'globalmenuviewlet'

    def getNavigation(self):
        menu = menus.NavigationMenu(self.context, self.request, self.view)
        menu.update()
        return menu.entries

    def getUser(self):
        menu = menus.UserMenu(self.context, self.request, self.view)
        menu.update()
        return menu.entries

    def getRenderableItems(self):
       return list()

    def getQuicklinks(self):
        menu = menus.Quicklinks(self.context, self.request, self.view)
        menu.update()
        return menu.entries


class FlashMessages(uvclight.Viewlet):
    uvclight.order(2)
    uvclight.layer(IDGUVRequest)
    uvclight.viewletmanager(managers.IAboveContent)
    template = uvclight.get_template('flash.cpt', __file__)

    def update(self):
        self.messages = [msg.message for msg in receive()]


@adapter(menus.IGlobalMenu, interface.Interface)
@implementer(ITemplate)
def global_template(context, request):
    return get_template('globalmenutemplate.cpt')
