(function() {
    'use strict';
    var website = odoo.website;
    website.odoo_website = {};
    
    website.snippet.options.timeline_clone_item = website.snippet.Option.extend({
        onFocus: function() {
            alert("On focus!");
        }
    })
    
})();