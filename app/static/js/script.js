$(function() {

	var now = new Date();
	var d = now.getDate();
	var m = now.getMonth()+1;
	var y = now.getFullYear();
	var now_str='' + (m<=9 ? '0' + m : m) + '/' + (d <= 9 ? '0' + d : d) + '/' + y;

	$( "#due_date" ).datepicker({dateFormat:"mm/dd/yy"}).datepicker("setDate",new Date());
	$( "#posted_date" ).val(now_str)
	$( "#due_date" ).attr('readonly',true)
	$( "#posted_date" ).attr('readonly',true)

});
