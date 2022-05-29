# Export plugin for sungather providing a prometheus metric.


## Usage

* Install this package.
* Add it to your SunGather configuration under `exports`:

```sh
  - name: prometheus
  	module: sungather_prometheus_exporter 
    enabled: True     # [Optional] Default is False
    # port: 5055      # [Optional] Default is 5055
    # host: localhost # [Optional] Default is localhost
    # prefix: some_   # [Optional] Prefix for prometheus metric names
```