# coding: utf-8

import rapidfork.views.index as index

urls = [
    (r'^/$', index.MainHandler),
    (r'^/api/demo', index.APIDemoHandler),
]
