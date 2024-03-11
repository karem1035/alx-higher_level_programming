# 0x12. JavaScript - Warm up

## Background Context

JavaScript is used for many things. Here, you will use JavaScript for 2 reasons:

1. Scripting (same as we did with Python)
2. Web front-end

For the moment, and for learning all basic concepts of this language, we will do some scripting. After, we will make our AirBnB project dynamic by using Javascript and JQuery.

---

## Resources

- Writing JavaScript Code
- Variables
- Data Types
- Operators
- Operator Precedence
- Controlling Program Flow
- Functions
- Objects and Arrays
- Intrinsic Objects
- Module patterns
- var, let and const
- JavaScript Tutorial
- Modern JS

---

## Learning Objectives

- Why JavaScript programming is amazing?
  - The go to language for web
  - Client-Side Scripting, Asynchronous Programming, DOM Manipulation
  - Cross-Platform Compatibility, Libraries and Frameworks
  - Prototype-Based Inheritance
  - And much more
- How to run a JavaScript script?
  - By adding the src of the JS file to HTML File
  - Or at the terminal by doing the following
    - `#!/usr/bin/node` adding as the first line of the script
    - Allow executing
- How to create variables and constants?
  - var, let, const
- What are differences between var, const and let?
  - var: globally hoisted const and let are not
  - var: lexically scoped var and let are block scoped
  - var is older than let, const but not recommended to use nowadays
  - var and let can be reassigned const cannot
- What are all the data types available in JavaScript?
  - String, Number, Boolean, Objects, Null, NaN, Undefined, Sybols
- How to use the if, if ... else statements?
  - `if (condition){code block} else if (condition){code block} else {code block}`
- How to use comments?
  - By adding `// comments` if a single line comment or `/* comments */` if a multible lines comments
- How to affect values to variables?
  - `var/let/const varName = value`
- How to use while and for loops?
  - `while(condition is true){keep doing this code block}`
- How to use break and continue statements?
  - `break` gets us out of the loop immediately
  - `continue` skips the current iteration to the next one
- What is a function and how do you use functions?
  - a block of code can be reused (maybe not IIFE).
  - get assigned to a name and might accepts parameters.
  - gets defined as a normal variable with a name.
- What does a function that does not use any return statement return?
  - `undefined`
- Scope of variables?
  - Global scope
  - Block Scope
  - Function Scope (ES6+)
- What are the arithmetic operators and how to use them?
  - +, -, /, \*, %, ++, --
  - Perform arithmetic operations to varibales or literal values
- How to manipulate dictionary?
  - `objName.keyToAddOrChange = theValue`
- How to import a file?
  - we use `const moduleName = require('fileName');` to export
  - we use `import * as moduleName from 'fileName';` to import

---

## Copyright - Plagiarism

- You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
- You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
- You are not allowed to publish any content of this project.
- Any form of plagiarism is strictly forbidden and will result in removal from the program.

---

## Requirements

### General

- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 20.04 LTS using node (version 14.x)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/node
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should be semistandard compliant (version 16.x.x). Rules of Standard + semicolons on top. Also as reference: AirBnB style
- All your files must be executable
- The length of your files will be tested using wc

---

## More Info

### Install Node 14

`$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash`
`$ sudo apt-get install -y nodejs`

### Install semi-standard

`$ sudo npm install semistandard --global`
