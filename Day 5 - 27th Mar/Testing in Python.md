# Testing in Python

### 1. Exploratory Testing
* A crucial step where testers explore the application <em>without predefined test cases</em>.
* Involves <em>manual</em> interaction with the application to discover bugs, usability issues, and other potential problems.

### 2. Automated Testing
* Process of using software tools to execute pre-scripted tests on a software application before it is released into production.
* Helps in quickly identifying any regressions or bugs in the codebase. Key components of automated testing include:
  - **Test Step**: Sequential actions performed on the software application to verify/validate its behavior.
  - **Test Assertion**: Condition or criteria that the software must meet to pass the test. Assertions are used to validate the expected outcomes of test cases.
  - **Integration Testing**: Tests the interactions between different components or modules of the software application to ensure the integrated units function correctly together, detecting issues related to data communication, dependencies, and compatibility.

### 3. Unit Testing
* Tests individual units or components of a software application in isolation.
* Focuses on testing small units of code, such as functions or methods, to ensure each unit performs as expected.
* Helps in identifying defects early in the development cycle and facilitate code refactoring and maintenance.
* Inspired by Java's JUnit framework, Python provides support for unit testing through libraries like `unittest`.

### References
1. [Real Python - Python Testing](https://realpython.com/python-testing/)
2. [Python Documentation - unittest](https://docs.python.org/3/library/unittest.html)
3. [Python Testing Guide](https://docs.python-guide.org/writing/tests/)
4. [How to Write Unit Tests for Python Functions](https://www.freecodecamp.org/news/how-to-write-unit-tests-for-python-functions/)

Feel free to explore these resources to deepen your understanding of testing practices in Python.
