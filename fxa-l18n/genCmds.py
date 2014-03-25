langs = ["cs", "cy", "de", "es", "fr", "fy", "hu", "it", "ko", "lt", "nb-NO", "nl", "pl", "pt-BR", "rm", "ru", "sk", "sq", "sr", "sr-LATN", "sv", "zh-CN", "zh-TW"]
for lang in langs:
    # Create Accounts
    #print "$COMMAND --email %s@restmail.net --lang %s create >& /dev/null" % (lang, lang)
    
    # print restmail text recieved
    print "./getRestmailText %s@restmail.net" % lang
