$(document).ready(function() {
$('#faders').css('display', 'none');
$('#faders').fadeIn(1500);

$('.link').click(function() {
event.preventDefault();
newLocation = this.href;
$('#faders').fadeOut(0, newpage);
});
function newpage() {
window.location = newLocation;
}
});
