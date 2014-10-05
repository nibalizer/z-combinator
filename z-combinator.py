
import yaml
import pprint



def merge_project(project, override):
    new_project = {}
    new_project['name'] = project['name']
    # Project sections are
        # template
        # check
        # gate
        # post
        # experimental
        # pre-release
        # release

    sections = [ 'template',
                 'check',
                 'gate',
                 'post',
                 'experimental',
                 'pre-release',
                 'release']

    # Removes first
    deep_merge = [] # Sections we have to deep inspection on

    for sec in sections:
        if sec in project:
            if sec in override['remove']:
                deep_merge.append(sec)
            else:
                # If a section exists in the upstream layout but not
                # in the config section, we can just add it
                new_project[sec] = project['sec']

    for sec in deep_merge:
        new_sec = []
        for job in project[sec]:
            if job in override['remove'][sec]:
                pass
            else:
                new_sec.append(job)
        new_project[sec] = new_sec

    # Adds second

    for sec, contents in override['add'].iteritems():
        new_project[sec] += contents


    return new_project


# Config parse

with open('z-combinator-config.yaml') as f:
    config = yaml.safe_load(f)
f.closed

upstream_file = config['z-combinator']['upstream']
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

# Merge

# jobs

# Merge

# projects

# Merge
new_projects = []
upstream_projects = upstream_layout['projects']
downstream_projects = downstream_layout['projects']
config_projects = config['projects']

# Everything that is downstream specific we just dump in

for project in downstream_projects:
    new_projects.append(project)

# Everything from upstream we just dump in, unless it is in our config

for project in upstream_projects:
    if project['name'] not in config_projects:
        # no ovverrides so we'll just dump it in
        new_projects.append(project)
        #from pdb import set_trace; set_trace()
    elif config_projects[project['name']] == 'delete':
        # Nothing to do here
        pass
    else:
        # Do fancy merging
        merged = merge_project(project, config_projects[project['name']])
        new_projects.append(merged)




new_layout['projects'] = new_projects

#pp.pprint(new_layout['includes'])
#pp.pprint(new_layout['pipelines'])
#pp.pprint(new_layout['projects'])
print yaml.dump(new_layout)



