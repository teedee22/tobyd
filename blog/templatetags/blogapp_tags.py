# Taken from https://www.accordbox.com/blog/wagtail-tutorials-10-add-comment-support-wagtail-blog/
from django.template import Library

import six

register = Library()


@register.simple_tag()
def post_date_url(post, blog_page):
    post_date = post.date
    url = blog_page.url + blog_page.reverse_subpage(
        'post_by_date_slug',
        args=(
            post_date.year,
            '{0:02}'.format(post_date.month),
            '{0:02}'.format(post_date.day),
            post.slug,
        )
    )
    return url


@register.inclusion_tag('blog/comments/disqus.html', takes_context=True)
def show_comments(context):
    blog_page = context['blog_page']
    post = context['post']
    path = post_date_url(post, blog_page)

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
            'disqus_identifier': post.pk,
            'request': context['request']}
