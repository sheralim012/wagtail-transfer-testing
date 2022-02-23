from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import PageChooserPanel
from wagtail.core.blocks import PageChooserBlock
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import (
    PageChooserPanel,
    StreamFieldPanel,
)


class HomePage(Page):
    featured_page = models.ForeignKey(
        'wagtailcore.Page', null=True, blank=True, on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        PageChooserPanel('featured_page'),
    ]


class PageButtonBlock(blocks.StructBlock):
    page = blocks.PageChooserBlock()
    text = blocks.CharBlock(required=False, max_length=255)


class Article(Page):
    body = StreamField([
        ('page_button', PageButtonBlock()),
        ('page', PageChooserBlock()),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]


class Poll(Page):
    pass 