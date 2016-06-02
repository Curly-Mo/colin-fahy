(function(){
    window.addEventListener('hashchange', load_page);
    load_page();
})();

var transitionend = ('WebkitTransition' in document.documentElement.style) ? 'webkitTransitionEnd' : 'transitionend'
function load_page(){
    var url = location.hash.slice(1) || 'projects';
    var path = url + '.html';
   	var content = document.getElementById('content');
    content.style.overflow = 'hidden';
    // Remove current content
    var div = (content.firstElementChild||content.firstChild);
    if(div != null){
        div.classList.add('off-bottom');
        div.addEventListener(transitionend, function(e){
            content.removeChild(this);
        });
    }
    div = document.createElement('div');
    div.classList.add('slide-content');
    div.classList.add('off-right');
    content.insertBefore(div, content.firstChild);
   	var xhr = new XMLHttpRequest();
   	xhr.onreadystatechange = function (e) { 
    	if (xhr.readyState == 4 && xhr.status == 200) {
     		div.innerHTML = xhr.responseText;
            var scripts = div.getElementsByTagName('script')
            for (var n = 0; n < scripts.length; n++){
                eval(scripts[n].innerHTML);
            }
            div.classList.remove('off-right');
            div.addEventListener(transitionend, function(e){
                content.style.overflow = 'auto';
            });
    	}
   	}
 	xhr.open('GET', path, true);
 	xhr.setRequestHeader('Content-type', 'text/html');
 	xhr.send();
}

//RESPONSIVE CLOSE TAB
(function() {
    "use strict";
    var toggles = document.querySelectorAll(".cmn-toggle-switch");

    for (var i = toggles.length - 1; i >= 0; i--) {
		var toggle = toggles[i];
		toggleHandler(toggle);
    };
    function toggleHandler(toggle) {
    toggle.addEventListener( "click", function(e) {
      e.preventDefault();
      (this.classList.contains("active") === true) ? this.classList.remove("active") : this.classList.add("active");
    });
    }

})();
