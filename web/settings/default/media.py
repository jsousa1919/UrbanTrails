# -*- coding: utf-8 -*-
__author__ = 'norad'

import os
APP_ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../'))

STATIC_ROOT = os.path.abspath(os.path.join(APP_ROOT, 'static'))
STATICFILES_DIRS = (
    os.path.abspath(os.path.join(APP_ROOT, 'prestatic')),
)

STATIC_URL = '/static/'
STATIC_DOC_ROOT = APP_ROOT + STATIC_URL

PIPELINE_YUI_BINARY = '/usr/bin/yui-compressor'
PIPELINE_YUI_CSS_ARGUMENTS = ''
PIPELINE_YUI_JS_ARGUMENTS = ''

PATENT_TEMPLATE_DIRECTORY = APP_ROOT + '/templates/'

PIPELINE_JS = {
    'third_party': {'source_filenames': (
        'js/third_party/jquery-1.9.1.js',
    ), 'output_filename': 'js/third_party.js'},
    'common': {'source_filenames': (
        'js/site.js',
        'js/common.js',
        'js/map.js',
        'js/mapmaker.js',
    ), 'output_filename': 'js/global.js'},
    'deferred': {'source_filenames': ('js/events.js',),
                 'output_filename': 'js/deferred.js',
                 'extra_context': {'defer': True}},
}

PIPELINE_CSS = {
    'style': {'source_filenames': (
        'css/base.css',
        'css/map.css',
    ), 'output_filename': 'css/style.css'},
}

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
PIPELINE_YUI_JS_ARGUMENTS = '--nomunge'