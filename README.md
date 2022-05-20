# _All Roads Lead to Philosophy_

In 2008, a Wikipedia user discovered that if you follow the first main link of almost all (about 90% at the time) Wikipedia articles, you'd eventually get to the Philosophy page. Here's a Wikipedia article on the very topic.

The original constraints in the above article are as follows:
- The first link must be non-parenthesized and non-italicized link
- External links, links to the current page, or red links (links to non-existent pages) are ignored
- Stopping when reaching "Philosophy", a page with no links or a page that does not exist, or when a loop occurs

As of today, Wikipedia pages are much more complex and trying these would likely get you in a lot of loops.

The goal in this project is to find the fastest road to philosophy. Here, the rule is slightly changed. When a loop is discovered, it is avoided and the next main link is followed.