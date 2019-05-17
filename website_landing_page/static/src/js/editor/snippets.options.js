// Clone timeline item
odoo.define('website_landing_page.snippets.options', function (require) {
    "use strict";


var core = require('web.core');
var Dialog = require('web.Dialog');
var weWidgets = require('web_editor.widget');
var options = require('web_editor.snippets.options');

var _t = core._t;
var qweb = core.qweb;


   
options.registry.timeline = options.Class.extend({
	addItem: function (previewMode, value, $opt) {
		var count = $('main-timeline').length;
		alert(count);
	},
	
	removeItem: function (previewMode, value, $opt) {
		alert('Puto');
	},
	
	onFocus: function () {
		var name = this.$target.attr('id');
		alert(name);
	},
	
	
});
    
});