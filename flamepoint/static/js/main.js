$('.filters ul li').click(function(){
  $('.filters ul li').removeClass('active');
  $(this).addClass('active');
  
  var data = $(this).attr('data-filter');
  $grid.isotope({
    filter: data
  })
});

var $grid = $(".grid").isotope({
  itemSelector: ".all",
  percentPosition: true,
  masonry: {
    columnWidth: ".all"
  }
});

$(window).scroll(function(){
	$grid.isotope( 'layout' );
})

  var onePageClick = function() {


$(document).on('click', '#fpoint-nav a[href^="#"]', function (event) {
  event.preventDefault();

  var href = $.attr(this, 'href');

  $('html, body').animate({
      scrollTop: $($.attr(this, 'href')).offset().top - 70
  }, 500, function() {
    // window.location.hash = href;
  });
});

};

onePageClick();

// scroll
var scrollWindow = function() {
		$(window).scroll(function(){
			var $w = $(this),
					st = $w.scrollTop(),
					navbar = $('.fpoint_navbar'),
					sd = $('.js-scroll-wrap');

			if (st > 150) {
				if ( !navbar.hasClass('scrolled') ) {
					navbar.addClass('scrolled');	
				}
			} 
			if (st < 150) {
				if ( navbar.hasClass('scrolled') ) {
					navbar.removeClass('scrolled sleep');
				}
			} 
			if ( st > 350 ) {
				if ( !navbar.hasClass('awake') ) {
					navbar.addClass('awake');	
				}
				
				if(sd.length > 0) {
					sd.addClass('sleep');
				}
			}
			if ( st < 350 ) {
				if ( navbar.hasClass('awake') ) {
					navbar.removeClass('awake');
					navbar.addClass('sleep');
				}
				if(sd.length > 0) {
					sd.removeClass('sleep');
				}
			}
		});
	};
	scrollWindow();

// Burger Menu
var burgerMenu = function() {

$('body').on('click', '.js-fh5co-nav-toggle', function(event){

  event.preventDefault();

  if ( $('#fpoint-nav').is(':visible') ) {
    $(this).removeClass('active');
  } else {
    $(this).addClass('active');	
  }

  
  
});

};
burgerMenu();
