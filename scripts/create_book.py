import nbformat as nbf
import glob
import yaml
from os import path
import json
import copy
from jinja2 import Template

# ******* Paths for notebooks ********
attack_paths = {
    "TA0001" : "01_initial_access",
    "TA0002" : "02_execution",
    "TA0003" : "03_persistence",
    "TA0004" : "04_privilege_escalation",
    "TA0005" : "05_defense_evasion",
    "TA0006" : "06_credential_access",
    "TA0007" : "07_discovery",
    "TA0008" : "08_lateral_movement",
    "TA0009" : "09_collection",
    "TA0011" : "11_command_and_control",
    "TA0010" : "10_exfiltration",
    "TA0040" : "40_impact"
}

# ******* Datasets Summary *********
summary_table = [
    {
        "platform" : "Windows",
        "dataset" : []
    },
    {
        "platform" : "Linux",
        "dataset" : []
    },
    {
        "platform" : "Mac",
        "dataset" : []
    },
    {
        "platform" : "AWS",
        "dataset" : []
    }
]

# ******* Initial TOC Template ********
with open('templates/toc_template.json') as json_file:
    toc_template = json.load(json_file)

# ******** Open every metadata yaml file available ****************
print("[+] Opening metadata yaml files..")
metadata_files = glob.glob(path.join(path.dirname(__file__), "..", "datasets/metadata", "*.yaml"))
metadata_loaded = [yaml.safe_load(open(metadata_file).read()) for metadata_file in metadata_files]

# ******** Translating YAML files to Notebooks ****************
print("\n[+] Translating YAML files to notebooks..")
for metadata in metadata_loaded:
    print("  [>>] Processing {} {} file..".format(metadata['id'], metadata['title']))
    nb = nbf.v4.new_notebook() 
    nb['cells'] = []
    # *** TITLE ****
    nb['cells'].append(nbf.v4.new_markdown_cell("# {}".format(metadata['title'])))
    # *** METADATA ****
    nb['cells'].append(nbf.v4.new_markdown_cell("## Metadata"))
    if metadata['mordor_environment']:
        mordor_environment = metadata['mordor_environment']
    else:
        mordor_environment = ''
    if 'script' in metadata['simulation_framework']:
        simulation_script = metadata['simulation_framework']['script']
    else:
        simulation_script = ''
    if metadata['adversary_view']:
        adversary_view = metadata['adversary_view']
    else:
        adversary_view = ''
    nb['cells'].append(nbf.v4.new_markdown_cell(
        """
|                   |    |
|:------------------|:---|
| id                | {} |
| author            | {} |
| creation date     | {} |
| platform          | {} |
| Mordor Environment| {} |
| Simulation Type   | {} |
| Simulation Tool   | {} |
| Simulation Script | {} |
| Mordor Dataset    | {} |""".format(metadata['id'], metadata['author'], metadata['creation_date'], metadata['platform'], mordor_environment, metadata['simulation_framework']['type'], metadata['simulation_framework']['name'], simulation_script, metadata['dataset']['file'])
    ))
    # *** DATASET DESCRIPTION ****
    nb['cells'].append(nbf.v4.new_markdown_cell("""## Dataset Description
{}""".format(metadata['description'])))
    # *** ADVERSARY VIEW ****
    nb['cells'].append(nbf.v4.new_markdown_cell("""## Adversary View
```
{}
```""".format(metadata['adversary_view'])))
    # *** EXPLORE DATASET ****
    nb['cells'].append(nbf.v4.new_markdown_cell("## Explore Mordor Dataset"))
    nb['cells'].append(nbf.v4.new_markdown_cell("### Initialize Analytics Engine"))
    nb['cells'].append(nbf.v4.new_code_cell(
        """from openhunt.mordorutils import *
spark = get_spark()"""
    ))
    nb['cells'].append(nbf.v4.new_markdown_cell("### Download & Process Mordor File"))
    nb['cells'].append(nbf.v4.new_code_cell(
        """mordor_file = "{}"
registerMordorSQLTable(spark, mordor_file, "mordorTable")""".format(metadata['dataset']['file'])
    ))
    nb['cells'].append(nbf.v4.new_markdown_cell("### Get to know your data"))
    nb['cells'].append(nbf.v4.new_code_cell(
        """df = spark.sql(
    '''
SELECT channel, COUNT(1)
FROM mordorTable
GROUP BY channel
    '''
)
df.show(10,False)
        """))

    platform = metadata['platform'].lower()
    # ***** Update Summary Tables *******
    for table in summary_table:
        if platform in table['platform'].lower():
            for attack in metadata['attack_mappings']:
                for tactic in attack['tactics']:
                    metadata['location'] = attack_paths[tactic]
                    if metadata not in table['dataset']:
                        table['dataset'].append(metadata)

    # ***** Update main TOC template and creating notebook *****
    for attack in metadata['attack_mappings']:
        for to in toc_template:
            if "/notebooks/small/{}/{}".format(platform,platform) in to.values():
                for section in to['sections']:
                    for tactic in attack['tactics']:
                        if attack_paths[tactic] in section['url']:
                            metadataDict = {
                                "url" : "/notebooks/small/{}/{}/{}".format(platform,attack_paths[tactic], metadata['id']),
                                "not_numbered" : True
                            }
                            if metadataDict not in section['subsections']:
                                print("    [>>] Adding {} to {} path..".format(metadata['id'], attack_paths[tactic]))
                                section['subsections'].append(metadataDict)
                                print("    [>>] Writing {} as a notebook to {}..".format(metadata['title'], attack_paths[tactic]))
                                nbf.write(nb, "../docs/content/notebooks/small/{}/{}/{}.ipynb".format(platform,attack_paths[tactic],metadata['id']))

