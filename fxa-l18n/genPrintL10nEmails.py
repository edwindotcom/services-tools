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
          "zh-TW",
          "xx"]
print '#!/bin/sh'

print 'epoch=$(date +%s)'
print 'export COMMAND="./ve/bin/fxa-client --password 12345678"'

for lang in langs:
    print "$COMMAND --email %s$epoch@restmail.net --lang %s create &> /dev/null" % (lang, lang)

print 'sleep 5'

for lang in langs:
    print "./getRestmailText %s$epoch@restmail.net" % lang

for lang in langs:
    print "$COMMAND --email %s$epoch@restmail.net destroy &> /dev/null" % (lang)
