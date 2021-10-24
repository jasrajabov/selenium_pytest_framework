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
        return template

    def jinja_temp_data(self):
        template = self.handle_template()
        data = self.handle_xml_to_html()

        total_ = int(data.get('tests'))
        skipped_ = int(data.get('skipped'))
        fail_ = int(data.get('failures'))
        errors_ = int(data.get('errors'))
        time_ = data.get('time')
        host_ = data.get('hostname')
        timestamp_ = data.get('timestamp')

        output = template.render(
            skipped=skipped_,
            fail=fail_,
            errors=errors_,
            passed=total_ - sum([skipped_, errors_, fail_]),
            time=time_,
            host=host_,
            timestamp=timestamp_
        )
        print(output)
        return output

    def generate_email(self):
        output = self.jinja_temp_data()
        with open("templates/out_email.html", 'w') as out:
            out.write(output)

if __name__ == '__main__':
    run = EmailGenerator()
    run.generate_email()