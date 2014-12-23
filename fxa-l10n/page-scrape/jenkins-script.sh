#npm install phantomjs

export now=`date +%Y%m%d%H%M`
mkdir -p ./pub/fxa-phantom/$now/dev
mkdir -p ./pub/fxa-phantom/$now/prod
mkdir -p ./pub/fxa-phantom/$now/dev-prod

cp fxa-l10n/page-scrape/fxa-content-screens.html ./pub/fxa-phantom/$now/

PUBLIC_URL=https://nightly.dev.lcip.org/ ./fxa-l10n/page-scrape/printAcctPages.sh
cp *.png ./pub/fxa-phantom/$now/dev/

PUBLIC_URL=https://accounts.firefox.com/ ./fxa-l10n/page-scrape/printAcctPages.sh
cp *.png ./pub/fxa-phantom/$now/prod/

cd pub/fxa-phantom/$now
../../../fxa-l10n/page-scrape/diffImages.sh
