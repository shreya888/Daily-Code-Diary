# Exception Handling in Python

Exception handling is a fundamental aspect of programming. Errors detected <em>during execution</em> such that program is unable to continue its normal flow are called exceptions and are not unconditionally fatal. Effective exception handling allows programs to recover from unexpected situations without crashing, providing a smoother user experience facilitating debugging with improved code reliability, even preventing data loss or worse corrupted data. Without proper exception handling, errors could disrupt the flow of execution, leading to crashes or unexpected behavior that negatively impacts the user's interaction with the software.

## Syntax and Usage of Exception Handling Constructs
Python's exception handling mechanism revolves around four main keywords:
1. **try**: The `try` block is used to wrap the code that may raise an exception. If an exception occurs within the `try` block, Python looks for an appropriate `except` block to handle it.
2. **except**: The `except` block catches and handles exceptions raised within the corresponding `try` block. It allows developers to specify how to handle specific types of exceptions or generic exceptions.
3. **else (optional)**: The `else` block is executed if no exceptions occur within the `try` block. It is typically used to execute code that should run only if the `try` block completes successfully.
4. **finally (optional)**: The `finally` block is executed regardless of whether an exception occurs in the `try` block. It is executed as the last task before the try statement completes. It is commonly used for cleanup operations, such as closing files or releasing resources.
```python
# Run Try block code first
try:
    # May raise an exception
    result = some_function()
# Execute Exception code only when there is an exception
except SomeException:
    # Handle specific exception
    handle_specific_exception()
except AnotherException:
    # Handle another specific exception
    handle_another_exception()
# No exeptions? Run Else block code
else:
    # Code to execute if no exceptions occur
    handle_no_exception()
# Always run Finally code
finally:
    # Cleanup code that always runs
    cleanup_operations()
```
Flowchart below explains the flow in a program:

![image](https://github.com/shreya888/Daily-Code-Diary/assets/25200389/c8c39f53-b71d-4b24-bbb2-8d19d3ec3da7)


