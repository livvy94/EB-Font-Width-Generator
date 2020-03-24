## A tool to help with custom fonts for your CoilSnake projects

This simple script goes through a font file (currently only `0.png`) and generates the YAML file containing the width in pixels of each character.

I used Visual Studio Code and the Remote-Containers extention to use Docker as my development environment, but if you have Python installed, it should run just fine.

### Usage:

```bash
pip install -r requirements.txt
python font-length-calc.py
```