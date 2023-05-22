import subprocess
import sys

# ANSI escape sequences for colors
GREEN = '\033[92m'
END = '\033[0m'

# Text to display
text = GREEN + "OK" + END


def test_reverse_string():
    # Test case 1: No arguments passed
    process = subprocess.Popen(['python', 'exec.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    assert stdout == b'', 'Test case 1 failed: Unexpected output'
    assert stderr == b'', 'Test case 1 failed: Unexpected error'
    # Print the text
    print("test 1" , text)

    # Test case 2: One argument passed
    process = subprocess.Popen(['python', 'exec.py', 'hello'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    assert stdout == b'OLLEH\n', 'Test case 2 failed: Unexpected output'
    assert stderr == b'', 'Test case 2 failed: Unexpected error'
    print("test 2" , text)

    # Test case 3: Multiple arguments passed
    process = subprocess.Popen(['python', 'exec.py', 'hello', 'world'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    assert stdout == b'DLROW OLLEH\n', 'Test case 3 failed: Unexpected output'
    assert stderr == b'', 'Test case 3 failed: Unexpected error'
    print("test 3" , text)

    # Test case 5: Arguments with non-string data types
    process = subprocess.Popen(['python', 'exec.py', 'hello', '123', '4.56', 'True'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    assert stdout == b'EURt 65.4 321 OLLEH\n', 'Test case 5 failed: Unexpected output'
    assert stderr == b'', 'Test case 5 failed: Unexpected error'
    print("test 4" , text)

test_reverse_string()
