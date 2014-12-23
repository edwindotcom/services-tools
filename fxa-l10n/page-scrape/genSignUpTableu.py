langs = [ "ca",
          "cs",
          "cy",
          "da",
          "de",
          "en-US",
          "es",
          "es-CL",
          "et",
          "eu",
          "fr",
          "fy",
          "he",
          "hu",
          "id",
          "it",
          "ja",
          "ko",
          "lt",
          "nb-NO",
          "nl",
          "pa",
          "pl",
          "pt",
          "pt-BR",
          "rm",
          "ru",
          "sk",
          "sl",
          "sq",
          "sr",
          "sr-LATN",
          "sv",
          "tr",
          "zh-CN",
          "zh-TW"]

# print '#!/bin/sh'
# print
print '<html><body>'
print '<p>nightly | prod | diff</p>'
for lang in langs:
     print '<p>'
     print '<img src="dev/fxa-signup-%s.png"  title="dev-%s" />' % (lang, lang)
     print '<img src="prod/fxa-signup-%s.png" title="prod-%s" />' % (lang, lang)
     print '<img src="dev-prod/fxa-signup-%s.png" title="diff-%s" />' % (lang, lang)
     print '</p>'
    # print "node_modules/phantomjs/bin/phantomjs fxa-l18n/page-scrape/loadPage.js %s" % lang
print
print '</body></html>'

