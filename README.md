z-combinator
------------


A tool to make running a downstream zuul easier.


z-combinator takes the current upstream zuul/layout.yaml, a downstream zuul/layout.yaml, and a config file as inputs. It will produce a zuul/layout.yaml that combines the two zuul/layout.yaml files and sets overrides from the config file.


Usage
-----


```shell
python z-combinator.py > layout.yaml
```


z-combinator takes three files as configuration. See z-combinator-config.yaml for example configuration.



