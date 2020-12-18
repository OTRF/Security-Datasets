import nbformat as nbf
import glob
import yaml
from os import path
import json
import copy
from jinja2 import Template

# ******** Translating YAML files to Notebooks ****************
print("\n[+] Translating YAML files to notebooks..")
metadata = yaml.safe_load(open("../../datasets/metadata/SDLIN-201110081941.yaml").read())

print("  [>>] Processing {} {} file..".format(metadata['id'], metadata['title']))
# **** METADATA ****
notebook_metadata = {
    "kernelspec": {
        "display_name": "PySpark_Python3",
        "language": "python",
        "name": "pyspark3"
    },
    "language_info": {
        "codemirror_mode": {
            "name": "ipython",
            "version": 3
        },
        "file_extension": ".py",
        "mimetype": "text/x-python",
        "name": "python",
        "nbconvert_exporter": "python",
        "pygments_lexer": "ipython3",
        "version": "3.7.3"
    }
}
# **** INITIALIZE NOTEBOOK **** 
nb = nbf.v4.new_notebook(metadata=notebook_metadata)
nb['cells'] = []
# *** TITLE ****
nb['cells'].append(nbf.v4.new_markdown_cell("# {}".format(metadata['title'])))
# *** METADATA ****
nb['cells'].append(nbf.v4.new_markdown_cell("## Metadata"))
techniques = []
tactics = []
if metadata['attack_mappings']:
    for tech in metadata['attack_mappings']:
        technique_name = tech['technique']
        technique_url= "https://attack.mitre.org/techniques/" + technique_name
        if tech['sub-technique']:
            technique_name = technique_name + '.' + tech['sub-technique']
            technique_url = technique_url + "/" + tech['sub-technique']
        technique = "[{}]({})".format(technique_name,technique_url)
        techniques.append(technique)
        if tech['tactics']:
            for tact in tech['tactics']:
                tactic_name = tact
                tactic_url = "https://attack.mitre.org/tactics/" + tactic_name
                tactic = "[{}]({})".format(tactic_name,tactic_url)
                tactics.append(tactic)
table = """
|                   |    |
|:------------------|:---|
| Author            | {} |
| Creation Date     | {} |
| Modification Date | {} |
| Tactics           | {} |
| Techniques        | {} |
| Tags              | {} |""".format(metadata['author'], metadata['creation_date'], metadata['modification_date'], tactics, techniques, metadata['tags'])
nb['cells'].append(nbf.v4.new_markdown_cell(table))
# *** DATASET DESCRIPTION ****
nb['cells'].append(nbf.v4.new_markdown_cell("""## Dataset Description
{}""".format(metadata['description'])))
# *** DOWNLOAD DATASETS ****
nb['cells'].append(nbf.v4.new_markdown_cell("## Datasets Downloads"))
table = """
| Dataset Type | Link   |
|:-------------|:-------|"""
table_list = [table]
for dataset in metadata['files']:
    table_list.append("| {} | [{}]({}) |".format(dataset['type'],dataset['link'], dataset['link']))
table_strings = '\n'.join(map(str, table_list))
nb['cells'].append(nbf.v4.new_markdown_cell(table_strings))
# *** NOTEBOOKS ***
nb['cells'].append(nbf.v4.new_markdown_cell("""## Notebooks
Notebooks created by the community leveraging the mordor datasets"""))
table = """
| Author | Name | Link |
|:-------|:-----|:-----|"""
table_list = [table]
if metadata['notebooks']:
    for notebook in metadata['notebooks']:
        table_list.append("| {} | {} | [{}]({}) |".format(notebook['project'],notebook['name'],notebook['link'],notebook['link']))
table_strings = '\n'.join(map(str, table_list))
nb['cells'].append(nbf.v4.new_markdown_cell(table_strings))
# *** SIMULATION METADATA ****
nb['cells'].append(nbf.v4.new_markdown_cell("## Simulation Plan"))
table = """
| Environment | Tool Type | Module |
|:------------|:----------|:-------|"""
table_list = [table]
simulation_environment = ''
if metadata['simulation']['environment']:
    simulation_environment = metadata['simulation']['environment']
if metadata['simulation']['tools']:
    for tool in metadata['simulation']['tools']:
        table_list.append("| {} | {} | [{}]({}) |".format(simulation_environment,tool['type'],tool['module'],tool['script']))
table_strings = '\n'.join(map(str, table_list))
nb['cells'].append(nbf.v4.new_markdown_cell(table_strings))
# *** ADVERSARY VIEW ****
adversary_view = ''
if metadata['simulation']['adversary_view']:
    adversary_view = metadata['simulation']['adversary_view']
nb['cells'].append(nbf.v4.new_markdown_cell("""## Adversary View
```
{}
```""".format(adversary_view)))
# *** EXPLORE DATASET ****
nb['cells'].append(nbf.v4.new_markdown_cell("## Explore Mordor Dataset"))
nb['cells'].append(nbf.v4.new_markdown_cell("### Initialize Analytics Engine"))
nb['cells'].append(nbf.v4.new_code_cell(
    """from openhunt.mordorutils import *
spark = get_spark()"""
))
nb['cells'].append(nbf.v4.new_markdown_cell("### Download & Process Mordor File"))
for dataset in metadata['files']:
    if dataset['type'] != 'Network':
        dataset_file = dataset['link']
        break
nb['cells'].append(nbf.v4.new_code_cell(
    """mordor_file = "{}"
registerMordorSQLTable(spark, mordor_file, "mordorTable")""".format(dataset_file)
))
nb['cells'].append(nbf.v4.new_markdown_cell("### Get to know your data"))
if metadata['platform'] == 'Windows':
    nb['cells'].append(nbf.v4.new_code_cell("""df = spark.sql(
'''
SELECT Hostname,Channel,EventID, Count(*) as count
FROM mordorTable
GROUP BY Hostname,Channel,EventID
ORDER BY count DESC
'''
)
df.show(truncate=False)"""))
else:
    nb['cells'].append(nbf.v4.new_code_cell("""df = spark.sql(
'''
SELECT *
FROM mordorTable
'''
)
df.show(1, vertical=True)"""))

platform = metadata['platform'].lower()

# ***** Update main TOC template and creating notebook *****
nbf.write(nb, '{}_{}.ipynb'.format(platform,metadata['id']))