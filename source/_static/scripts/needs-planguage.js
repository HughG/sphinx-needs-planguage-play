$(document).ready(function () {
    // Add line-break opportunities after every "." in each ID link.
    $('a.reference').html(function (index, html) {
        return html.replace(/_/g, '_\u200B');
    });
    $('aside.needs-planguage-id-heading').html(function (index, html) {
        return html.replace(/_/g, '_\u200B');
    });

    // Hack the layout to "merge" the right header cell into the center one.
    $('td.head_left').remove();
    $('td.head_center').attr('colspan', 5);
    $('td.head_right').attr('colspan', 1);
    $('td.footer_left').remove();
    $('td.footer').attr('colspan', 6);
    $('td.footer_right').remove();
})
