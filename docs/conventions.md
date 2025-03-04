# Conventions

This document describes the conventions used in this project. Including:

- [File Structure](#file-structure)
- [Naming](#naming)
- [Code Style](#code-style)
- [Documentation](#documentation)
- [Testing](#testing)
- [Versioning](#versioning)

## File Structure

The file structure is as follows:

```
.
├── src/
│   └── knightrade/
│       ├── __init__.py
│       ├── module1.py
│       └── module2.py
├── tests/
│   ├── __init__.py
│   ├── test_module1.py
│   └── test_module2.py
├── docs/
│   ├── version_log.md
│   ├── conventions.md
│   ├── doc_module1.md
│   └── proposal.md
├── .gitignore
├── LICENSE
├── README.md
└── pyproject.toml
```

## Naming

Example: `snake_case`, `CamelCase`, `CONSTANT_CASE`, `_private`, `__protected`.

- **Modules**: `snake_case`.
- **Classes**: `CamelCase`.
    - **Abstract Classes**: prefwx with `ABC`. E.g. `ABCClassName`. **Exceptions**: suffix with `Error`. E.g. `ClassNameError`.
    - **Attributes**: 
        - **Private**: prefix with `_`. E.g. `_attribute_name`.
        - **Protected**: prefix with `__`. E.g. `__attribute_name`.
- **Functions**: `snake_case`.
- **Variables**: `snake_case`.
- **Constants**(Global Variables): `CONSTANT_CASE`.
- **Documents**: `docs/doc_module_name.md`

## Code Style

- **Indentation**: 4 spaces.
- **Line Length**: 79 characters.
- **Imports** order:
    - **Standard Library**.
    - **Third Party**.
    - **Local**.
    - **Type Annotations**.
    - Put import before from
- **Type Annotations**: Use type hints.
- **Docstrings** example:

```python
def function_name(arg1: int, 
                  arg2: str) -> None:
    """
    Short description.

    :param arg1: Description.
    :param arg2: Description.
    :return: Description.

    Long description.
    """
    pass
```

## Documentation

- **README**: 
    - **Description**: Short description of the project.
    - **Installation**: How to install the project.
    - **Usage**: How to use the project.
    - **Contributing**: How to contribute to the project.
    - **License**: License of the project.
- **Module Doc**: 
    - **Description**: Short description of the module.
    - **Usage**: How to use the module.
    - **Example**: Example of the module.
    - **Methods**: List of methods.
    - **Classes**: List of classes.

Module Doc Example `doc_module_name.md`:

```markdown
# Module Name

Short description.

## Usage

How to use the module.

## Example

Example of the module.

## Methods

### Method Name

Long description.

#### Parameters and Returns

- `param1`: Description.
- `param2`: Description.
- `return`: Description.

#### Example

Important method should have an example.

## Classes

### ClassName

Short description.

#### Attributes

- `attribute1`: Description.
- `attribute2`: Description.

#### Methods

- `method1`: Description.
- `method2`: Description.

#### Example

Important class should have an example.

```

## Testing

- **Test Files**: `tests/test_module_name.py`.
- using `unittest` module.

Example:

```python
import unittest
from src.knightrade.module1 import function_name

class TestModule1(unittest.TestCase):

    def test_function_name(self):
        self.assertEqual(function_name(1, 2), 3)

if __name__ == '__main__':
    unittest.main()
```

## Versioning

1. Need pull request to merge to `main` branch.
2. Git commit message should follow the conventions:
    - `[<sprint_number>-<type>] short description`
    - Example, for sprint 1:
        - `[1-feature] add new feature`
        - `[1-bug] fix bug`
        - `[1-doc] update documentation`
3. Each commit should have:
    - code changes
    - corresponding test
    - corresponding documentation
4. version number:
    - `major.minor.patch`
    - start with `0.0.0`, first release is `1.0.0`

