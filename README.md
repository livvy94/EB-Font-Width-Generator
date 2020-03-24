## A tool to help with custom fonts for your CoilSnake projects

This simple script goes through a font file (currently only `0.png`) and generates the YAML file containing the width in pixels of each character.

I used Visual Studio Code and the Remote-Containers extention to use Docker as my development environment, but if you have Python installed, it should run just fine.

### Requirements:

- pillow, a fork of the Python Image Library
- PyYAML

### Usage:

```bash
pip install -r requirements.txt
python font-length-calc.py [font file]
```
