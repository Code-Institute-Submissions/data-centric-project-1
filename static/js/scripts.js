$( document ).ready(function() {
    
    $(".genres-sm a:gt(3)").hide();
    $(".show-genres").click(function() {
        $(".genres-sm a:gt(3)").show();
        $(".show-genres").hide();
    });
    
    $(".authors-sm a:gt(3)").hide();
    $(".show-authors").click(function() {
        $(".authors-sm a:gt(3)").show();
        $(".show-authors").hide();
    });
    
    $(".genres-lg a:gt(3)").hide();
    $(".show-genres").click(function() {
        $(".genres-lg a:gt(3)").show();
        $(".show-genres").hide();
    });
    
    $(".authors-lg a:gt(3)").hide();
    $(".show-authors").click(function() {
        $(".authors-lg a:gt(3)").show();
        $(".show-authors").hide();
    });
    
    $("#quick-searches a:gt(4)").hide();
    $(".show-searches").click(function() {
        $("#quick-searches a:gt(4)").show();
        $(".show-searches").hide();
    });
    
});