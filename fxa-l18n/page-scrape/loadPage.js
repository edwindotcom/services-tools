// usage: phantomjs loadPage.js
// "use strict";

var page = require('webpage'),
    system = require('system'),
    env = system.env,
    args = system.args;

var url = env.PUBLIC_URL || 'https://accounts-latest.dev.lcip.org/signup';
var lang = args[1];

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

function loadPage(address, headers){
  page = require('webpage').create(),
  // page.settings.userAgent = "User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.101 Safari/537.11";
  page.customHeaders = headers;
  page.open(address, function (status) {
    if (status !== 'success') {
      console.log('FAIL to load the address');
    } else {
      // console.log(page.content);
        waitFor(function() {
          // Check in the page if a specific element is now visible
          return page.evaluate(function() {
            return $(document.getElementsByClassName('sign-up')).is(":visible");
          });
        }, function() {
            var data = page.evaluate(function () {
              var p = document.getElementsByClassName("privacy-links");
              priv = p[0].textContent;
              var fxa = document.getElementById("fxa-signup-header").innerHTML;
              // fxa = fxa[0].textContent;
              return {"title":document.title,
                  "privacy-links": priv,
                  "fxa-signup-header": fxa};
            });
          console.log(JSON.stringify(data));
          phantom.exit();
          // page.render('fxa-signup.png');
        });
    }
  });
}

loadPage(url, {'accept-language': lang});

