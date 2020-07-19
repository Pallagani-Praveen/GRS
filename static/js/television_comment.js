$().ready(function(){
    $('.com-heart').addClass('dislike');
});




function togglelike(num){
    let id = 'heart'+num;
    let i = document.getElementById(id);
    if (i.classList.contains('liked'))
    {
        i.classList.remove('liked');
        i.classList.add('dislike');
    }
    else{
        i.classList.add('liked');
        i.classList.remove('dislike');
    }
}


function addElement(username,comment){
    let ul = document.getElementById('com-ul');
    let childs = document.querySelector('ul#com-ul li');
    let li = document.createElement('li');
    li.setAttribute('class','d-flex justify-content-between');

    let user = `<span class="text-danger"> from ${username}</span>`;

    let review =document.createElement('i');
    review.innerHTML = comment+user;
    li.appendChild(review);

    let heart = document.createElement('i');
    heart.setAttribute('class','fa fa-heart com-heart text-light');
    let id = Math.random();
    heart.setAttribute('id','heart'+id);
    heart.setAttribute('onclick','togglelike("'+id+'")');

    li.appendChild(heart);

    ul.appendChild(li);
    if(!childs){
        document.querySelector('ul#com-ul span').remove();
    }

    
    
}


$('#comment-form').on('submit',(e)=>{
    e.preventDefault();
    let username = $('input[name="username"]').val();
    let televisionid = $('input[name="televisionid"]').val();
    let comment = $('#comment-input').val();
    let senddata = {
        "username":username,
        "televisionid":televisionid,
        "comment":comment,
        csrfmiddlewaretoken:$('input[name="csrfmiddlewaretoken"').val(),
    }
    
    $.ajax({
        type:"POST",
        url:'http://localhost:8000/GRSapp/maketelcom',
        data:senddata,
        dataType:'json',
        success:function(resdata){
            console.log('success');
        }
    });

    addElement(username,comment);
    $('#comment-input').val('');

});

