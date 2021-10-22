import os
import xml.etree.ElementTree as ET
from jinja2 import Environment, FileSystemLoader


class EmailGenerator:

    def handle_xml_to_html(self):
        metadata = {}
        for file_ in os.listdir('./tests/junit'):
            if file_.endswith('.xml'):
                tree = ET.parse('./tests/junit/' + file_)
                root = tree.getroot()
                for child in root:
                    metadata[child.tag] = child.attrib
        
        if metadata:
            metadata = metadata['testsuite']

        return metadata
    
    def handle_template(self):
        file_loader = FileSystemLoader('templates')
        env = Environment(loader=file_loader)
        template = env.get_template('email.html')
        data = self.handle_xml_to_html()
        print(data)
        output = template.render(
            pass_ = data.get('tests'),
            skipped = data.get('skipped'),
            fail = data.get('failures'),
            errors = data.get('errors')
        )
        print(output)
        with open("templates/out_email.html", 'w') as out:
            out.write(output)



    

            
    

if __name__ == '__main__':
    run = EmailGenerator()
    run.handle_template()