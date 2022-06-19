#!/usr/bin/env python3

from flask import Flask, request


app = Flask(__name__)

@app.route('/')
def main_page():
    return '<i>Nothing to see here</i>'


if __name__ == "__main__":
    app.run()