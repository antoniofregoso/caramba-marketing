 # -*- coding: utf-8 -*-

from odoo import models, fields, api

PIXEL_EVENTS = [
        ('AddPaymentInfo','Add payment information'),
        ('AddToCart','Add To chart'),
        ('AddToWishlist','Add To wish list'),
        ('CompleteRegistration','Complete Registration'),
        ('Contact','Contact'),
        ('CustomizeProduct','Customoze product'),
        ('Donate','Donate'),
        ('FindLocation','Find Location'),
        ('InitiateCheckout','Initialize Checkout'),
        ('Lead','Lead'),
        ('PageView','Page View'),
        ('Purchase','Purchase'),
        ('Schedule','Schedule'),
        ('Search','Search'),
        ('StartTrial','Start Trial'),
        ('SubmitApplication','Submit Application'),
        ('Subscribe','Suscribe'),
        ('ViewContent','View Content'),
        ]


class WebsiteFacebookPixel(models.Model):    
    _name = 'website.facebook_pixel'
    _description = 'Facebook Pixel'
    
    name = fields.Char('Name', required=True)
    page_id = fields.Many2one('Page', required=True)
    event = fields.Selection(PIXEL_EVENTS, string="Event")
    content_category = fields.Char('Content Category', help="Category of the page/product.")
    content_ids = fields.Char('Content Ids', help="Product IDs associated with the event, such as SKUs (e.g. ['ABC123', 'XYZ789']).")
    content_name = fields.Char('Content Name', help="Name of the page/product.")
    content_type = fields.Char('Content Type', help="Either product or product_group based on the content_ids or contents being passed. If the IDs being passed in content_ids or contents parameter are IDs of products then the value should be product. If product group IDs are being passed, then the value should be product_group.")
    contents = fields.Char('Contents', help="An array of JSON objects that contains the quantity and the International Article Number (EAN) when applicable, or other product or content identifier(s). id and quantity are the required fields. e.g. [{'id': 'ABC123', 'quantity': 2}, {'id': 'XYZ789', 'quantity': 2}].")
    currency = fields.Many2one('Concurrency', help="The currency for the value specified.")
    num_items = fields.Char('Menu Items', help="Used with InitiateCheckout event. The number of items when checkout was initiated.")
    predicted_ltv = fields.Char('Predicted LTV', help="Predicted lifetime value of a subscriber as defined by the advertiser and expressed as an exact value.")
    search_string = fields.Char('Search String', help="Used with the Search event. The string entered by the user for the search.")
    status = fields.Boolean('Status', help="Used with the CompleteRegistration event, to show the status of the registration.")
    value = fields.Char('Value', help="The value of a user performing this event to the business.")
    
     
    
    