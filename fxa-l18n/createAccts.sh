#!/bin/sh
export PUBLIC_URL=https://api-accounts.stage.mozaws.net/
export COMMAND="./ve/bin/fxa-client --password 12345678"
$COMMAND --email ca@restmail.net --lang ca create
$COMMAND --email cs@restmail.net --lang cs create
$COMMAND --email cy@restmail.net --lang cy create
$COMMAND --email de@restmail.net --lang de create
$COMMAND --email es@restmail.net --lang es create
$COMMAND --email fr@restmail.net --lang fr create
$COMMAND --email fy@restmail.net --lang fy create
$COMMAND --email he@restmail.net --lang he create
$COMMAND --email hu@restmail.net --lang hu create
$COMMAND --email id@restmail.net --lang id create
$COMMAND --email it@restmail.net --lang it create
$COMMAND --email ko@restmail.net --lang ko create
$COMMAND --email lt@restmail.net --lang lt create
$COMMAND --email nb-NO@restmail.net --lang nb-NO create
$COMMAND --email nl@restmail.net --lang nl create
$COMMAND --email pa@restmail.net --lang pa create
$COMMAND --email pl@restmail.net --lang pl create
$COMMAND --email pt-BR@restmail.net --lang pt-BR create
$COMMAND --email rm@restmail.net --lang rm create
$COMMAND --email ru@restmail.net --lang ru create
$COMMAND --email sk@restmail.net --lang sk create
$COMMAND --email sq@restmail.net --lang sq create
$COMMAND --email sr@restmail.net --lang sr create
$COMMAND --email sr-LATN@restmail.net --lang sr-LATN create
$COMMAND --email sv@restmail.net --lang sv create
$COMMAND --email tr@restmail.net --lang tr create
$COMMAND --email zh-CN@restmail.net --lang zh-CN create
$COMMAND --email zh-TW@restmail.net --lang zh-TW create
