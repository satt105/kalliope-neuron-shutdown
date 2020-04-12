# The neuron shutdown
## Synopsis

the neurons allow the raspberry to stop more cleanly and safely

## Installation

```bash
kalliope install --git-url https://github.com/satt105/kalliope-neuron-shutdown.git
```

##### Options
| parameter      | required | default |
|----------------|----------|---------|
|   shutdown     |   yes    |   no   |
|    reboot      |   yes    |   no    |

##### Synapses example

``` yml
  - name: "shutdown"
    signals:
      - order: "this is an example of stop"
    neurons:
      - shutdown:
          action: "shutdown"
```

## Notes
the neuron was developed by the kalliope dream team.
