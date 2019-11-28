# shogi

A shogi game written in Python

---

## Summary

The program creates the shogi board, places the pieces on it and allows user to select and move each kind of piece

#### Features

* creation of the shogi board
* display of the shogi board
* initial setting of pieces
* piece selection 
* piece movement

#### Known issues

* no piece capture implemented
* no bounds validation on piece movement
* no piece promotions
* no piece drops

## Requirements

The following packages are required by sitrack-test

| Package Name | URL                                                           | Minimum required version |
|--------------|---------------------------------------------------------------|--------------------------|
| Python       | https://www.python.org/downloads/                             | `3.7`                    |
| git          | https://git-scm.com/book/en/v2/Getting-Started-Installing-Git | `latest`                 |

## Directory structure

```bash
$ tree
├── classes
├── shogi.py
└── README.md
```

| Dirname | Description                                                         |
|---------|---------------------------------------------------------------------|
| classes | This directory contains board and piece classes                     |



## Installation

1. Checkout the repo
```bash
$ git clone git@github.com:GustavoJE/eventbrite.git
```
2. Run the application
```bash
$ python shogi.py
```
