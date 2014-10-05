
import yaml
import pprint


# Config parse

with open('z-combinator-config.yaml') as f:
    config = yaml.safe_load(f)
f.closed

upstream_file= config['z-combinator']['upstream']
downstream_file = config['z-combinator']['downstream']


pp = pprint.PrettyPrinter(indent=4)
new_layout = {}

with open(upstream_file) as f:
    upstream_layout  = yaml.safe_load(f)
f.closed

with open(downstream_file) as f:
    downstream_layout = yaml.safe_load(f)
f.closed

# There are several main trees inside layout.yaml

# incudes
# This tree is low-churn, simply consume from downstream

new_layout['includes'] = downstream_layout['includes']

# pipelines
# This tree is low-chrun, simply consume from downstream

new_layout['pipelines'] = downstream_layout['pipelines']


# project-templates

# Go through the merging process

pp.pprint(new_layout['includes'])
pp.pprint(new_layout['pipelines'])




