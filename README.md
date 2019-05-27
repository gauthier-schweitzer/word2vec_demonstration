# word2vec in a simple and fully customizable app

## Summary
Thanks to this repo, you can simply deploy a local app to show how Word2Vec can be used. You can customize the design to adapt it to clients.

## Dependencies
Download [GoogleNews-vectors-negative300.bin.gz](https://github.com/mmihaltz/word2vec-GoogleNews-vectors) in the folder.

To run the app, you have to first setup a conda environement using the `environment.yml` file. Then, once the environment is created, activate it (`conda activate <nameoftheenv>`) and run `python app.py` in the Prompt

## Technical details
The app is based on Python Flask. For interactivity, it uses Javascript and Ajax Callbacks, which make it slightly harder to understand at first sight.

## Adaptation
To adapt the design, modify `templates/index.html`

## Design of the App

![Alt text](App_screenshot.png?raw=true "Title")
