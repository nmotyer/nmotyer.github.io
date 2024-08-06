import glob
import os
from lxml import etree
from datetime import datetime

def create_sitemap(directory, base_url, extra_urls):
    # Create the root element
    urlset = etree.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")

    # Find all .md files in the directory
    md_files = glob.glob(os.path.join(directory, "*.md"))

    # Add URLs for .md files
    for md_file in md_files:
        filename = os.path.basename(md_file)
        file_id = os.path.splitext(filename)[0]  # Remove the .md extension
        url = f"{base_url}/news/{file_id}/"
        
        url_element = etree.SubElement(urlset, "url")
        loc_element = etree.SubElement(url_element, "loc")
        loc_element.text = url

        # Optional: Add lastmod element with the current date
        lastmod_element = etree.SubElement(url_element, "lastmod")
        lastmod_element.text = datetime.now().strftime("%Y-%m-%d")

    # Add extra URLs
    for extra_url in extra_urls:
        url_element = etree.SubElement(urlset, "url")
        loc_element = etree.SubElement(url_element, "loc")
        loc_element.text = extra_url

        # Optional: Add lastmod element with the current date
        lastmod_element = etree.SubElement(url_element, "lastmod")
        lastmod_element.text = datetime.now().strftime("%Y-%m-%d")

    # Convert the tree to a string and write to sitemap.xml
    tree = etree.ElementTree(urlset)
    tree.write("sitemap.xml", pretty_print=True, xml_declaration=True, encoding="UTF-8")

# Directory containing .md files
directory = "./content/news"
# Base URL for the site
base_url = "https://eduhub.news"
# Extra URLs to include in the sitemap
extra_urls = [
    f"{base_url}/news",
    f"{base_url}/contact",
    f"{base_url}/faq"
]

create_sitemap(directory, base_url, extra_urls)
