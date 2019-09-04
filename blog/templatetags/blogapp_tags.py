from django.template import Library

import six

register = Library()

# Adapted from https://www.accordbox.com/blog/wagtail-tutorials-10-add-comment-support-wagtail-blog/
@register.inclusion_tag('blog/comments/disqus.html', takes_context=True)
def show_comments(context):
    blog_page = context['page']
    path = blog_page.get_parent().url + blog_page.url

    raw_url = context['request'].get_raw_uri()
    parse_result = six.moves.urllib.parse.urlparse(raw_url)
    abs_path = six.moves.urllib.parse.urlunparse([
        parse_result.scheme,
        parse_result.netloc,
        path,
        "",
        "",
        ""
    ])

    return {'disqus_url': abs_path,
            'disqus_identifier': blog_page.pk,
            'request': context['request']}
