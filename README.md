z-combinator
------------


A tool to make running a downstream zuul easier.


z-combinator takes the current upstream zuul/layout.yaml, a downstream zuul/layout.yaml, and a config file as inputs. It will produce a zuul/layout.yaml that combines the two zuul/layout.yaml files and sets overrides from the config file.



zuul
----

Zuul, http://ci.openstack.org/zuul/, is a 'gate master' used by openstack to control merging multiple proposed patches across interdependent projects. 


Zuul's configuration is in layout.yaml. The ci-openstack infrastructure has a config file that is open source: http://git.openstack.org/cgit/openstack-infra/project-config/tree/zuul/layout.yaml. z-combinator operates on the upstream configuration file to produce one suitable for downstream use.


Usage
-----


Look at the the example configuration provided.


```shell
python z-combinator.py > layout.yaml
```


z-combinator takes three files as configuration. See z-combinator-config.yaml for example configuration.



