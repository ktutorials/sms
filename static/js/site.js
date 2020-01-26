
$(document).ready(function() {

    $.getStudents = function(){
        $( "#studentsList" ).empty();
        fetch("/api/v1/students")
         .then(response => response.json())
         .then(response => {
            console.log(response.students);
            $( response.students ).each(function( index ) {
                 $( "#studentsList" ).append(createCard(this));
             });
        });
    }

    $.getStudents();

    $.hideStudents = function(){
        $( "#studentsList" ).addClass("hidden");
        $( "#registerBtn" ).addClass("hidden");
        $( "#registerStudent" ).removeClass("hidden");
    }

    $.showStudents = function(){
        $( "#registerStudent" ).addClass("hidden");
        $( "#registerBtn" ).removeClass("hidden");
        $( "#studentsList" ).removeClass("hidden");
    }

    $.resetInputs = function(){
        var $doc = $("#registerStudent");
        $doc.find( "input").val('');
        $doc.find( "select").val('KG');
    }

    // show registration form on click of register btn
    $( "#registerBtn" ).click(function( event ) {

        // Stop form/btn from submitting/default normally
        event.preventDefault();

        $.hideStudents();

    });

    // show registration form on click of register btn
    $( "#resetBtn" ).click(function( event ) {

        // Stop form/btn from submitting/default normally
        event.preventDefault();

        $.resetInputs();

    });

    $( "#cancelBtn" ).click(function( event ) {

        // Stop form/btn from submitting/default normally
        event.preventDefault();

        $.showStudents();

    });

    // Attach a click handler to the submit button
    $( "#submitStdBtn" ).click(function( event ) {
    
        // Stop form/btn from submitting/default normally
        event.preventDefault();
    
        // Get some values from elements on the page:
        //var $doc = $( document );

        var $doc = $("#registerStudent");

        //console.log( $( document ).serializeArray() );
        var jsonData = objectifyArray($doc.find( "input").serializeArray());
        var selectData = objectifyArray($doc.find( "select").serializeArray());
        if(!jsonData || !selectData){
            $( "#results" ).empty().append("Please enter values for required fields.");
            return
        }
        $.extend(jsonData, selectData);

        console.log(jsonData);
        var url = "/api/v1/students";
    
        // Send the data using post
        var request = $.ajax( {
            url:url,
            method: "POST",
            headers: {
                        "Content-Type": "application/json"
                     },
            data: JSON.stringify(jsonData),
            dataType: "json"
        });
    
        // Put the results in a div
        request.done(function( data ) {
            console.log( data );
            $.showStudents();
            $.resetInputs();
            if (data.success){
                $( "#results" ).empty().append("Student is registered!");
                $.getStudents();
            } else {
                $( "#results" ).empty().append("Failed to register student at this time. Please try again later.");
            }
        });
        request.fail(function(error){
            console.log( error );
            $( "#results" ).empty().append( JSON.stringify(error) );
        });
        request.always(function() {
            console.log( "finished" );
        });
    });
});

function createCard(student){
    var card = document.createElement("div");
    card.setAttribute("class", "card");
    card.setAttribute("style", "width : 18rem;");
    var cardBody = document.createElement("div");
    cardBody.setAttribute("class", "card-body");
    var title = document.createElement("h5");
    title.setAttribute("class", "card-title");
    title.innerHTML = student.Name;
    var grade = document.createElement("h6");
    grade.setAttribute("class", "card-subtitle");
    grade.innerHTML = student.Grade;
    var hobbies = document.createElement("p");
    hobbies.setAttribute("class", "card-text");
    hobbies.innerHTML = student.Hobbies;

    cardBody.append(title);
    cardBody.append(grade);
    cardBody.append(hobbies);
    card.append(cardBody);
    return card;

}

function objectifyArray(dataArray) {//serialize data function

    var returnArray = {};
    for (var i = 0; i < dataArray.length; i++){
        var val = dataArray[i]['value'].trim();
        if(val.length == 0) return
        returnArray[dataArray[i]['name']] = val;
    }
    return returnArray;
  }