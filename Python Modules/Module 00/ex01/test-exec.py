import subprocess
import sys

def test_reverse_string():
    # Test case 1: No arguments passed
    process = subprocess.Popen(['python', 'exec.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    assert stdout == b'', 'Test case 1 failed: Unexpected output'
    assert stderr == b'', 'Test case 1 failed: Unexpected error'

    # Test case 2: One argument passed
    process = subprocess.Popen(['python', 'exec.py', 'hello'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    assert stdout == b'olleh\n', 'Test case 2 failed: Unexpected output'
    assert stderr == b'', 'Test case 2 failed: Unexpected error'

    # Test case 3: Multiple arguments passed
    process = subprocess.Popen(['python', 'exec.py', 'hello', 'world'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    assert stdout == b'olleh dlrow\n', 'Test case 3 failed: Unexpected output'
    assert stderr == b'', 'Test case 3 failed: Unexpected error'

    # Test case 4: Arguments with special characters
    process = subprocess.Popen(['python', 'exec.py', 'hello', '$%^&*()'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    assert stdout == b'olleh )(*&^%$#\n', 'Test case 4 failed: Unexpected output'
    assert stderr == b'', 'Test case 4 failed: Unexpected error'

    # Test case 5: Arguments with non-string data types
    process = subprocess.Popen(['python', 'exec.py', 'hello', '123', '4.56', 'True'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    assert stdout == b'olleh 321 65.4 eurT\n', 'Test case 5 failed: Unexpected output'
    assert stderr == b'', 'Test case 5 failed: Unexpected error'

test_reverse_string()
