//Up vote event
$('li input').click(function(e){
    e.preventDefault();
    var id = $(this).attr('id');

    $.ajax({
        url:'/images/'+id+'/upVote/',
        success: function () {
            window.location.reload(true);
        }
    })
})

//Favorite event
$('span input').click(function(e){
    e.preventDefault();
    var id = $(this).attr('id');

    $.ajax({
        url:'/images/'+id+'/fav/',
        success: function () {
            window.location.reload(true);
        }
    })
})
