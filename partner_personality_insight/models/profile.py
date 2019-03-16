# -*- coding: utf-8 -*-

from odoo import models, fields, api

PROFILE_CATEGORIES = [
    ('personality', 'Personality'),
    ('needs', 'Needs'),
    ('values', 'Values'),
    ('behavior', 'Behavior')
    ]

PROFILE_PERSONALITY = [
    ('big5_openness', 'Openness'),
    ('facet_adventurousness','(O) Adventurousness'),
    ('facet_artistic_interests','(O) Artistic interests'),
    ('facet_emotionality','(O) Emotionality'),
    ('facet_imagination','(O) Imagination'),
    ('facet_intellect','(O) Intellect'),
    ('facet_liberalism','(O) Authority-challenging'),
    ('big5_conscientiousness','Conscientiousness'),
    ('facet_achievement_striving','(C) Achievement striving'),
    ('facet_cautiousness','(C) Cautiousness'),
    ('facet_dutifulness','(C) Dutifulness'),
    ('facet_orderliness','(C) Orderliness'),
    ('facet_self_discipline','(C) Self-discipline'),
    ('facet_self_efficacy','(C) Self-efficacy'),
    ('big5_extraversion','Extraversion'),
    ('facet_activity_level','(E) Activity level'),
    ('facet_assertiveness','(E) Assertiveness'),
    ('facet_cheerfulness','(E) Cheerfulness'),
    ('facet_excitement_seeking','(E) Excitement-seeking'),
    ('facet_friendliness','(E) Outgoing'),
    ('facet_gregariousness','(E) Gregariousness'),
    ('big5_agreeableness','Agreeableness'),
    ('facet_altruism','(A) Altruism'),
    ('facet_cooperation','(A) Cooperation'),
    ('facet_modesty','(A) Modesty'),
    ('facet_morality','(A) Uncompromising'),
    ('facet_sympathy','(A) Sympathy'),
    ('facet_trust','(A) Trust'),
    ('big5_neuroticism','Emotional range'),
    ('facet_anger','(N) Fiery'),
    ('facet_anxiety','(N) Prone to worry'),
    ('facet_depression','(N) Melancholy'),
    ('facet_immoderation','(N) Immoderation'),
    ('facet_self_consciousness','(N) Self-consciousness'),
    ('facet_vulnerability','(N) Susceptible to stress'),
    ]

PROFILE_TRAIY = [
    ('need_challenge','Challenge'),
    ('need_closeness','Closeness'),
    ('need_curiosity','Curiosity'),
    ('need_excitement','Excitement'),
    ('need_harmony','Harmony'),
    ('need_ideal','Ideal'),
    ('need_liberty','Liberty'),
    ('need_love','Love'),
    ('need_practicality','Practicality'),
    ('need_self_expression','Self-expression'),
    ('need_stability','Stability'),
    ('need_structure', 'Structure'),
    ('value_conservation', 'Conservation'),
    ('value_openness_to_change', 'Openness to change'),
    ('value_hedonism', 'Hedonism'),
    ('value_self_enhancement', 'Self-enhancement'),
    ('value_self_transcendenc', 'Self-transcendence'),
    ]



class PersonalityTrait(models.Model):
    _name = 'profile.personality_trait'
    _description = 'Personality Insights Profile Trait'
    
    name = fields.Selection(PROFILE_PERSONALITY, string='Name', index=True)
    category = fields.Selection(PROFILE_CATEGORIES, string='Category', index=True)
    percentile = fields.Float('Percentile')
    raw_score = fields.Float('Raw Score')
    significant = fields.Boolean('Significant')
    children = fields.Many2many('profile.personality_trait', 'profile_personality_trait_rel', 'parent_id', 'children_id', string='Facets', help='Facets of the parent category')
    
class Trait(models.Model):
    _name = 'profile.trait'
    _description = 'Generic Insights Profile Trait'
    
    trait_id = fields.Char('Trait Id', required=True)
    name = fields.Char('Name', required=True, index=True)
    category = fields.Selection(PROFILE_CATEGORIES, string='Category')
    percentile = fields.Float('Percentile')
    raw_score = fields.Float('Raw Score')
    significant = fields.Boolean('Significant')
    
class ConsumptionPreferencesType(models.Model):
    _name = 'profile.consumption_preferences_type'
    _description = 'Consumption Preference Type'
    
    consumption_preference_id = fields.Char('Consumtion Preference Id', required=True)
    name = fields.Char('Name', required=True, index=True)
    score = fields.Float('Score')
    consumption_preferences_id = fields.One2many('profile.consumption_preferences', 'preference_type_id', string='Consuption Preferences', copy=True)


class ConsumptionPreferences(models.Model):
    _name = 'profile.consumption_preferences'
    _description = 'Consumption Preferences'
    
    consumption_preference_category_id = fields.Char('Opportunity', required=True, index=True)
    name = fields.Char('Opportunity', required=True, index=True)
    preference_type_id = fields.Many2one('profile.consumption_preferences_type', string='Consuption Preference Type', required=True, ondelete='cascade')
    
class Behavior(models.Model):
    _name = 'profile.behavior'
    _description = 'Profile behavior'
    
    trait_id = fields.Char('Opportunity', required=True)
    name = fields.Char('Opportunity', required=True, index=True)
    category = fields.Char('Opportunity', required=True, index=True)
    percentage = fields.Float('Percentage')
    
    
class Warning(models.Model):
    _name = 'profile.warning'
    _description = 'Warnings'
    
    warning_id = fields.Char('Opportunity', required=True)
    message = fields.Char('Opportunity', required=True)
    
    

class Profile(models.Model):
    _name = 'profile'
    _description = 'Personality Insights Profile'
    
    word_count =
    word_count_message = fields.Char('Word Count Message')
    processed_language =
    personality =
    needs =
    values =
    consumption_preferences =
    behavior = 
    warnings =
    content = 
    partner_id = fields.Many2one('res.partner', string='Customer', index=True, required=True)
    
class ProfileEndpoint(models.Model):
    _name = 'profile.endpoint'
    _description = 'Service Endpoint'
    
    name = fields.Char('Name', required=True)
    url = fields.Char('Url', required=True)
    
    
    
    
    
    