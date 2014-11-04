$(document).ready(function () {
//    content for the delete popover...
    var content = "<p>Are you sure you want to delete this?<br/><br/>" +
        "<input value='DELETE' type='submit' class='btn btn-primary real-delete'>" +
        "<button type='button' id='cncl-delete' class='btn btn-primary'>CANCEL</button>" +
        "</p>";


//    this is the 'delete' button
    $('.ppr').on("click", function () {
//        when you click the delete button, signals the conent to change
        var $content = $(content);

        //        associate the id of the delete button (which references the blog entry) with the actual deletion button
        var formId = $(this).parent().attr('id');
        $content.find('input').attr('form', formId);
        var options = {
            content: $content,
            html: true
        };

        //this is a bootstrap thing...
        $('.ppr').popover(options);
        $(this).popover('toggle');
    });


});

////    $('#real-delete').on("click", function(){
////        $('#delete-form').submit()
////    });
//
//    $(".real-delete").click(function () {
////        when you click the real-delete button, submit the associated form...
////        1. grab the id from the real-delete button
////        2. submit the form with that id...
//        var id = $(this).attr('form')
//        $(id).submit();
//        $("#delete-form").submit();
//    });


