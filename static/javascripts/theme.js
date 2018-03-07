// Theme custom js methods
$(document).ready(function(){

  // Hide institutional tab in income articles 
  var state = getUIState();
  if (state.field == 'income' && state.view == 'economic') {
    $('#tabs a[href="#institutional"]').remove();
  }
});