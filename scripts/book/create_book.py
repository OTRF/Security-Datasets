import nbformat as nbf
import glob
import yaml
import os
import json
import copy
from jinja2 import Template

###### Variables #####
current_directory = os.path.dirname(__file__)
templates_directory = os.path.join(current_directory, "templates")
toc_template = os.path.join(templates_directory, "toc_template.json")
datasets_directory = os.path.join(current_directory, "../..", "datasets")
atomic_metadata_directory = os.path.join(datasets_directory, "atomic/_metadata")
compound_metadata_directory = os.path.join(datasets_directory, "compound/_metadata")
docs_directory = os.path.join(current_directory, "../../docs")
notebooks_directory = os.path.join(docs_directory, "notebooks")
toc_file = os.path.join(docs_directory, "_toc.yml")
summary_table_template = os.path.join(templates_directory, "summary_template.md")

###########################
##### Tactic Mappings #####
###########################
tactic_maps = {
    "TA0001" : "initial_access",
    "TA0002" : "execution",
    "TA0003" : "persistence",
    "TA0004" : "privilege_escalation",
    "TA0005" : "defense_evasion",
    "TA0006" : "credential_access",
    "TA0007" : "discovery",
    "TA0008" : "lateral_movement",
    "TA0009" : "collection",
    "TA0011" : "command_and_control",
    "TA0010" : "exfiltration",
    "TA0040" : "impact",
    "TA0043" : "reconnaissance",
    "TA0042" : "resource_development"
}

###########################
##### Dataset Summary #####
###########################
summary_table = {
    "atomic" : {},
    "compound" : []
}

#############################
##### Load TOC Template #####
#############################
print("[+] Loading TOC template..")
with open(toc_template) as json_file:
    toc_template_loaded = json.load(json_file)

#######################################
##### Process Datasets YAML Files #####
#######################################
print("[+] Reading metadata yaml files..")
atomic_metadata_files = glob.glob(os.path.join(atomic_metadata_directory, "*.yaml"))
compound_metadata_files = glob.glob(os.path.join(compound_metadata_directory, "*.yaml"))
metadata_files = atomic_metadata_files + compound_metadata_files
metadata_loaded = [yaml.safe_load(open(metadata_file, encoding="utf8").read()) for metadata_file in metadata_files]

