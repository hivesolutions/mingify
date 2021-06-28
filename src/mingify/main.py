#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier
import appier_extras

class MingifyApp(appier.WebApp):

    def __init__(self, *args, **kwargs):
        appier.WebApp.__init__(
            self,
            name = "mingify",
            parts = (
                appier_extras.AdminPart,
            ),
            *args, **kwargs
        )

    def _version(self):
        return "0.1.1"

    def _description(self):
        return "Mingify"

    def _observations(self):
        return "Simple URL minification service"

if __name__ == "__main__":
    app = MingifyApp()
    app.serve()
else:
    __path__ = []
