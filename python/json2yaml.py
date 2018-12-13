#!/usr/bin/env python
import sys
import json
import yaml

with open(sys.argv[1]) as f:
        print yaml.safe_dump(json.load(f), default_flow_style=False)
