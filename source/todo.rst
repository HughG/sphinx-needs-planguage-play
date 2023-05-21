====
TODO
====


In Progress
====

* Add other types: Quality Requirements


Blocked
----

* Come up with some other way to represent relationships which plays into Sphinx-Needs' idea of links, but also allows me to put qualifiers (textual or variants) on any given link.  Might be default options values which use links_from_content (or a similar custom fucnction) along with filtering by the target need type?
  * See https://github.com/useblocks/sphinx-needs/discussions/926.


Things to Do
====

Next things to try (in no order, as yet).

* Use needs_ide_directive_snippets.
* Add some form of Levels, e.g., Sphinx Fields -- but not sure Sphinx-Needs allows that easily, without custom Python.
  * Try having each level as a direct option of the need, as per https://github.com/useblocks/sphinx-needs/discussions/926#discussioncomment-5948573
  * Try need_parts for Quality Requirement levels?
* Try fixing the VSCode extension workflowFolder bug.
* Investigate https://sphinx-modeling.useblocks.com/.
* Put Jira ticket links as extra info in JSON output.
  * Probably requires a custom option parser or custom handling, to treat a specific field as list (at the Sphinx level) such that the JSON output is also a list (via the Needs Builder).
  * Alternatively, could just pull them out of the "tests" field with a regex :-)
* Try list2need.
* Add a warning if the Source, Author, or Owner don't contain an email.
* Add warnings for requirements which have (type-specific) tags I don't want.
* Add warnings for requirements which don't have (type-specific) tags I want to require.
* Add Qualifiers, of different kinds.
* Add a warning when content or any tag values contain uncertain text.
* Allow Author and Owner, at least (maybe not Source), to be inherited at a page level, or from parent needs.
* Link to users on Confluence, and broaden Source/Author/Owner validation to allow those instead of email.
* Generate the above links using custom Sphinx Roles.
* Add info to test links to show test pass/fail.

  * Probably requires creating a Source for the test run output and processing that XML.
  * Use the correct branch, based on the document version!

* Get general reStructureText VSCode extension to not keep spitting out errors.
* Use needreport.
* Try needs_extra_links -- but I can't see how to render them *as* links from Jinja templates!
* Add explicit directives which wrap Sphinx-Needs (for ease of typing, specific customisations, and to abstract over it).


To Not Do (Yet)
====

These might be useful but are pretty standard, so not top of the list to look at.

* Intersphinx (linking between generated documentation).
* Docs with multiple versions you can navigate between (https://github.com/sphinx-contrib/sphinxcontrib-versioning for self-hosted, as opposed to https://readthedocs.org/).
* Adding comments to pages: https://sphinx-notes.github.io/isso/ -- needs you to run a "comments server".


Things Done
====

* Use default role to indicate uncertain text.
* Add other types: Design Constraints.
* Work out whether it would be helpful to use "need parts".  Might depend on JSON output.
  * No: the text of the "part" is in an interpreted text role "span", so can't contain further markup or structure.
* Link to Jira tickets.
* Figure out how to link to as-yet-undefined needs with just a warning, rather than an error.
  * Just seems to work now :-)
* Investigate IDE support.
* Link to Automated test results on Bamboo.
  * Ideally, using the same role usage as the Jira link.  It looks like a role returns multiple nodes, so we can have more than one textual link.  Might need a role argument for which output build covers it.  (Ideally we'd have one build which aggregated results from elsewhere, so we could just refer to that from doc, allowing us to refactor test builds without breaking doc.)
* Add metadata for Source, Author, and Owner.
* Investigate using variants for Planguage Qualifiers.
  * Could be used at need level to `:delete:`, `:hide:`, or de-emphasize (`:status:`?) requirements based on variants.
  * I don't think these could be applied within a Quality Requirement to qualify different levels, or othewise within the content or other options of a need.  So, might not be the right approach.
  * Could try using `:needextend:` with a variant, to override specific parts of a need.  It won't flow as nicely in the source, but since you can replace or extend options it might work.  I don't know if you can replace or extent the content, though.
* Convert other relationship types into needs_extra_links.
