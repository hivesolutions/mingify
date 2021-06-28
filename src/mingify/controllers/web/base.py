#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

import mingify

class BaseController(appier.Controller):

    @appier.route("/<str:hash>", "GET", priority = -1)
    def gateway(self, hash):
        link = mingify.Link.get(hash = hash)
        return self.redirect(link.url, absolute = True)
