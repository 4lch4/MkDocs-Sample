def on_page_markdown(self, markdown, *, page, config, files):
    page.file.url           = page.file.url.replace("_index", "index")
    page.file.dest_uri      = page.file.dest_uri.replace("_index", "index")
    page.file.abs_dest_path = page.file.abs_dest_path.replace("_index", "index")
