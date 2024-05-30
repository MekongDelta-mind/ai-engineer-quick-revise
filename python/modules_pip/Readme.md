> You don;t have the luxury of going through the "External Libs" like in Pycharm. Although if you ever find it difficult to understnad which pip package is your project using then follow the below:


To find the path of a package installed in your Python environment from the terminal, you can use the `pip show` command or the `python -m site` module. Here's how you can do it:

### Using `pip show`
1. **Activate your conda environment (if necessary):**
   ```bash
   conda activate your_env_name
   ```

2. **Use `pip show` to find the package path:**
   ```bash
   pip show <package_name>
   ```

This command will display various details about the package, including its location.

For example, to find the path of the `numpy` package:
```bash
pip show numpy
```

You will get output similar to this:
```
Name: numpy
Version: 1.21.0
Summary: NumPy is the fundamental package for array computing with Python.
Home-page: https://www.numpy.org
Author: Travis E. Oliphant et al.
Author-email: numpy-discussion@python.org
License: BSD
Location: /path/to/your/env/lib/python3.8/site-packages
Requires: 
Required-by: 
```

The `Location` field shows where the package is installed.

### Using Python's `site` module
1. **Activate your conda environment (if necessary):**
   ```bash
   conda activate your_env_name
   ```

2. **Use the `site` module to get site-packages paths:**
   ```bash
   python -m site
   ```

This will display the paths that Python uses to look for packages, including `site-packages` directories where packages are typically installed.

For example:
```bash
python -m site
```

Output might look like:
```
sys.path = [
    '/path/to/your/current/directory',
    '/path/to/your/env/lib/python3.8/site-packages',
    # ... other paths ...
]
USER_BASE: '/home/your_username/.local' (exists)
USER_SITE: '/home/your_username/.local/lib/python3.8/site-packages' (exists)
ENABLE_USER_SITE: True
```

### Checking the package's location from within a Python script
You can also find the installation path of a package from within a Python script or interactive session:

```python
import <package_name>
print(<package_name>.__file__)
```

For example, to find the path of the `numpy` package:
```python
import numpy
print(numpy.__file__)
```

This will print the path to the `numpy` package, showing you exactly where it is installed.

Using these methods, you can easily determine the installation path of any package in your Python environment.


> The `{package_path}/RECORD` would have the actual path to the python package where teh python files would be present.
Like in the example after installing python-docx: 

* you get the package locaiton from the conda command to go to the folder `/home/prabin_nayak/anaconda3/envs/cs50_env/lib/python3.12/site-packages/python_docx-1.1.2.dist-info` in the env folder.
* but the actual python files are present in the path `/home/prabin_nayak/anaconda3/envs/cs50_env/lib/python3.12/site-packages/docx` , which is mentioned in `RECORD` found in the `package_path` which is here `python_docx-1.1.2.dist-info/RECORD`