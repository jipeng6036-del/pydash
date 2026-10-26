#!/bin/sh
set -eu
envname="$1"
mkdir -p /work
tar -xf /proof/pydash-candidate-canonical.tar -C /work
cd /work
python -VV
python -m pip install tox
tox -e "$envname"
".tox/$envname/bin/python" -m pip freeze --all > "/proof/pydash-v2-$envname-freeze.txt"
".tox/$envname/bin/python" /proof/pydash-consumer.py > "/proof/pydash-v2-$envname-consumer.json"
