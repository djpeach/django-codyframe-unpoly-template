/**
 * Instead of creating files for each component, paste all codyframe component js here.
 *
 * Some helper methods will also be imported. When codyframe component js is pasted,
 *  check for these standalone helper methods and move them to `Util.prototype` instead.
 *  Be sure to update references after moving
 */

/**
 * Util helper methods
 * eg: Util.myHelper = function() {};
 */
function Util () {};

// File#: _1_pre-header
// Usage: codyhouse.co/license
(function() {
	var preHeader = document.getElementsByClassName('js-pre-header');
	if(preHeader.length > 0) {
		for(var i = 0; i < preHeader.length; i++) {
			(function(i){ addPreHeaderEvent(preHeader[i]);})(i);
		}

		function addPreHeaderEvent(element) {
			var close = element.getElementsByClassName('js-pre-header__close-btn')[0];
			if(close) {
				close.addEventListener('click', function(event) {
					event.preventDefault();
					element.classList.add('pre-header--hide');
				});
			}
		}
	}
}());