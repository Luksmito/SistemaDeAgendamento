$(document).ready(function() {

   
    var select_health_insurance = $('#health-insurance')
    var what_health_insurance = $('#what-health-insurance')
    
    $(what_health_insurance).css('display', 'none');
    $(select_health_insurance).change(function() {
        var selected = $(this).val();
        if (selected == "sim") {
            $(what_health_insurance).css('display', 'block');
        } else {
            $(what_health_insurance).css('display', 'none');
        }
    })
});

