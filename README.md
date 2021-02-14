# cumin-py

Python Binding for [cumin](https://github.com/cympfh/cumin).

## setup

### from PyPI

```bash
pip install cumin-py
```

### from Github

```bash
clone this, then
pip install .
```

## Usage

```python
import cumin

cumin.loads("""
struct S { x: Int, y: Int = 0 }
let a = S(1);
[a, a]
""")
# => [{'x': 1, 'y': 0}, {'x': 1, 'y': 0}]

cumin.load("conf.cumin")  # read ./conf.cumin
```
