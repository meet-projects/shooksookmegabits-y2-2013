$(document).ready(function() {
	var xLogin = false;
	var xRegister = false;
	$('#loginButton').click(function() {
		xLogin = !xLogin;
		if(xLogin)
			$("#login_formBOX").css('visibility', 'visible');
		else
			$("#login_formBOX").css('visibility', 'hidden');
	});

	$('#registerButton').click(function() {
		xRegister = !xRegister;
		if(xRegister)
			$("#register_formTEXT").css('visibility', 'visible');
		else
			$("#register_formTEXT").css('visibility', 'hidden');
	});
});



