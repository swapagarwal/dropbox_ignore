# .dropbox_ignore

A python script that allows you to use patterns to exclude certain files from your Dropbox.

### Usage

Set the following variables appropriately in ```monitor.py```:

```DROPBOX_PATH``` Location of your Dropbox folder

```LOCAL_FOLDER``` Location of the folder you want to sync

```CLOUD_FOLDER``` Location of that folder in your Dropbox cloud

```IGNORE_FILE``` Location of the ignore file to be used

### Example

Want to exclude that annoying node_modules folder? Just add ```node_modules/*``` in your ignore file and you're good to go!

### Requirements

```
pip install -r requirements.txt
```

### Note

This is in its very early stage of development. (Use it only for testing purposes, for now!)
