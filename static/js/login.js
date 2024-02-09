$(document).ready(function () {
    $("#toggle-password").click(function () {
        var passwordField = $("#id_password");
        var passwordFieldType = passwordField.attr('type');

        if (passwordFieldType === 'password') {
            passwordField.attr('type', 'text');
        } else {
            passwordField.attr('type', 'password');
        }
    });
});