import yaml
from jinja2 import Environment, FileSystemLoader
from pdflatex import PDFLaTeX
import argparse
import os

DEFAULT_OUTPUT = 'output'
DEFAULT_YAML = 'data.yaml'
DEFAULT_TEMPLATE = 'template.tex'


def yaml_to_pdf(yaml_file, template_file, output_file, keep_latex):
    output_file = output_file + '.tex'
    # Load data from Yaml
    with open(yaml_file) as f:
        data = yaml.safe_load(f)

    # Load Jinja Template
    env = Environment(
            loader=FileSystemLoader('.'),
            comment_start_string='{=',
            comment_end_string='=}',
    )

    template = env.get_template(template_file)

    # Render template
    rendered_template = template.render(data)

    # Write rendered LaTeX to file
    with open(output_file, 'w') as f:
        f.write(rendered_template)

    # Make pdf from Latex
    pdfl = PDFLaTeX.from_texfile(output_file)
    pdf, log, completed_process = pdfl.create_pdf(keep_pdf_file=True, keep_log_file=False)

    if not keep_latex:
        os.remove(output_file)


def main():
    parser = argparse.ArgumentParser(description='convert structured yaml data into a pdf resume')
    parser.add_argument('-y', '--yaml', type=str, default=DEFAULT_YAML,
                        help='Choose yaml file (Default = data.yaml)')
    parser.add_argument('-o', '--output', type=str, default=DEFAULT_OUTPUT,
                        help='Choose a name used for the outputed files (Default = output)')
    parser.add_argument('-t', '--template', type=str, default=DEFAULT_TEMPLATE,
                        help='Choose a template for the resume (Default = template.tex)')
    parser.add_argument('-l', '--latex', action='store_true',
                        help='When enabled script will output the filled in LaTeX template')
    args = parser.parse_args()

    yaml_to_pdf(args.yaml, 'template.tex', args.output, args.latex)


if __name__ == '__main__':
    exit(main())
