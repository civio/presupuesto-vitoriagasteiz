// Theme custom js methods
$(document).ready(function(){

  var expandPoliciesTable = function () {
    setTimeout(function() {
      $('#myGrid a.toggle.expand').trigger('click');
    }, 500);
  }
  
  var state = getUIState();
 
  // Hide institutional tab in income articles 
  if (state.field == 'income' && state.view == 'economic') {
    $('#tabs a[href="#institutional"]').remove();
  }

  // Expand table for institutional tab
  if (state.view == 'functional' || state.view == 'economic') {
    $('#tabs a[href="#institutional"]').click(expandPoliciesTable);
    $('#year-selection').change(expandPoliciesTable);
  } else if  (state.view == 'institutional') {
    expandPoliciesTable();
    $('#year-selection').change(expandPoliciesTable);
  }

});