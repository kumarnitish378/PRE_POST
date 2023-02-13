import wikipediaapi

wiki = wikipediaapi.Wikipedia(
        language='en',
        extract_format=wikipediaapi.ExtractFormat.WIKI
)

page = wiki.page('Member of Parliament')

print("Page - Summary: %s" % page.summary[0:60])

# Get the first paragraph from the page
first_paragraph = " ".join(page.text.split('\n')[0:10])

tts = gTTS(first_paragraph, lang='en', slow=False)

print("First Paragraph: %s" % first_paragraph)