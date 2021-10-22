import os
import shutil

def handle_xml_to_html():
    for file_ in os.listdir('./tests/junit'):
        if file_.endswith('.xml'):
            shutil.copy('./tests/junit/'+file_, './tests/junit/email.html')
    

if __name__ == '__main__':
    handle_xml_to_html()