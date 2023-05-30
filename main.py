from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="og:image" content="https://cdn.discordapp.com/avatars/959816718803431424/d1962358692ad47c4c6359be51027eb8.png?size=2048">
    <meta name="og:title" content="Gigzas">
    <meta name="og:description" content="Very racist and bombed L">
    <title>Document</title>
</head>
<body>
    
</body>
</html>"""
