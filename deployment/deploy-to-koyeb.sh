#!/bin/bash 

set -e

KOYEB_ACCESS_TOKEN="${KOYEB_ACCESS_TOKEN}"
KOYEB_SERVICE_ID="${KOYEB_SERVICE_ID}"

echo "Installing Koyeb CLI"
curl -fsSL https://raw.githubusercontent.com/koyeb/koyeb-cli/master/install.sh | sh
export PATH=$HOME/.koyeb/bin:$PATH

echo "Redeploying service"
koyeb services redeploy $KOYEB_SERVICE_ID --token $KOYEB_ACCESS_TOKEN