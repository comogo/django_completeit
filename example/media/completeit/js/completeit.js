$(document).ready(function(){
    $focus = null;
    
    $('.completeit').focus(function(){
        $focus = $(this);
    });
    
    $('.completeit').autocomplete({
        key: $(this).attr('completeit_key'),
        source: function(request, response){
            $.ajax({
                url: "/completeit/",
                dataType: "json",
                type: 'GET',
                data: {
                    k: $focus.attr('completeit_key'),
                    q: request.term,
                    f: 'json'
                },
                success: function(data){
                    response( $.map(data.results, function(item){
                        return {
                            label: item.value,
                            value: item.value
                        }
                    }));
                    
                }
            });
        },
        select: function( event, ui ) {
            alert(ui.item.label);
		},
        minLength: 2
    });
});