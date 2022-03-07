# {{platform_name}}

## ATT&CK Navigator View

<iframe src="https://mitre-attack.github.io/attack-navigator/enterprise/#layerURL=https%3A%2F%2Fraw.githubusercontent.com%2FOTRF%2Fmordor%2Fmaster%2Fdocs%2Fnotebooks%2Fatomic%2F{{platform_name|lower}}%2F{{platform_name|lower}}.json&tabs=false&selecting_techniques=false" width="950" height="450"></iframe>

## {{summary|length}} Datasets

|Created|Dataset|Description|Tags|Contributors|
| :---| :---| :---| :---| :---|
{% for s in summary|sort(attribute='creation_date', reverse=True) %}|{{s['creation_date']}} |[{{s['title']}}](https://securitydatasets.com/notebooks/atomic/{{s['platform'][0]|lower}}/{{s['tactic_name']}}/{{s['id']}}.html) |{{s['description']}} | {{s['tags']}}| {% for contributor in s['contributors'] %}{% set handle = contributor.split('@') %} [{{contributor}}](http://twitter.com/{{handle[1]}}){% if not loop.last %}, {% endif %}{% endfor %} |
{% endfor %}