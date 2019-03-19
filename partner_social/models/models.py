 # -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResPartner(models.Model):

    _inherit = 'res.partner'
    
    
    facebook = fields.Char('Facebook')
    facebook_page = fields.Char('Facebook Page')
    instagram = fields.Char('Instagram')
    twitter = fields.Char('Twitter')
    linkedin = fields.Char('LinkedIn')
    youtube = fields.Char('Youtube')
    pinterest = fields.Char('Pinterest')
    github = fields.Char('GitHub')
    blog1 = fields.Char('Blog 1')
    blog2 = fields.Char('Blog 2')
    blog3 = fields.Char('Blog 3')