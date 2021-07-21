
def rewrite_github_links(markdown: str, page, config, files):
    return markdown.replace('](../', f"]({config['repo_url']}blob/master/")
