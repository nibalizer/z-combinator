
import yaml
import pprint


new_layout = {}

with open('upstream-layout.yaml') as f:
    upstream_layout  = yaml.safe_load(f)
f.closed

with open('downstream-layout.yaml') as f:
    downstream_layout = yaml.safe_load(f)
f.closed

# There are several main trees inside layout.yaml

# incudes
# This tree is low-churn, simply consume from downstream

new_layout['includes'] = downstream_layout['includes']

# pipelines
# This tree is low-chrun, simply consume from downstream

new_layout['pipelines'] = downstream_layout['pipelines']


pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(x)

pp.pprint(new_layout['includes'])
pp.pprint(new_layout['pipelines'])


new_layout


