'''
Created on 24 Feb 2013

@author: cooke
'''
from cms.plugin_base import CMSPluginBase
from models import SvgPluginEditor
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

class SvgPluginPublisher(CMSPluginBase):
    model = SvgPluginEditor
    name = _("Svg Plugin")
    render_template = "cmsplugin_filer_svg/svg_plugin.html"
    text_enabled = True
    admin_preview = True

    def render(self, context, instance, placeholder):
        context.update({
            'object':instance,
            'placeholder':placeholder,
        })
        return context
plugin_pool.register_plugin(SvgPluginPublisher)

