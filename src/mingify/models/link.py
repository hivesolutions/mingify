#!/usr/bin/python
# -*- coding: utf-8 -*-

import binascii

import appier

from . import base

class Link(base.MingifyBase):

    url = appier.field(
        index = True,
        meta = "url",
        description = "URL"
    )

    hash = appier.field(
        index = True
    )

    sequence = appier.field(
        type = int,
        index = "all",
        increment = True
    )

    @classmethod
    def validate(cls):
        return super(Link, cls).validate() + [
            appier.not_null("url"),
            appier.not_empty("url"),
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
        if hash: link.hash = hash
        link.save()
        return link

    def post_create(self):
        base.MingifyBase.post_create(self)
        if not self.hash:
            sequence_s = "%d" % self.sequence
            sequence_s = appier.legacy.bytes(sequence_s)
            sequence_h = binascii.hexlify(sequence_s)
            self.hash = appier.legacy.str(sequence_h)
            self.save()
