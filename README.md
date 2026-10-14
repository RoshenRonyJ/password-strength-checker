# Password Strength Checker

A Python command-line tool that rates password strength, explains how to improve weak passwords, and detects common passwords used in dictionary attacks.

## Features

- Hidden password input using `getpass`, so the password is never shown on screen
- Scores passwords out of 6 based on length and character variety
- Rates passwords as Weak, Medium or Strong
- Gives specific tips to improve weak passwords
- Checks against a list of 10,000 common passwords and flags them as weak, even if they pass the other rules

## Why the common password check matters

Attackers rarely start with random guesses. They use **dictionary attacks**, trying lists of the most common passwords first. A password like `Password1!` passes typical rules (uppercase, number, symbol) but would be cracked almost instantly. This tool catches that.

## How to run

1. Install Python 3
2. Clone this repository
3. Run: `python checker.py`

## Example

Enter your password:
Your password is 10 characters long.
Score: 0/6
Weak

How to improve it:
- This is one of the most common passwords. Attackers try these first, so it can be cracked almost instantly.

## Tech used

- Python 3
- Common password list from [SecLists](https://github.com/danielmiessler/SecLists)

## What I learned

- Working with sets for fast lookups
- Reading files safely with encodings
- How dictionary attacks work and why password rules alone aren't enough

## Future improvements

- Check passwords against real data breaches using the Have I Been Pwned API
- Estimate how long the password would take to crack
