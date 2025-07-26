import json

adversaries = 0
with open("json/adversaries.json", "r", encoding="utf-8-sig") as file:
    adversaries = json.load(file)
environments = 0
with open("json/environments.json", "r", encoding="utf-8-sig") as file:
    environments = json.load(file)

def convert_environment(json):
    md = """---
statblock: inline
---

```statblock
layout: Daggerheart Environment
"""
    for key, value in json.items():
        if key == "feats":
            md += "feats:\n"
            for name, desc in [feat.values() for feat in value]:
                desc_raw = repr(desc)[1:-1]
                md += f' - name: "{name}"\n   desc: "{desc_raw}"\n'
        else:
            md += f'{key}: "{value}"\n'
    md += "```"
    return md

def convert_adversary(json):
    md = """---
statblock: inline
---

```statblock
layout: Daggerheart Adversary
"""
    for key, value in json.items():
        if key == "feats":
            md += "feats:\n"
            for name, desc in [feat.values() for feat in value]:
                md += f' - name: "{name}"\n   desc: "{desc}"\n'
        else:
            md += f'{key}: "{value}"\n'
    md += "```"
    return md

for adversary in adversaries:
    folder = f""
    with open(f"../adversaries/Tier {adversary['tier']}/{adversary['name']}.md", "w") as file:
        file.write(convert_adversary(adversary))

for environment in environments:
    with open(f"../environments/Tier {environment['tier']}/{environment['name']}.md", "w") as file:
        file.write(convert_environment(environment))

