/* copy the pref group below into a user.js file created in profile dir. e.g.
 * Mac: /Users/<user>/Library/Application\ Support/Firefox/Profiles/<obfuscate_chars>.default/user.js
 * Win: C:/Users/Username/Appdata/Roaming/Mozilla/Firefox/Profiles/<obfuscate_chars>.default/user.js
 * Lnx: ~/.mozilla/firefox/<obfuscate_chars>.default/user.js
 * Restart Firefox
*/


// useful

user_pref("browser.shell.checkDefaultBrowser", false);
user_pref("general.warnOnAboutConfig", false);

/*
//prod
user_pref("services.sync.log.appender.file.logOnSuccess", true);
user_pref("identity.fxaccounts.auth.uri", "https://api.accounts.firefox.com/v1");
user_pref("identity.fxaccounts.remote.force_auth.uri", "https://accounts.firefox.com/force_auth?service=sync&context=fx_desktop_v1");
user_pref("identity.fxaccounts.remote.signin.uri", "https://accounts.firefox.com/signin?service=sync&context=fx_desktop_v1");
user_pref("identity.fxaccounts.remote.signup.uri", "https://accounts.firefox.com/signup?service=sync&context=fx_desktop_v1");
user_pref("identity.fxaccounts.settings.uri", "https://accounts.firefox.com/settings");

*/

//stage
user_pref("services.sync.log.appender.file.logOnSuccess", true);
user_pref("identity.fxaccounts.auth.uri", "https://api-accounts.stage.mozaws.net/v1");
user_pref("identity.fxaccounts.remote.force_auth.uri", "https://accounts.stage.mozaws.net/force_auth?service=sync&context=fx_desktop_v1");
user_pref("identity.fxaccounts.remote.signin.uri", "https://accounts.stage.mozaws.net/signin?service=sync&context=fx_desktop_v1");
user_pref("identity.fxaccounts.remote.signup.uri", "https://accounts.stage.mozaws.net/signup?service=sync&context=fx_desktop_v1");
user_pref("identity.fxaccounts.settings.uri", "https://accounts.stage.mozaws.net/settings");
user_pref("services.sync.tokenServerURI", "https://token.stage.mozaws.net/1.0/sync/1.5");


/*
//dev - deployed nightly
user_pref("services.sync.log.appender.file.logOnSuccess", true);
user_pref("identity.fxaccounts.auth.uri", "https://api-accounts.dev.lcip.org/v1");
user_pref("identity.fxaccounts.remote.force_auth.uri", "https://accounts.dev.lcip.org/force_auth?service=sync&context=fx_desktop_v1");
user_pref("identity.fxaccounts.remote.signin.uri", "https://accounts.dev.lcip.org/signin?service=sync&context=fx_desktop_v1");
user_pref("identity.fxaccounts.remote.signup.uri", "https://accounts.dev.lcip.org/signup?service=sync&context=fx_desktop_v1");
user_pref("identity.fxaccounts.settings.uri", "https://accounts.dev.lcip.org/settings");
user_pref("services.sync.tokenServerURI", "https://token.stage.mozaws.net/1.0/sync/1.5");


//dev-latest - auto deploys for every commit
user_pref("services.sync.log.appender.file.logOnSuccess", true);
user_pref("identity.fxaccounts.auth.uri", "https://api-accounts-latest.dev.lcip.org/v1");
user_pref("identity.fxaccounts.remote.force_auth.uri", "https://accounts-latest.dev.lcip.org/force_auth?service=sync&context=fx_desktop_v1");
user_pref("identity.fxaccounts.remote.signin.uri", "https://accounts-latest.dev.lcip.org/signin?service=sync&context=fx_desktop_v1");
user_pref("identity.fxaccounts.remote.signup.uri", "https://accounts-latest.dev.lcip.org/signup?service=sync&context=fx_desktop_v1");
user_pref("identity.fxaccounts.settings.uri", "https://accounts-latest.dev.lcip.org/settings");
user_pref("services.sync.tokenServerURI", "https://token.stage.mozaws.net/1.0/sync/1.5");

*/
