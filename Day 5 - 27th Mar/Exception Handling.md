# Exception Handling in Python

Exception handling is a fundamental aspect of programming. Errors detected <em>during execution</em> such that program is unable to continue its normal flow are called exceptions and are not unconditionally fatal. Effective exception handling allows programs to recover from unexpected situations without crashing, providing a smoother user experience facilitating debugging with improved code reliability, even preventing data loss or worse corrupted data. Without proper exception handling, errors could disrupt the flow of execution, leading to crashes or unexpected behavior that negatively impacts the user's interaction with the software.

## Syntax and Usage of Exception Handling Constructs
Python's exception handling mechanism revolves around four main keywords:
1. **try**: The `try` block is used to wrap the code that may raise an exception. If an exception occurs within the `try` block, Python looks for an appropriate `except` block to handle it.
2. **except**: The `except` block catches and handles exceptions raised within the corresponding `try` block. It allows developers to specify how to handle specific types of exceptions or generic exceptions. Code can have as many exception blocks as needed.
3. **else (optional)**: The `else` block is executed if no exceptions occur within the `try` block. It is typically used to execute code that should run only if the `try` block completes successfully.
4. **finally (optional)**: The `finally` block is executed regardless of whether an exception occurs in the `try` block. It is executed as the last task before the try statement completes. It is commonly used for cleanup operations, such as closing files, releasing resources (memory, lock, semaphore, network resources, database connections, etc.) or rollback transactions.
   - If the try statement reaches a break, continue or return statement, the finally clause will execute just prior to the break, continue or return statement’s execution
   - If a finally clause includes a return statement, the returned value will be the one from the finally clause’s return statement, not the value from the try clause’s return
   - If exception occurs in try but is not caught in except clause, the exception is re-raised after the finally clause has been executed
   - If exception occurs during execution of an except or else clause, the exception is re-raised after the finally clause has been executed
```python
# Run Try block code first
try:
    # May raise an exception
    result = some_function()

# Exception code is executed when there is an exception in Try
except SomeException as e:  # Access the exception object (e) in the indented block
    # Handle specific exception
    print(e)  # Print exception error's string representation, which corresponds to the error message attached to the object
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
Flowchart below explains the flow in a program: [[3](https://rollbar.com/blog/throwing-exceptions-in-python)]

![image](https://github.com/shreya888/Daily-Code-Diary/assets/25200389/c8c39f53-b71d-4b24-bbb2-8d19d3ec3da7)


## Common Types of Exceptions
Python provides a wide range of built-in exception types to handle different error scenarios. Some common built-in exceptions include:
* `ZeroDivisionError`: Raised when division or modulo by zero occurs.
* `TypeError`: Raised when an operation or function is applied to an object of an inappropriate type.
* `ValueError`: Raised when a built-in operation or function receives an argument of the correct type but with an inappropriate value.
* `FileNotFoundError`: Raised when attempting to access a file or directory that does not exist.
* `KeyError`: Raised when a dictionary key is not found.
* `NameError`: Raised when an identifier is not found in the local or global namespace.

Read more at [[2](https://docs.python.org/3/library/exceptions.html)].

## Error vs. Exception
* Error typically refers to a syntax or logic mistake in the code that prevents it from executing.
* Exception is an event that disrupts the normal flow of the program during execution, often due to external factors such as bad data, broken network connectivity, corrupted databases, memory pressures, unexpected/invalid user inputs or resource unavailability.

## Raising and Handling Exceptions
The `raise` statement lets programmers to deliberately trigger/force a particular exception to occur. 
It requires specifying the exception to be raised as its sole argument, which can either be an instance of an exception or a class representing the exception (like a custom exception class). When an exception class is passed, it is automatically instantiated by invoking its constructor with no arguments.  
Additionally, for scenarios where we want to identify if an exception occurred but don't intend to handle it immediately, a simpler form of the raise statement enables us to re-raise the exception as below:
```python
try:
    # Raise a NameError with custom message
    raise NameError('HiThere')
except NameError:
    # Print a message indicating an exception occurred
    print('An exception flew by!')
    # Re-raise the caught exception
    raise
```
```
An exception flew by!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: HiThere
```

## Exception Chaining
If an unhandled exception occurs inside an except block, it will have the exception being handled attached to it and included in the error message. Python allows exceptions to be chained together, preserving the context of the original exception while raising a new one. This can be useful for providing additional information about the error or wrapping lower-level exceptions with higher-level exceptions.
```python
try:
    # May raise an exception
    open("database.sqlite")
except OSError:
    # Handling the original exception and raising a new one
    raise RuntimeError("unable to handle OS error")
```
```
Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'database.sqlite'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 6, in <module>
RuntimeError: unable to handle OS error
```
To indicate that an exception is a direct consequence of another, the `raise` statement allows an optional from clause. For example, in above code change line 6 `raise RuntimeError("unable to handle OS error")` as follows:
```python
# "exc" must be exception instance or None
# "from None" will disabling automatic exception chaining
raise RuntimeError("unable to handle OS error") from exc
```
This will change the message to:
```
Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
  File "<stdin>", line 3, in func
ConnectionError

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 6, in <module>
RuntimeError: unable to handle OS error
```


## User-Defined Exceptions
Create custom exception classes by subclassing Python's built-in `Exception` class for application-specific exception hierarchies tailored to the needs of the project.
```python
# Define user-defined/custom exceptions as a class
class CustomErrorName(Exception):
    def __init__(self, message):
        self.message = message

# Raise custom exception
try:
    if (condition):
        raise CustomErrorName("Custom error message")
except CustomErrorName:
    pass
```

## Conclusion
Exception handling is a critical aspect of Python programming, enabling developers to write robust and reliable code that gracefully handles errors and unexpected situations. By understanding the syntax, usage, and best practices of exception handling in Python, developers can create more resilient and maintainable applications.

## References:
1. https://docs.python.org/3/tutorial/errors.html
2. https://docs.python.org/3/library/exceptions.html
3. https://rollbar.com/blog/throwing-exceptions-in-python
4. https://www.w3schools.com/python/python_try_except.asp
5. https://realpython.com/python-exceptions
6. https://www.programiz.com/python-programming/user-defined-exception
