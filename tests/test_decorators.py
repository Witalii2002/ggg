import os

import pytest

from src.decorators import log


# Helper function to clear log file after each test
def clear_logfile(filename):
    if os.path.exists(filename):
        os.remove(filename)


# ----- Тесты для декоратора log -----

# def test_log_success_console(capsys):
#     @log()
#     def my_function(x, y):
#         return x + y
#
#     result = my_function(1, 2)
#     captured = capsys.readouterr()  # Captures stdout and stderr
#     assert "my_function ok" in captured.out
#     assert str(result) in captured.out  # Ensure the result is also captured
#     assert captured.err == "" # Ensure nothing was written to stderr


def test_log_error_console(capsys):
    @log()
    def my_function(x, y):
        return x / y  # Potential ZeroDivisionError

    with pytest.raises(ZeroDivisionError):  # Verify that exception is still raised
        my_function(1, 0)
    captured = capsys.readouterr()
    assert "my_function error: ZeroDivisionError" in captured.out
    assert "Inputs: (1, 0), {}" in captured.out
    assert captured.err == ""  # Ensure nothing was written to stderr


def test_log_success_file():
    filename = "test_log.txt"
    clear_logfile(filename)  # Ensure the logfile is empty before the test

    @log(filename=filename)
    def my_function(x, y):
        return x + y

    result = my_function(3, 4)  # run function, log it to file

    with open(filename, "r") as f:
        log_content = f.read()  # read the log file and save to log_content

    assert "my_function ok" in log_content
    assert result == 7

    clear_logfile(filename)  # Delete logfile


def test_log_error_file():
    filename = "test_log.txt"
    clear_logfile(filename)

    @log(filename=filename)
    def my_function(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):  # Verify exception is still raised
        my_function(5, 0)

    with open(filename, "r") as f:
        log_content = f.read()

    assert "my_function error: ZeroDivisionError" in log_content
    assert "Inputs: (5, 0), {}" in log_content  # Make sure inputs were logged.

    clear_logfile(filename)


# def test_log_no_args_no_filename(capsys):
#
#     @log()
#     def my_function():
#         return "Success"
#
#     my_function()
#     captured = capsys.readouterr()  # Captures stdout and stderr
#     assert "my_function ok" in captured.out
#     assert "Success" in captured.out
#     assert captured.err == ""