###########################################
##### Convert YAML files to notebooks #####
###########################################
print("\n[+] Converting YAML files to notebooks..")
for metadata in metadata_loaded:
    print("  [>>] Processing {} {} file..".format(metadata['id'], metadata['title']))
    ##### Initialize Notebook object #####
    nb = nbf.v4.new_notebook()
    nb['cells'] = []
    # *** TITLE ****
    nb['cells'].append(nbf.v4.new_markdown_cell("# {}".format(metadata['title'])))
    # *** METADATA ****
    nb['cells'].append(nbf.v4.new_markdown_cell("## Metadata"))
    contributors = ','.join(metadata['contributors'])
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
                    tactic_url = "https://attack.mitre.org/tactics/" + tact
                    tactic = "[{}]({})".format(tact,tactic_url)
                    if tactic not in tactics:
                        tactics.append(tactic)
    techniques = ','.join(techniques)
    tactics = ','.join(tactics)
    tags = metadata['tags']
    if isinstance(tags, list):
        tags = ','.join(metadata['tags'])
    table = """
|                   |    |
|:------------------|:---|
| Contributors      | {} |
| Creation Date     | {} |
| Modification Date | {} |
| Tactics           | {} |
| Techniques        | {} |
| Tags              | {} |""".format(contributors, metadata['creation_date'], metadata['modification_date'], tactics, techniques, tags)
    nb['cells'].append(nbf.v4.new_markdown_cell(table))
    # *** DATASET DESCRIPTION ****
    nb['cells'].append(nbf.v4.new_markdown_cell("""## Dataset Description
{}""".format(metadata['description'])))
    # *** DOWNLOAD DATASETS ****
    nb['cells'].append(nbf.v4.new_markdown_cell("## Datasets Downloads"))
    table = """
| Type | Link   |
|:-------------|:-------|"""
    table_list = [table]
    for dataset in metadata['files']:
        table_list.append("| {} | [{}]({}) |".format(dataset['type'],dataset['link'], dataset['link']))
    table_strings = '\n'.join(map(str, table_list))
    nb['cells'].append(nbf.v4.new_markdown_cell(table_strings))
    # *** SIMULATION METADATA ****
    nb['cells'].append(nbf.v4.new_markdown_cell("## Simulation Metadata"))
    simulation_keys = list(metadata['simulation'].keys())
    if 'environment' in simulation_keys and 'environment_link' in simulation_keys:
        table = """
| Name | link |
|:-----|:-----|
| {}   | [{}]({})   |""".format( metadata['simulation']['environment'], metadata['simulation']['environment_link'], metadata['simulation']['environment_link'])
        table_list = [table]
        nb['cells'].append(nbf.v4.new_markdown_cell("### Environment"))
        nb['cells'].append(nbf.v4.new_markdown_cell(table))
    table = """
| type | Name | Module |
|:-----|:-----|--------|"""
    table_list = [table]
    if 'tools' in simulation_keys:
        for tool in metadata['simulation']['tools']:
            table_list.append("| {} | {} | [{}]({}) |".format(tool['type'],tool['name'],tool['module'],tool['script']))
        table_strings = '\n'.join(map(str, table_list))
        nb['cells'].append(nbf.v4.new_markdown_cell("### Tools"))
        nb['cells'].append(nbf.v4.new_markdown_cell(table_strings))
    # *** ADVERSARY VIEW ****
    if 'adversary_view' in simulation_keys:
        adversary_view = ''
        adversary_view = metadata['simulation']['adversary_view']
        nb['cells'].append(nbf.v4.new_markdown_cell("""## Adversary View
```
{}
```""".format(adversary_view)))
    if metadata['type'] == 'atomic':
        # *** EXPLORE DATASET ****
        nb['cells'].append(nbf.v4.new_markdown_cell("## Explore Datasets"))
        nb['cells'].append(nbf.v4.new_markdown_cell("### Download & Decompress Dataset"))
        for dataset in metadata['files']:
            if dataset['type'] != 'Network':
                dataset_file = dataset['link']
                break
        nb['cells'].append(nbf.v4.new_code_cell("""import requests
from zipfile import ZipFile
from io import BytesIO

url = {}
zipFileRequest = requests.get(url)
zipFile = ZipFile(BytesIO(zipFileRequest.content))
datasetJSONPath = zipFile.extract(zipFile.namelist()[0])""".format(dataset_file)))
        nb['cells'].append(nbf.v4.new_markdown_cell("### Read JSON File"))
        nb['cells'].append(nbf.v4.new_code_cell("""from pandas.io import json

df = json.read_json(path_or_buf=datasetJSONPath, lines=True)"""))
        nb['cells'].append(nbf.v4.new_markdown_cell("### Access Security Events"))
        if metadata['platform'][0] == 'Windows':
            nb['cells'].append(nbf.v4.new_code_cell("df.groupby(['Channel']).size().sort_values(ascending=False)"))
        else:
            nb['cells'].append(nbf.v4.new_code_cell("""df.head(1)"""))
    # ***** REFERENCES *****
    reference_list = ["## References"]
    if 'references' in list(metadata.keys()) and isinstance(metadata['references'], list):
        for ref in metadata['references']:
            reference_list.append("* [{}]({}) ".format(ref, ref))
        reference_strings = '\n'.join(map(str, reference_list))
    nb['cells'].append(nbf.v4.new_markdown_cell(reference_strings))

    ################################
    ##### update Summary Table #####
    ################################
    if metadata['type'] == 'atomic':
        platform = metadata['platform'][0].lower()
        metadata['tactic_name'] = tactic_maps[metadata['attack_mappings'][0]['tactics'][0]]
        if platform not in list(summary_table['atomic'].keys()):
            summary_table['atomic'][platform] = []
        summary_table['atomic'][platform].append(metadata)
    else:
        summary_table['compound'].append(metadata)

    ###########################
    ##### Write Notebooks #####
    ###########################
    if metadata['type'] == 'atomic':
        print("  [>>] Creating atomic notebook..")
        for attack in metadata['attack_mappings']:
            for tactic in attack['tactics']:
                platform_directory = "{}/atomic/{}".format(notebooks_directory,platform)
                platform_intro_file = "{}/intro.md".format(platform_directory)
                tactic_directory = "{}/{}".format(platform_directory,tactic_maps[tactic])
                tactic_intro_file = "{}/intro.md".format(tactic_directory)
                # creating directory for notebooks if they have not been created yet
                # platform directory
                if not os.path.exists(platform_directory):
                    print("    [>] Creating platform directory: {}".format(platform_directory))
                    os.makedirs(platform_directory)
                # platform intro file
                if not os.path.exists(platform_intro_file):
                    print("    [>] Creating platform intro file: {}".format(platform_intro_file))
                    with open(platform_intro_file, 'x') as f:
                        f.write('# {}'.format(platform))
                # tactic directory
                if not os.path.exists(tactic_directory):
                    print("    [>] Creating platform directory: {}".format(tactic_directory))
                    os.makedirs(tactic_directory)
                # tactic intro file
                if not os.path.exists(tactic_intro_file):
                    print("    [>] Creating platform intro file: {}".format(tactic_intro_file))
                    with open(tactic_intro_file, 'x') as f:
                        f.write('# {}'.format(tactic_maps[tactic]))
                
                # Write notebooks to file..
                notebook_path = "{}/{}.ipynb".format(tactic_directory,metadata['id']) 
                print("    [>] writing notebook to {}".format(notebook_path))
                nbf.write(nb, notebook_path)
    else:
        print("  [>>] Creating compound notebook..")
        compound_directory = "{}/compound".format(notebooks_directory)
        # creating directory for notebooks if they have not been created yet
        if not os.path.exists(compound_directory):
            print("    [>] Creating compound directory: {}".format(compound_directory))
            os.makedirs(compound_directory)

        # Write notebooks to file..
        notebook_name = metadata['title'].replace(" ", "")
        notebook_path = "{}/{}.ipynb".format(compound_directory,notebook_name) 
        print("    [>] Writing notebook to {}".format(notebook_path))
        nbf.write(nb, notebook_path)

