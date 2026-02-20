# ML Modules test report (.venv)

Environment:
- Interpreter: `.venv/bin/python`
- Dependencies installed: `numpy`, `pandas`, `scikit-learn`, `matplotlib`

Baseline result (validated during automated sweep):
- Total test scripts: 44
- Passed: 38
- Failed: 6

Remaining failing scripts:
1. `ML Module 01/ex04/test.py`
   - `FileNotFoundError: [Errno 2] No such file or directory: './are_blue_pills_magic.csv'`
2. `ML Module 01/ex05/test.py`
   - `TypeError: 'int' object is not callable`
3. `ML Module 01/ex06/test.py`
   - `TypeError: 'int' object is not callable`
4. `ML Module 02/ex06/testMultivariate.py`
   - `FileNotFoundError: [Errno 2] No such file or directory: 'spacecraft_data.csv'`
5. `ML Module 02/ex06/testUnivariate.py`
   - `FileNotFoundError: [Errno 2] No such file or directory: 'spacecraft_data.csv'`
6. `ML Module 03/ex02/test.py`
   - `TypeError: only 0-dimensional arrays can be converted to Python scalars`

Command used:
```bash
.venv/bin/python -c "import subprocess;from pathlib import Path;files=sorted({p for p in Path('ML Modules').rglob('test*.py') if p.is_file()});passed=[];failed=[]
for p in files:
 r=subprocess.run(['.venv/bin/python',str(p)],capture_output=True,text=True)
 (passed if r.returncode==0 else failed).append((str(p),r.returncode,(r.stderr.strip() or r.stdout.strip())))
print('Passed:',len(passed));print('Failed:',len(failed))"
```
