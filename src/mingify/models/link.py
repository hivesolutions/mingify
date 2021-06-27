#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier
import appier_extras

from . import base

class Link(base.MingifyBase):

    url = appier.field(
        index = True,
        description = "URL"
    )

    hash = appier.field(
        index = True
    )

    @classmethod
    def validate(cls):
        return super(Link, cls).validate() + [
            appier.not_null("url"),
            appier.not_empty("url"),

            appier.not_null("hash"),
            appier.not_empty("hash"),
            appier.not_duplicate("hash", cls._name())
        ]


    @classmethod
    def list_names(cls):
        return ["url", "hash"]

    @classmethod
    def order_name(cls):
        return ["url", -1]

    @classmethod
    @appier.operation(
        name = "Create link",
        parameters = (
            ("URL", "url", str),
            ("Hash", "hash", str)
        ),
        factory = True
    )
    def create_link_s(cls, url, hash = None):
        link = cls(url = url)
        if not hash: link.hash = "asdd"
        return link
