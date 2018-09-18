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
    
    $("#add-book").submit(function(event) {
        
		var form = $(this);			
		var author = form.find("input[name='author']");
		var genre = form.find("input[name='genre']");

		var authorVal = author.val();
		var genreVal = genre.val();
		var pattern_1 = /^([a-zA-Z]+)?([\s])?([a-zA-Z]+[-]?[a-zA-Z]+)?([\s])?$/;
		var pattern_2 = /^([a-zA-Z]+)?([-])?([a-zA-Z]+)?([\s])?$/;


		if (!pattern_1.test(authorVal)) {
		    event.preventDefault();
		    $("#author-help").addClass("error");
		} else if (!pattern_2.test(genreVal)) {
			event.preventDefault();
			$("#author-help").removeClass("error");
			$("#genre-help").addClass("error");
		} else {
		    $("#author-help").removeClass("error");
			$("#genre-help").removeClass("error");
		}
	});
    
});