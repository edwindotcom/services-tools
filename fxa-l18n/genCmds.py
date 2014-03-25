langs = ["ca", "cs", "cy", "de", "es", "fr", "fy", "he", "hu", "id", "it", "ko", "lt", "nb-NO", "nl", "pa", "pl", "pt-BR", "rm", "ru", "sk", "sq", "sr", "sr-LATN", "sv", "tr", "zh-CN", "zh-TW"]

print '#!/bin/sh'
print 'export PUBLIC_URL=https://api-accounts.stage.mozaws.net/'
print 'export COMMAND="./ve/bin/fxa-client --password 12345678"'

for lang in langs:
    # Create Accounts
    #print "$COMMAND --email %s@restmail.net --lang %s create" % (lang, lang)
    
    # print restmail text recieved
    print "./getRestmailText %s@restmail.net" % lang