# ****** Removing empty lists ********
print("\n[+] Removing empty platforms and empty lists..")
for to in toc_template[:]:
    if 'sections' in to.keys() and len(to['sections']) > 0:
        for section in to['sections'][:]:
            if 'subsections' in section and not section['subsections']:
                print("  [>>] Removing {} ..".format(section['url']))
                to['sections'].remove(section)

# ****** Creating Datasets Summaries ******
print("\n[+] Creating ATT&CK navigator layers for each platform..")
# Reference: https://github.com/mitre-attack/car/blob/master/scripts/generate_attack_nav_layer.py#L30-L45
for summary in summary_table:
    if len(summary['dataset']) > 0:
        techniques_mappings = dict()
        for dataset in summary['dataset']:
            metadata = dict()
            metadata['name'] = dataset['title']
            metadata['value'] = dataset['id'] 
            for coverage in dataset['attack_mappings']:
                technique = coverage['technique']
                if technique not in techniques_mappings:
                    techniques_mappings[technique] = []
                    techniques_mappings[technique].append(metadata)
                elif technique in techniques_mappings:
                    if metadata not in techniques_mappings[technique]:
                        techniques_mappings[technique].append(metadata)
        
        VERSION = "2.2" 
        NAME = "THP {} Analytics".format(summary['platform'])
        DESCRIPTION = "Analytics covered by the Threat Hunter Playbook {} detection notebooks".format(summary['platform'])
        DOMAIN = "mitre-enterprise"
        PLATFORM = summary['platform'].lower()

        print("  [>>] Creating navigator layer for {} metadatas..".format(summary['platform']))
        thp_layer = {
            "description": DESCRIPTION,
            "name": NAME,
            "domain": DOMAIN,
            "version": VERSION,
            "techniques": [
                {
                    "score": 1,
                    "techniqueID" : k,
                    "metadata": v
                } for k,v in techniques_mappings.items()
            ],
            "gradient": {
                "colors": [
                    "#ffffff",
                    "#66fff3"
                ],
                "minValue": 0,
                "maxValue": 1
            },
            "legendItems": [
                {
                    "label": "Datasets researched",
                    "color": "#66fff3"
                }
            ]
        }
        open('../docs/content/notebooks/small/{}/{}.json'.format(PLATFORM,PLATFORM), 'w').write(json.dumps(thp_layer))
    
print("\n[+] Creating dataset summary tables for each platform..")
summary_template = Template(open('templates/summary_template.md').read())
for summary in summary_table:
    if len(summary['dataset']) > 0:
        print("  [>>] Creating summary table for {} datasets..".format(summary['platform']))
        summary_for_render = copy.deepcopy(summary)
        markdown = summary_template.render(summary=summary_for_render)
        open('../docs/content/notebooks/small/{}/{}.md'.format(summary['platform'].lower(),summary['platform'].lower()), 'w').write(markdown)

# ******* Update Jupyter Book TOC File *************
print("\n[+] Writing final TOC file for Jupyter book..")
with open(r'../docs/_data/toc.yml', 'w') as file:
    yaml.dump(toc_template, file, sort_keys=False)