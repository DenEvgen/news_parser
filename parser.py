import re


class Parser:
    def __init__(self, content):
        self.content = content
        self.encode_page = self.content.read()
        self.charset = self.content.headers.get_content_charset()
        self.decode_page = self.encode_page.decode(self.charset)

    def parse_header(self):
        result = re.findall(r'<h1.*?>(.*?)</h1>', self.decode_page)
        header = []
        for i in range(len(result)):
            text = re.sub(r'(\<(/?[^>]+)>)', '', result[i])
            text_with_any_simb1 = text.replace('&nbsp;', ' ')
            text_with_any_simb2 = text_with_any_simb1.replace('&laquo;', '«')
            text_with_any_simb3 = text_with_any_simb2.replace('&laquo;', '»')
            header.append(text_with_any_simb3)
        return header

    def parse_paragraphs(self):
        result = re.findall(r'<p.*?>(.*?)</p>', self.decode_page)
        links = []
        # for i in range(len(result)):
        #     link = re.findall(r'"((?:http|https)s?://.*?)"', result[i])
        #     links.append(link)

        art = []
        for i in range(len(result)):
            el = result[i]
            main_link = re.search(r'(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w\.-]*)*\/?', el)
            if main_link:
                main_link = "[" + main_link.group(0) + "]"
            else:
                main_link = ''
            text = re.sub(r'<a.*?href="(.*?)".*?>', main_link + ' ', result[i])
            text_span_clean = re.sub(r'<.*?span.*?>', '', text)
            clean_text = text_span_clean.replace('&mdash;', '-')
            text_with_any_symb = clean_text.replace('&nbsp;', ' ')
            text_with_any_symb = text_with_any_symb.replace('&laquo;', '«')
            text_with_any_symb = text_with_any_symb.replace('&raquo;', '»')
            text_with_any_symb = re.sub(r'(\<(/?[^>]+)>)', '', text_with_any_symb)
            art.append(text_with_any_symb)

        art_wl = []
        for i in range(len(art)):
            text = art[i].replace('</a>', '')
            art_wl.append(text)

        return art_wl
