#!/usr/bin/python

import os, shutil
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

DROPBOX_PATH = os.path.expanduser("~/Dropbox/")
LOCAL_FOLDER = os.path.expanduser("~/workspace/local/")
CLOUD_FOLDER = DROPBOX_PATH + "cloud/"
IGNORE_FILE = ".dropbox_ignore"
VERBOSE = 1

class Handler(PatternMatchingEventHandler):
    def on_any_event(self, event):
        if VERBOSE:
            print event

    def on_created(self, event):
        destination = event.src_path.replace(LOCAL_FOLDER, CLOUD_FOLDER)
        if event.is_directory:
            if os.path.lexists(destination):
                shutil.rmtree(destination)
            else:
                os.mkdir(destination)
        else:
            if os.path.lexists(destination):
                os.remove(destination)
            else:
                os.symlink(event.src_path, destination)

    def on_deleted(self, event):
        destination = event.src_path.replace(LOCAL_FOLDER, CLOUD_FOLDER)
        if event.is_directory:
            if os.path.lexists(destination):
                shutil.rmtree(destination)
        else:
            if os.path.lexists(destination):
                os.remove(destination)

    def on_modified(self, event):
        pass

    def on_moved(self, event):
        source = event.src_path.replace(LOCAL_FOLDER, CLOUD_FOLDER)
        destination = event.dest_path.replace(LOCAL_FOLDER, CLOUD_FOLDER)
        if os.path.lexists(destination):
            os.remove(destination)
        if event.is_directory:
            os.rename(source, destination)
        else:
            if os.path.lexists(source):
                os.remove(source)
            os.symlink(event.dest_path, destination)

def readIgnoreFile():
    excludes=[]
    with open(IGNORE_FILE,'r') as f:
        for line in f.readlines():
            line = line.strip()
            if line and not line.startswith("#"):
                excludes.append(LOCAL_FOLDER + line)
    return excludes

if __name__ == "__main__":
    path = LOCAL_FOLDER
    excludes = readIgnoreFile()
    if VERBOSE:
        print excludes
    event_handler = Handler(
        ignore_patterns = excludes,
        case_sensitive = True
    )
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    observer.join()
