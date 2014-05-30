Summary: a few shell scripts to create accounts in for each l18n accept-language type and to print those emails via stdout.

Known Issues: redirecting stdout to text file borks on ascii, for now, just copy and paste from shell

Usage:
0. git clone git@github.com:edmoz/fxa-python-client.git
1. cd fxa-python-client
2. git checkout add-lang-option
* Waiting for PR merge from upstream
3. cp all files from this into fxa-python-client
4. Create Accts
./createAccts.sh
5. Print them in shell
./printAcctEmails.sh
6. Delete Accts
./destroyAccts.sh
