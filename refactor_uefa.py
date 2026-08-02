import json

def process_notebook(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
        
    for cell in nb.get('cells', []):
        if cell.get('cell_type') == 'code':
            source = "".join(cell.get('source', []))
            if 'import kagglehub' in source:
                cell['source'] = [
                    "from huggingface_hub import snapshot_download\n",
                    "import os\n",
                    "import pandas as pd\n",
                    "import glob\n",
                    "import matplotlib.pyplot as plt"
                ]
            elif 'def baixar_dataset_se_nao_existir' in source:
                cell['source'] = [
                    "# Definir o ID do repositório no Hugging Face\n",
                    "repo_id = \"debs-b/uefa-euro\"\n",
                    "\n",
                    "# O snapshot_download baixa e faz o cache dos dados automaticamente!\n",
                    "caminho_dataset = snapshot_download(repo_id=repo_id, repo_type=\"dataset\")\n",
                    "print(f\"Dataset pronto e cacheado em: {caminho_dataset}\")"
                ]
                cell['outputs'] = []
                cell['execution_count'] = None
            elif 'piterfm/football-soccer-uefa-euro-1960-2024' in source and 'baixar_dataset_se_nao_existir' in source:
                cell['source'] = ["# Célula substituída pela integração com o Hugging Face"]
                cell['outputs'] = []
                cell['execution_count'] = None
            elif 'caminho_dataset = "/home/debs/.cache/kagglehub/' in source and 'os.listdir' in source:
                cell['source'] = [
                    "files = os.listdir(caminho_dataset)\n",
                    "files\n"
                ]
                # Keep output if exists, or clear it. Let's clear it to be safe.
                cell['outputs'] = []
                cell['execution_count'] = None
            
            # Find any other mention of kagglehub or that old cache path
            new_source = []
            changed = False
            for line in cell.get('source', []):
                if '/home/debs/.cache/kagglehub/datasets/piterfm/football-soccer-uefa-euro-1960-2024/versions/12' in line:
                    new_source.append(line.replace('/home/debs/.cache/kagglehub/datasets/piterfm/football-soccer-uefa-euro-1960-2024/versions/12', '{caminho_dataset}').replace('"{caminho_dataset}"', 'caminho_dataset').replace("'{caminho_dataset}'", 'caminho_dataset'))
                    changed = True
                else:
                    new_source.append(line)
            
            if changed:
                cell['source'] = new_source

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)

process_notebook("/home/debs/canal_debs_b/eda-uefa/analise_UEFA_completo.ipynb")
process_notebook("/home/debs/canal_debs_b/eda-uefa/analise_UEFA_aula.ipynb")
