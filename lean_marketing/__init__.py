# -*- coding: utf-8 -*-

from . import models

def _set_blacklisted_out(cr, registry):
            
    cr.execute("UPDATE ir_model_fields"
        " SET website_form_blacklisted=false"
        " WHERE model = 'crm.lead' and name in ('content_id', 'term_id')")