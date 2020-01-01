# {{summary['platform']}}
{% if summary['dataset']|length > 0 %}
## ATT&CK Navigator View

<iframe src="https://mitre-attack.github.io/attack-navigator/enterprise/#layerURL=https%3A%2F%2Fraw.githubusercontent.com%2Fhunters-forge%2Fmordor%2Fmaster%2Fdocs%2Fcontent%2Fnotebooks%2Fsmall%2F{{summary['platform']|lower}}%2F{{summary['platform']|lower}}.json&tabs=false&selecting_techniques=false" width="950" height="450"></iframe>

## Table View

|Created|Dataset|Description|Simulator|Author|
| :---| :---| :---| :---| :---|
{% for s in summary['dataset']|sort(attribute='title') %}|{{s['creation_date']}} |[{{s['title']}}](https://mordordatasets.com/notebooks/small/{{s['platform']|lower}}/{{s['location']}}/{{s['id']}}.html) |{{s['description']}} |{{s['simulation_framework']['name']}}|{{s['author']}} |
{% endfor %}{% endif %}