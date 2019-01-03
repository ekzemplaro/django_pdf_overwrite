// -----------------------------------------------------------------------
//	pdf_overwrite.js
//
//					Jan/03/2019
//
// -----------------------------------------------------------------------
jQuery (function ()
{
	jQuery("#outarea_aa").html ("*** pdf_overwrite.js *** start *** Jan/03/2019 ***")

	click_check_proc ()

	jQuery("#outarea_hh").html ("*** pdf_overwrite.js *** end *** Jan/03/2019 ***")
})

// -----------------------------------------------------------------------
function click_check_proc ()
{
	jQuery ("button.check").click (function ()
		{
		var str_out = "*** clicked ***<br />"
		jQuery("#outarea_bb").html(str_out)

		const url = "/pdf_overwrite/main/"

		var params = {}
		params['pdf_out'] = jQuery("#pdf_out").val()
		params['receiver'] = jQuery("#receiver").val()
		params['price'] = jQuery("#price").val()

		var str_out = ""
		str_out += params['pdf_out'] + "<br />"
		str_out += params['receiver'] + "<br />"
		str_out += params['price'] + "<br />"

		jQuery("#outarea_cc").html(str_out)

		jQuery.post(url,params,function (res)
			{
			var str_tmp = "*** check *** ccc ***<br />"
			jQuery("#outarea_ee").html(str_tmp)
			jQuery("#outarea_ff").text(res)
			})
		})
}

// -----------------------------------------------------------------------
