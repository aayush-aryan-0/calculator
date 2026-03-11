# Scientific Calculator (Tkinter)

A desktop **Scientific Calculator** built using **Python and Tkinter**.  
It supports basic arithmetic operations along with several scientific functions such as trigonometry, logarithms, square roots, factorial, and exponentiation.

The calculator parses mathematical expressions using a **custom Infix to Postfix conversion algorithm**, and then evaluates them using a postfix evaluation stack.

---

## Features

- Basic arithmetic operations  
  `+  -  ×  ÷  mod`

- Scientific functions
  - `sin`
  - `cos`
  - `tan`
  - `log`
  - `sqrt`
  - `factorial (!)`

- Expression parsing
  - Custom **Infix → Postfix conversion**
  - Postfix evaluation using a stack

- Parentheses support `()`

- Error handling
  - Division by zero
  - Invalid expressions
  - Invalid factorial inputs

- GUI built with **Tkinter**

---

## Technologies Used

- **Python 3**
- **Tkinter** (GUI framework)
- **math module**

---

## How It Works

1. The calculator accepts expressions in **infix notation**.
2. The program converts the expression to **postfix notation** using a stack-based algorithm.
3. The postfix expression is then evaluated using another stack.
4. The result is displayed in the calculator interface.

---

## Supported Operations

| Operation | Symbol |
|----------|--------|
Addition | `+`
Subtraction | `-`
Multiplication | `x`
Division | `/`
Modulus | `mod`
Exponent | `^`
Factorial | `!`
Square Root | `sqrt`
Logarithm | `log`
Trigonometry | `sin cos tan`

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/scientific-calculator-tkinter.git
