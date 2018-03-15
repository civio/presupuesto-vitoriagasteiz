// Theme custom js methods
$(document).ready(function(){

  // Customize institutional breakdown
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

  // Explanatory note for policies expenditure breakdown
  var notes = {
    'es': {
      'text': '<p>Por aplicación del Decreto Foral de Álava 56/2015 se produce una reordenación de la organización '+
        'y codificación de la clasificación por programas del presupuesto, por lo que la comparación y evolución de '+
        'estos no es homogénea antes y después del 2015.</p><p>Por ejemplo hasta 2014 existía "limpieza viaria"y a '+
        'partir de 2015 se divide en "limpieza viaria", "recogida de residuos" y "tratamiento de residuos".</p>',
    },
    'eu': {
      'text': '<p>Arabako 56/2015 Foru Dekretua aplikatzearen ondorioz, aldatu egin ziren aurrekontuko programen '+
        'antolakuntza eta sailkapen-kodeak, eta, horrenbestez, horien alderaketa eta bilakaera ez dira homogeneoak, '+
        '2015. urtearen aurretik eta ondoren.</p><p>Esate baterako, 2014ra arte, "kale-garbiketa" zegoen, eta 2015az '+
        'geroztik, berriz, "kale-garbiketa", "hondakin-bilketa" eta "hondakinen tratamendua" bereizten dira.</p>',
    },
  };

  var note = window.location.pathname.match(/^\/(es|eu)\/politicas\/\d\d\/.*/)

  if (note) {
    $('.policies .policies-content .policies-chart').append( '<div class="policy-description">'+notes[note[1]].text+'</div>' );
  }

});