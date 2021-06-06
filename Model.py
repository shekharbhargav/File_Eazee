#MODULES FOR ORGANIZER
from watchdog.observers import Observer
import time
from pathlib import Path
from watchdog.events import FileSystemEventHandler
import os
import json
import shutil
#MODULES FOR BACKUP
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
#MODULES FOR CLEANER



class Model():
    FILE_FORMATS={'.html5': 'HTML', '.html': 'HTML', '.htm': 'HTML', '.xhtml': 'HTML', '.jpeg': 'IMAGES', '.jpg': 'IMAGES', '.tiff': 'IMAGES', '.gif': 'IMAGES', '.bmp': 'IMAGES', '.png': 'IMAGES', '.bpg': 'IMAGES', 'svg': 'IMAGES', '.heif': 'IMAGES', '.psd': 'IMAGES', '.avi': 'VIDEOS', '.flv': 'VIDEOS', '.wmv': 'VIDEOS', '.mov': 'VIDEOS', '.mp4': 'VIDEOS', '.webm': 'VIDEOS', '.vob': 'VIDEOS', '.mng': 'VIDEOS', '.qt': 'VIDEOS', '.mpg': 'VIDEOS', '.mpeg': 'VIDEOS', '.3gp': 'VIDEOS', '.oxps': 'DOCUMENTS', '.epub': 'DOCUMENTS', '.pages': 'DOCUMENTS', '.docx': 'DOCUMENTS', '.doc': 'DOCUMENTS', '.fdf': 'DOCUMENTS', '.ods': 'DOCUMENTS', '.odt': 'DOCUMENTS', '.pwi': 'DOCUMENTS', '.xsn': 'DOCUMENTS', '.xps': 'DOCUMENTS', '.dotx': 'DOCUMENTS', '.docm': 'DOCUMENTS', '.dox': 'DOCUMENTS', '.rvg': 'DOCUMENTS', '.rtf': 'DOCUMENTS', '.rtfd': 'DOCUMENTS', '.wpd': 'DOCUMENTS', '.xls': 'DOCUMENTS', '.xlsx': 'DOCUMENTS', '.ppt': 'DOCUMENTS', 'pptx': 'DOCUMENTS', '.a': 'ARCHIVES', '.ar': 'ARCHIVES', '.cpio': 'ARCHIVES', '.iso': 'ARCHIVES', '.tar': 'ARCHIVES', '.gz': 'ARCHIVES', '.rz': 'ARCHIVES', '.7z': 'ARCHIVES', '.dmg': 'ARCHIVES', '.rar': 'ARCHIVES', '.xar': 'ARCHIVES', '.zip': 'ARCHIVES', '.aac': 'AUDIO', '.aa': 'AUDIO', '.dvf': 'AUDIO', '.m4a': 'AUDIO', '.m4b': 'AUDIO', '.m4p': 'AUDIO', '.mp3': 'AUDIO', '.msv': 'AUDIO', 'ogg': 'AUDIO', 'oga': 'AUDIO', '.raw': 'AUDIO', '.vox': 'AUDIO', '.wav': 'AUDIO', '.wma': 'AUDIO', '.txt': 'PLAINTEXT', '.in': 'PLAINTEXT', '.out': 'PLAINTEXT', '.pdf': 'PDF', '.py': 'PYTHON', '.xml': 'XML', '.exe': 'EXE', '.sh': 'SHELL'}
    DIRECTORIES = {
        "HTML": [".html5", ".html", ".htm", ".xhtml"],
        "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
                   ".heif", ".psd"],
        "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
                   ".qt", ".mpg", ".mpeg", ".3gp"],
        "DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                      ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                      ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                      "pptx"],
        "ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                     ".dmg", ".rar", ".xar", ".zip"],
        "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
                  ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
        "PLAINTEXT": [".txt", ".in", ".out"],
        "PDF": [".pdf"],
        "PYTHON": [".py"],
        "XML": [".xml"],
        "EXE": [".exe"],
        "SHELL": [".sh"]

    }
    def __init__(self):
        
        pass
    def organizer(self):
        pass
    def event_handler(self):
        pass
    def backup(self,file_list):
        for file in file_list:
            pass

        pass
    def authenticator(self,credfile):#credfile = "filename.txt"
        gauth = GoogleAuth()
        gauth.LoadCredentialsFile(credfile)
        if gauth.credentials is None:
            # Authenticate if they're not there
            gauth.LocalWebserverAuth()
        elif gauth.access_token_expired:
            # Refresh them if expired
            gauth.Refresh()
        else:
            # Initialize the saved creds
            gauth.Authorize()
        # Save the current credentials to a file

        gauth.SaveCredentialsFile("cred.txt")
        return gauth
