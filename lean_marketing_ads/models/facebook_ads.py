# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#

from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.business import Business

def update_ad_account(self):
    api_access = self.env['res.company'].sudo().search_read([],['id', 'fb_business_id', 'fb_access_token', 'fb_app_id', 'fb_app_secret'])
    for bsn in api_access:
        if bsn['fb_business_id'] != None and bsn['fb_business_id'] != None and bsn['fb_access_token'] != None and bsn['fb_app_id'] != None and bsn['fb_app_secret'] != None:
            FacebookAdsApi.init(bsn['fb_app_id'], bsn['fb_app_secret'], bsn['fb_access_token'] )
            my_business = Business(bsn['fb_business_id'])
            fields = ['id', 'account_id', 'name','currency', 'age','balance','disable_reason', 'account_status']
            accounts = my_business.get_owned_ad_accounts(fields=fields)
            for account in accounts:
                
            
            

            
            
    