import json

def fix_comments(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
        
    for cell in nb.get('cells', []):
        if cell.get('cell_type') == 'code':
            source = "".join(cell.get('source', []))
            if 'fonte: https://www.kaggle.com/datasets/piterfm' in source:
                cell['source'] = ["# Fonte dos dados (Hugging Face): https://huggingface.co/datasets/debs-b/uefa-euro"]

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)

fix_comments("/home/debs/canal_debs_b/eda-uefa/analise_UEFA_completo.ipynb")
fix_comments("/home/debs/canal_debs_b/eda-uefa/analise_UEFA_aula.ipynb")
