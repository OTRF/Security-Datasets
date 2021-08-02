# {{platform_name}}

## ATT&CK Navigator View

<iframe src="https://mitre-attack.github.io/attack-navigator/enterprise/#layerURL=https%3A%2F%2Fraw.githubusercontent.com%2FOTRF%2Fmordor%2Fmaster%2Fdocs%2Fnotebooks%2Fsmall%2F{{summary['platform']|lower}}%2F{{summary['platform']|lower}}.json&tabs=false&selecting_techniques=false" width="950" height="450"></iframe>

## {{summary|length}} Datasets

|Created|Dataset|Description|Tags|Author|
| :---| :---| :---| :---| :---|
{% for s in summary|sort(attribute='creation_date', reverse=True) %}|{{s['creation_date']}} |[{{s['title']}}](https://securitydatasets.com/notebooks/small/{{s['platform']|lower}}/{{s['location']}}/{{s['id']}}.html) |{{s['description']}} | {{s['tags']}}|{{s['author']}} |
{% endfor %}
