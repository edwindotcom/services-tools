// usage: phantomjs loadPage.js
// "use strict";

var page = require('webpage').create(),
    system = require('system'),
    env = system.env,
    args = system.args;

var url = env.PUBLIC_URL || 'https://accounts-latest.dev.lcip.org/';
url += 'signup';
var lang = args[1] || 'en-us';

function waitFor(testFx, onReady, timeOutMillis) {
  var maxtimeOutMillis = timeOutMillis ? timeOutMillis : 3000, //< Default Max Timout is 3s
    start = new Date().getTime(),
    condition = false,
    interval = setInterval(function() {
      if ( (new Date().getTime() - start < maxtimeOutMillis) && !condition ) {
        // If not time-out yet and condition not yet fulfilled
        condition = (typeof(testFx) === "string" ? eval(testFx) : testFx()); //< defensive code
      } else {
        if(!condition) {
          // If condition still not fulfilled (timeout but condition is 'false')
          console.log("'waitFor()' timeout");
          phantom.exit(1);
        } else {
          // Condition fulfilled (timeout and/or condition is 'true')
          // console.log("'waitFor()' finished in " + (new Date().getTime() - start) + "ms.");
          typeof(onReady) === "string" ? eval(onReady) : onReady(); //< Do what it's supposed to do once the condition is fulfilled
          clearInterval(interval); //< Stop this interval
        }
      }
    }, 250); //< repeat check every 250ms
}

function loadPage(address, lang){
  page.customHeaders = {'accept-language': lang};
  page.viewportSize = { width: 400, height: 600 };
  page.open(address, function (status) {
    if (status !== 'success') {
      console.log('FAIL to load the address');
    } else {
      waitFor(function() {
        // Check in the page if a specific element is now visible
        return page.evaluate(function() {
          return $(document.getElementsByClassName('sign-up')).is(":visible");
        });
      }, function() {
          var data = page.evaluate(function () {
            var p = document.getElementsByClassName("privacy-links");
            var fxa = document.getElementById("fxa-signup-header").innerHTML;
            return {"title":document.title,
                    "privacy-links": p[0].textContent.trim(),
                    "fxa-signup-header": fxa};
          });
        console.log('accept-language:'+lang);
        console.log(JSON.stringify(data));
        page.render('fxa-signup-'+lang+'.png');
        phantom.exit();
        });
    }
  });
}

loadPage(url, lang);

