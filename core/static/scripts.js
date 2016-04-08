function show_hide_connection()
	{
		if (document.getElementById('connection').style.display == 'none')
			document.getElementById('connection').style.display = 'block';

		else
			document.getElementById('connection').style.display = 'none';
			
		document.getElementById('connection').style.right = ((screen.width / 2) - 200) + 'px';
		document.getElementById('connection').style.bottom = ((screen.height / 2) - 100) + 'px';
	}