###############################
##### Update TOC template #####
###############################
print("\n[+] Updating TOC file..")
for part in toc_template_loaded['parts']:
    if 'Atomic Datasets' == part['caption']:
        # Processing Platforms
        platform_list = list(summary_table['atomic'].keys())
        for platform in platform_list:
            # processing tactics
            print("  [>>] Creating tactic sections for {}..".format(platform))
            tactics_list = []
            for dataset in summary_table['atomic'][platform]:
                for attack in dataset['attack_mappings']:
                    for tactic in attack['tactics']:
                        tactic_name = tactic_maps[tactic]
                        if tactic_name not in tactics_list:
                            tactics_list.append(tactic_name)
            tactic_sections = []
            for tn in tactics_list:
                tactic_section = {
                    "file": "notebooks/atomic/{}/{}/intro".format(platform, tn),
                    "sections": []
                }
                tactic_sections.append(tactic_section)
            # Processing techniques
            print("  [>>] Adding techniques to tactic sections for {}..".format(platform))          
            for dataset in summary_table['atomic'][platform]:
                for section in tactic_sections:
                    for attack in dataset['attack_mappings']:
                        for tactic in attack['tactics']:
                            tactic_name = tactic_maps[tactic]
                            if tactic_name in section['file']:
                                dataset_dict = {
                                    "file" : "notebooks/atomic/{}/{}/{}".format(platform,tactic_name, dataset['id'])
                                }
                                if dataset_dict not in section['sections']:
                                    section['sections'].append(dataset_dict)
            # Processing Chapters
            platform_chapter = {
                "file" : "notebooks/atomic/{}/intro".format(platform),
                "sections" : tactic_sections
            }
            part['chapters'].append(platform_chapter)
    elif 'Compound Datasets' == part['caption']:
        doc_name = metadata['title'].replace(" ", "")
        for compound in summary_table['compound']:
            compound_chapter = {
                "file" : "notebooks/compound/{}".format(doc_name)
            }
            part['chapters'].append(compound_chapter)

# ******* Update Jupyter Book TOC File *************
print("\n[+] Writing final TOC file for Jupyter book..")
with open(toc_file, 'w') as file:
    yaml.dump(toc_template_loaded, file, sort_keys=False)

#########################################
##### Create AT&CK Navigator Layers #####
#########################################
print("\n[+] Creating ATT&CK navigator layers..")
# Reference: https://github.com/mitre-attack/car/blob/master/scripts/generate_attack_nav_layer.py#L30-L45
print("[+] Processing atomic techniques..")
for platform in list(summary_table['atomic'].keys()):
    techniques_mappings = dict()
    for dataset in summary_table['atomic'][platform]:
        metadata = dict()
        metadata['name'] = dataset['title']
        metadata['value'] = dataset['id'] 
        for attack in dataset['attack_mappings']:
            technique = attack['technique']
            if attack['sub-technique']:
                technique = technique + '.' + attack['sub-technique']
            if technique not in techniques_mappings:
                techniques_mappings[technique] = []
                techniques_mappings[technique].append(metadata)
            elif technique in techniques_mappings:
                if metadata not in techniques_mappings[technique]:
                    techniques_mappings[technique].append(metadata)
    
    LAYER_VERSION = "4.2"
    NAVIGATOR_VERSION = "4.3"
    NAME = "{} security datasets".format(platform)
    DESCRIPTION = "Datasets created after simulating adversaries in a {} environment".format(platform)
    DOMAIN = "mitre-enterprise"
    if platform == 'aws':
        PLATFORM = ["SaaS","IaaS"]
    elif platform == 'azure':
        PLATFORM = ["SaaS","IaaS","Azure AD","Office 365"]
    elif platform == 'gcp':
        PLATFORM = ["Google Workspace","SaaS","IaaS",]
    else:    
        PLATFORM = platform

    print("  [>>] Creating navigator layer for {} datasets..".format(platform))
    dataset_layer = {
        "description": DESCRIPTION,
        "name": NAME,
        "domain": DOMAIN,
        "versions": {
            "attack": "9",
            "navigator": NAVIGATOR_VERSION,
            "layer": LAYER_VERSION
        },
        "filters": {
            "stages": [
                "act"
            ],
            "platforms": [
                PLATFORM
            ]
        },
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
    open('{}/atomic/{}/{}.json'.format(notebooks_directory, platform.lower(),platform.lower()), 'w').write(json.dumps(dataset_layer))
    
print("\n[+] Creating dataset summary tables for each platform..")
summary_template = Template(open(summary_table_template).read())
for platform in list(summary_table['atomic'].keys()):
    print("  [>>] Creating summary table for {} datasets..".format(platform))
    summary_for_render = copy.deepcopy(summary_table['atomic'][platform])
    markdown = summary_template.render(summary=summary_for_render, platform_name=platform)
    open('{}/atomic/{}/intro.md'.format(notebooks_directory,platform.lower()), 'w').write(markdown)
