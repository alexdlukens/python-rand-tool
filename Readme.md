# Py-rand-tool

Example MVP snap package for trying out the snapcraft build process. When installed, the snap exposes a cli application "py-rand-tool" which lets users generate a random int or float number. Users can specify the min/max values and generator seed.

```
usage: py-rand-tool [-h] [-v] [-i] [-f] [--min MIN] [--max MAX] [--seed SEED]

Generate a random integer or float.

options:
  -h, --help     show this help message and exit
  -v, --version  show program's version number and exit
  -i, --int      Generate a random integer
  -f, --float    Generate a random float
  --min MIN      Minimum value
  --max MAX      Maximum value
  --seed SEED    Seed value

Made by Alex Lukens in NYC
```