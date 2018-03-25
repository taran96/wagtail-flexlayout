from wagtail.core import blocks


class FlexItemBlock(blocks.StructBlock):
    """
    A block that contains rich text `content` in a div with the flex css value
    as `flex`.
    """
    flex = blocks.IntegerBlock(min_value=0)
    content = blocks.RichTextBlock()

    class Meta:
        template = 'wagtail_flexlayout/flex.html'


class BaseFlexBlock(blocks.StructBlock):
    """
    A base block which contains a `ListBlock` of `FlexItemBlock`.
    """
    flex_items = blocks.ListBlock(FlexItemBlock())


class FlexColumnBlock(BaseFlexBlock):
    """
    A block which represents its items in a column.
    """

    class Meta:
        icon = 'cogs'
        template = 'wagtail_flexlayout/flex_column.html'


class FlexRowBlock(BaseFlexBlock):
    """
    A block which represent its items in a row.
    """

    class Meta:
        icon = 'cogs'
        template = 'wagtail_flexlayout/flex_row.html'
