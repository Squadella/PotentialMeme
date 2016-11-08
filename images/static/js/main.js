$('li input').click(function(e){
    e.preventDefault();
    var id = $(this).attr('id');

    $.ajax({
        url:'/images/'+id+'/upVote/'
    })
})

$('span input').click(function(e){
    e.preventDefault();
    var id = $(this).attr('id');

    $.ajax({
        url:'/images/'+id+'/fav/'
    })
})