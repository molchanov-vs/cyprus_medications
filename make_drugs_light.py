import json
from utils import load_json, dump_json

def main() -> None:

    drugs = load_json('drugs.json')

    for d in drugs:
        del d["29-03-2024"]
        del d["05-12-2023"]

    
    dump_json('drugs_light.json', drugs)


if __name__ == "__main__":
    main()
    print('Done!')